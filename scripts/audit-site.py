"""Read-only migration audit. Run after npm run build; emits JSON to stdout."""

import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.images, self.ids, self.paragraphs, self.text = [], [], [], [], []
        self.paragraph = None
        self.has_media = False
        self.ignore_text = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "img":
            self.images.append(attrs)
        if tag == "p":
            self.paragraph, self.has_media = "", False
        if tag in {"img", "iframe", "video", "audio", "svg"}:
            self.has_media = True
        if tag in {"script", "style"}:
            self.ignore_text = True

    def handle_endtag(self, tag):
        if tag == "p" and self.paragraph is not None:
            if not self.has_media:
                self.paragraphs.append(self.paragraph)
            self.paragraph = None
        if tag in {"script", "style"}:
            self.ignore_text = False

    def handle_data(self, data):
        if not self.ignore_text:
            self.text.append(data)
            if self.paragraph is not None:
                self.paragraph += data


root = Path(__file__).resolve().parent.parent
dist = root / "dist"
if not (dist / "index.html").exists():
    raise SystemExit("No built site found. Run npm run build first.")

redirects = {}
for line in (root / "public/_redirects").read_text().splitlines():
    if line.strip() and not line.startswith("#"):
        source, target, status = line.split()
        redirects[source.rstrip("/")] = target

report = {"pages": 0, "article_pages": 0, "missing_local_targets": [],
          "redirected_local_targets": [], "duplicate_ids": [],
          "url_image_alts": [], "empty_image_alts": [], "stray_markdown": [],
          "raw_embed_script_text": [], "empty_paragraphs": [], "retired_community_links": []}

for path in sorted(dist.rglob("*.html")):
    page = Page()
    page.feed(path.read_text())
    name = str(path.relative_to(dist))
    report["pages"] += 1
    duplicates = [key for key, count in Counter(page.ids).items() if count > 1]
    if duplicates:
        report["duplicate_ids"].append({"page": name, "ids": duplicates})
    for target in page.links + [image.get("src", "") for image in page.images]:
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        destination = redirects.get(url.path.rstrip("/"), url.path)
        dest = dist / unquote(destination.lstrip("/")) if destination.startswith("/") else path.parent / unquote(destination)
        if not dest.is_file() and not (dest / "index.html").is_file():
            report["missing_local_targets"].append({"page": name, "target": target})
        elif destination != url.path:
            report["redirected_local_targets"].append({"page": name, "target": target, "destination": destination})
    if not name.startswith("writing/") or name == "writing/index.html":
        continue
    report["article_pages"] += 1
    for image in page.images:
        alt = image.get("alt", "").strip()
        if alt.startswith(("http://", "https://")):
            report["url_image_alts"].append(name)
        elif not alt:
            report["empty_image_alts"].append(name)
    for paragraph in page.paragraphs:
        if re.fullmatch(r"\s*(\[|\]\(.*\))\s*", paragraph):
            report["stray_markdown"].append(name)
        if not paragraph.replace("\u200d", "").replace("\u200b", "").strip():
            report["empty_paragraphs"].append(name)
    if re.search(r"document\.write|createElement\(", " ".join(page.text)):
        report["raw_embed_script_text"].append(name)
    report["retired_community_links"].extend(
        {"page": name, "target": href} for href in page.links if "community.saent.com" in href
    )

print(json.dumps(report, indent=2))
