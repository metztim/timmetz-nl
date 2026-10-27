#!/usr/bin/env python3
"""Import verified Medium HTML while preserving existing writing URLs.

Run with a Python environment containing lxml and Pillow. Raw images and the
download journal stay beside the private ZIP; public images are separate copies.
"""
import argparse
import hashlib
import io
import json
import re
import threading
import time
import unicodedata
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlparse

from lxml import html
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def slug(title):
    text = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')


def link_url(value):
    return value.replace(' ', '%20').replace('(', '%28').replace(')', '%29')


def marked(inner, marker):
    if not inner.strip():
        return inner
    leading = inner[:len(inner) - len(inner.lstrip())]
    trailing = inner[len(inner.rstrip()):]
    return leading + marker + inner.strip() + marker + trailing


def convert(node, images, links):
    tag = node.tag.lower() if isinstance(node.tag, str) else ''
    if tag in ('script', 'style') or 'graf--title' in node.get('class', '').split():
        return ''
    if tag == 'img':
        src = node.get('src')
        if not src:
            return ''
        if src not in images:
            raise ValueError('Image absent from verified download journal: ' + src)
        return '\n\n![' + (node.get('alt', '').replace('[', '').replace(']', '')) + '](' + images[src]['publicUrl'] + ')\n\n'
    if tag in ('iframe', 'video', 'audio'):
        src = node.get('src')
        return '\n\n[Embedded media](' + link_url(src) + ')\n\n' if src else ''
    if tag == 'br':
        return '\\\n'
    if tag == 'hr':
        return '\n\n---\n\n'
    if tag == 'pre':
        text = node.text_content()
        fence = '`' * max(3, max([len(x) + 1 for x in re.findall(r'`+', text)] or [3]))
        return '\n\n' + fence + '\n' + text + '\n' + fence + '\n\n'
    inner = (node.text or '').replace('<', '&lt;').replace('>', '&gt;')
    for child in node:
        inner += convert(child, images, links) + (child.tail or '').replace('<', '&lt;').replace('>', '&gt;')
    if tag in ('strong', 'b'):
        return marked(inner, '**')
    if tag in ('em', 'i'):
        return marked(inner, '*')
    if tag == 'code':
        return '`' + node.text_content().replace('`', '\\`') + '`'
    if tag == 'a':
        href = node.get('href', '')
        if not href or not inner.strip() or '![' in inner:
            return inner
        parsed = urlparse(href)
        match = re.search(r'(?:-|/)([0-9a-f]+)$', parsed.path)
        if parsed.hostname and parsed.hostname.endswith('medium.com') and match and match.group(1) in links and not parsed.fragment:
            href = '/writing/' + links[match.group(1)]
        leading = inner[:len(inner) - len(inner.lstrip())]
        trailing = inner[len(inner.rstrip()):]
        return leading + '[' + inner.strip() + '](' + link_url(href) + ')' + trailing
    if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        return '\n\n' + '#' * max(2, min(4, int(tag[1]) - 1)) + ' ' + inner.strip() + '\n\n'
    if tag in ('ul', 'ol'):
        items = []
        for i, child in enumerate(node.xpath('./li'), 1):
            body = convert(child, images, links).strip()
            items.append((str(i) + '. ' if tag == 'ol' else '- ') + body.replace('\n', '\n  '))
        return '\n\n' + '\n'.join(items) + '\n\n'
    if tag == 'blockquote':
        return '\n\n' + '\n'.join('> ' + line for line in inner.strip().splitlines()) + '\n\n'
    if tag in ('p', 'figcaption', 'div', 'section', 'figure'):
        return '\n\n' + inner.strip() + '\n\n'
    return inner


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, required=True)
    parser.add_argument('--download', action='store_true')
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--interval', type=float, default=1.5)
    args = parser.parse_args()
    base = args.archive
    report = json.loads((base / 'archive-verification.json').read_text())
    assert sha((base / report['archiveFilename']).read_bytes()) == report['archiveSha256']
    inventory = json.loads((base / 'archive-post-inventory.json').read_text())
    existing = json.loads((ROOT / 'scripts/medium-existing-map.json').read_text())
    articles = [e for e in inventory if e['publishedAt'] and (e['classification'] == 'article_formatted_post' or e['id'] == '467708f2f51a')]
    new = [e for e in articles if e['id'] not in existing]
    work = base / 'website-import-2026-10-27'
    raw_dir = work / 'original-images'
    raw_dir.mkdir(parents=True, exist_ok=True)
    journal_path = work / 'image-downloads.json'
    journal = json.loads(journal_path.read_text()) if journal_path.exists() else {}
    previous_path = work / 'site-import.json'
    previous = json.loads(previous_path.read_text()) if previous_path.exists() else {'newPosts': []}
    generated_hashes = {e['file']: e['siteSha256'] for e in previous['newPosts']}
    urls = sorted({url for e in new for url in e['remoteImageUrls']})
    request_lock = threading.Lock()
    stopped = threading.Event()
    last_request = [0.0]

    def download(url):
        if stopped.is_set():
            raise RuntimeError('Batch stopped after browser challenge')
        assert urlparse(url).hostname == 'cdn-images-1.medium.com'
        if url in journal:
            record = journal[url]
            assert sha((raw_dir / record['rawFilename']).read_bytes()) == record['sha256']
            return url, record
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        for attempt in range(3):
            with request_lock:
                time.sleep(max(0, args.interval - (time.monotonic() - last_request[0])))
                last_request[0] = time.monotonic()
            try:
                with urllib.request.urlopen(req, timeout=45) as response:
                    data = response.read(15_000_001)
                    content_type = response.headers.get('Content-Type')
                break
            except urllib.error.HTTPError as error:
                if error.headers.get('Cf-Mitigated') == 'challenge':
                    stopped.set()
                    raise RuntimeError('Browser challenge requires a later retry') from error
                if error.code != 429 or attempt == 2:
                    raise
                delay = float(error.headers.get('Retry-After', 30))
                if delay > 60:
                    raise ValueError('Rate limit requires later retry: ' + str(delay)) from error
                time.sleep(delay)
        if len(data) > 15_000_000:
            raise ValueError('Image exceeds download limit: ' + url)
        image = Image.open(io.BytesIO(data))
        image.verify()
        ext = {'JPEG': '.jpg', 'PNG': '.png', 'GIF': '.gif', 'WEBP': '.webp'}.get(image.format)
        if not ext:
            raise ValueError('Unsupported image format: ' + str(image.format))
        name = sha(data)[:24] + ext
        (raw_dir / name).write_bytes(data)
        assert sha((raw_dir / name).read_bytes()) == sha(data)
        return url, {'rawFilename': name, 'sha256': sha(data), 'bytes': len(data), 'contentType': content_type}

    if args.download:
        failures = []
        with ThreadPoolExecutor(max_workers=4) as pool:
            tasks = {pool.submit(download, url): url for url in urls}
            for task in as_completed(tasks):
                try:
                    url, record = task.result()
                    journal[url] = record
                    journal_path.write_text(json.dumps(journal, indent=2) + '\n')
                except Exception as error:
                    failures.append({'url': tasks[task], 'error': str(error)})
                    if stopped.is_set():
                        for pending in tasks:
                            pending.cancel()
                        break
        (work / 'image-errors.json').write_text(json.dumps(failures, indent=2) + '\n')
        print(json.dumps({'downloaded': len(journal), 'failures': failures}), flush=True)
        if failures:
            raise SystemExit(1)
    if not args.write:
        return
    assert all(url in journal for url in urls), 'Complete image downloads before writing posts'
    public = ROOT / 'public/images/medium'
    public.mkdir(parents=True, exist_ok=True)
    for url in urls:
        record = journal[url]
        data = (raw_dir / record['rawFilename']).read_bytes()
        assert sha(data) == record['sha256']
        image = Image.open(io.BytesIO(data))
        name = record['rawFilename']
        if image.format != 'GIF' and not getattr(image, 'is_animated', False):
            output = io.BytesIO()
            image.save(output, 'WEBP', quality=90, method=6)
            if len(output.getvalue()) < len(data):
                data = output.getvalue()
                name = Path(name).stem + '.webp'
        assert len(data) < 5_000_000, 'Keep large binaries in private assets'
        target = public / name
        if target.exists():
            assert target.read_bytes() == data
        else:
            target.write_bytes(data)
        record['publicUrl'] = '/images/medium/' + name
        record['publicSha256'] = sha(data)
    links = dict(existing)
    for e in new:
        links[e['id']] = slug(e['title']) + '-' + e['id']
    results = []
    for e in new:
        raw = (base / 'extracted-posts' / Path(e['archivePath']).name).read_bytes()
        assert sha(raw) == e['sha256']
        root = html.fromstring(raw)
        body = root.xpath('//*[@data-field="body"]')[0]
        headings = body.xpath('.//h1|.//h2|.//h3|.//h4')
        for heading in headings[:2]:
            if len(slug(heading.text_content())) > 8 and slug(e['title']).endswith(slug(heading.text_content())):
                heading.set('class', heading.get('class', '') + ' graf--title')
        text = convert(body, journal, links)
        text = re.sub(r'\n[ \t]*\n(?:[ \t]*\n)+', '\n\n', text).strip()
        text = re.sub(r'^---\s*', '', text)
        summary = root.xpath('//*[@data-field="subtitle"]')
        description = summary[0].text_content().strip() if summary else ''
        if not description:
            paragraphs = body.xpath('.//p')
            description = paragraphs[0].text_content().strip() if paragraphs else e['title']
        description = re.sub(r'\s+', ' ', description)[:200]
        source = e.get('publishedInventoryUrl') or e['canonicalUrl']
        tags = ['medium']
        if 'saent' in (source + ' ' + e['title']).lower():
            tags.append('saent')
        front = '---\n' + 'title: ' + json.dumps(e['title'], ensure_ascii=False) + '\n'
        front += 'description: ' + json.dumps(description, ensure_ascii=False) + '\n'
        front += 'pubDate: ' + e['publishedAt'][:10] + '\nsourceName: "Medium"\n'
        front += 'mediumUrl: ' + json.dumps(source) + '\ntags: ' + json.dumps(tags) + '\n---\n\n'
        target = ROOT / 'src/content/writing' / (links[e['id']] + '.md')
        output = front + text + '\n'
        if target.exists():
            if target.read_text() != output:
                assert sha(target.read_bytes()) == generated_hashes.get(str(target.relative_to(ROOT))), 'Refusing to overwrite an edited post: ' + str(target)
                target.write_text(output)
        else:
            target.write_text(output)
        results.append({'mediumId': e['id'], 'file': str(target.relative_to(ROOT)), 'sourceUrl': source, 'sourceSha256': e['sha256'], 'siteSha256': sha(target.read_bytes())})
    for e in articles:
        if e['id'] not in existing:
            continue
        target = ROOT / 'src/content/writing' / (existing[e['id']] + '.md')
        original = target.read_text()
        source = e.get('publishedInventoryUrl') or e['canonicalUrl']
        if re.search(r'^mediumUrl:', original, re.MULTILINE):
            assert re.search(r'^mediumUrl: (.+)$', original, re.MULTILINE).group(1) == json.dumps(source)
        else:
            front, body = original.split('---', 2)[1:]
            front += 'mediumUrl: ' + json.dumps(source) + '\n'
            target.write_text('---' + front + '---' + body)
    journal_path.write_text(json.dumps(journal, indent=2) + '\n')
    (work / 'site-import.json').write_text(json.dumps({'newPosts': results, 'existingPosts': existing, 'imageCount': len(urls)}, indent=2) + '\n')
    print(json.dumps({'newPosts': len(results), 'existingPosts': len(existing), 'imageUrls': len(urls), 'publicImageFiles': len(list(public.iterdir()))}), flush=True)


if __name__ == '__main__':
    main()
