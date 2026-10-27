"""Check the built Medium migration against its untouched account export."""
import argparse
import hashlib
import html as entities
import json
import re
from pathlib import Path

from lxml import html

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--archive', type=Path, required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
base = args.archive
manifest = json.loads((base / 'website-import-2026-10-27/site-import.json').read_text())
images = json.loads((base / 'website-import-2026-10-27/image-downloads.json').read_text())
inventory = {e['id']: e for e in json.loads((base / 'archive-post-inventory.json').read_text())}


def normalized(text):
    return re.sub(r'[^\w]', '', entities.unescape(text))


failures = []
for entry in manifest['newPosts']:
    slug = Path(entry['file']).stem
    page = root / 'dist/writing' / slug / 'index.html'
    if not page.exists():
        failures.append({'id': entry['mediumId'], 'error': 'Missing built article'})
        continue
    parsed = html.fromstring(page.read_bytes())
    prose = parsed.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," prose ")]')[0]
    saved = normalized(prose.text_content() + ' ' + parsed.xpath('//h1')[0].text_content())
    record = inventory[entry['mediumId']]
    raw = (base / 'extracted-posts' / Path(record['archivePath']).name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == record['sha256']
    source = html.fromstring(raw).xpath('//*[@data-field="body"]')[0]
    fragments = source.xpath('.//text()[not(ancestor::*[contains(concat(" ",normalize-space(@class)," ")," graf--title ")]) and not(ancestor::script) and not(ancestor::style)]')
    # Ordered-list numbers are rendered markers rather than DOM text.
    missing = [str(t).strip() for t in fragments if len(str(t).strip()) > 30 and normalized(re.sub(r'^\d+\.\s+', '', str(t).strip())) not in saved]
    if missing:
        failures.append({'id': entry['mediumId'], 'error': 'Text differs', 'fragments': missing})
    for src in prose.xpath('.//img/@src'):
        if not src.startswith('/images/medium/') or not (root / 'public' / src.lstrip('/')).is_file():
            failures.append({'id': entry['mediumId'], 'error': 'Image missing or still remote', 'src': src})
    canonicals = parsed.xpath('//link[@rel="canonical"]/@href')
    assert len(canonicals) == 1 and canonicals[0].rstrip('/') == 'https://www.timmetz.nl/writing/' + slug
    assert entry['sourceUrl'] in parsed.xpath('//footer//a/@href')
    published = parsed.xpath('//article/header//time/@datetime')
    assert published and published[0][:10] == record['publishedAt'][:10]

for medium_id, slug in manifest['existingPosts'].items():
    assert (root / 'dist/writing' / slug / 'index.html').is_file(), medium_id
for record in images.values():
    path = root / 'public' / record['publicUrl'].lstrip('/')
    assert hashlib.sha256(path.read_bytes()).hexdigest() == record['publicSha256']

result = {'newArticlesChecked': len(manifest['newPosts']), 'existingArticlesPreserved': len(manifest['existingPosts']), 'imageUrlsChecked': len(images), 'failures': failures}
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(bool(failures))
