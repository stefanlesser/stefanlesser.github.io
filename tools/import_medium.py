#!/usr/bin/env python3
"""
Import the three "Behind the Game" Medium posts into this Hugo site.

Source: Wayback Machine snapshots of the Medium pages, which embed the
full post content as structured JSON in window.__APOLLO_STATE__
(Paragraph items with type/text/markups, ImageMetadata, MediaResource).
The snapshots are in /tmp/medium-migrate/ (see docs below for URLs).

Transformations:
  - Item 0 (H3 title) -> front matter title.
  - Item 1 (H4 subtitle) -> front matter description (plain text).
  - P -> paragraph; H4 -> "### " heading; PQ -> "> " blockquote;
    ULI -> "- " list item (consecutive items merged into one list).
  - IMG -> local ![caption](/images/<uuid>.<ext>); the original is
    downloaded from miro.medium.com (full resolution) into static/images/.
    The UUID is derived deterministically from the Medium image ID, so
    re-runs produce the same filenames.
  - IFRAME -> Hugo youtube shortcode for YouTube embeds, a plain link
    for embedded tweets.
  - Inline markups EM/STRONG/A -> * / ** / [text](href); archive.org
    URL prefixes are stripped; [ and ] in text are escaped.
  - The Medium profile link (https://medium.com/@stefanlesser) is
    rewritten to the Behind the Game series page on this site.
  - All three posts get `series: behind-the-game` in the front matter;
    the series page lives in content/series/behind-the-game.md.

Usage:
    python3 tools/import_medium.py

Idempotent: content files are regenerated on every run; images are
only downloaded if missing.
"""

import json
import re
import sys
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

HUGO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = HUGO_ROOT / "content" / "post"
STATIC_IMAGES = HUGO_ROOT / "static" / "images"
SRC_DIR = Path("/tmp/medium-migrate")

# Wayback snapshots used as the content source:
#   blek.html         2019-12-18 https://medium.com/@stefanlesser/behind-the-game-blek-bdf9673984a0
#   hidden-folks.html 2025-09-05 https://medium.com/@stefanlesser/behind-the-game-hidden-folks-e6198dfa885a
#   pinout.html       2020-09-25 https://medium.com/@stefanlesser/behind-the-game-pinout-73a869ebba8f
POSTS = [
    {
        "html": SRC_DIR / "blek.html",
        "slug": "behind-the-game-blek",
        "date": "2017-09-16T09:57:46Z",
    },
    {
        "html": SRC_DIR / "hidden-folks.html",
        "slug": "behind-the-game-hidden-folks",
        "date": "2017-04-20T07:09:59Z",
    },
    {
        "html": SRC_DIR / "pinout.html",
        "slug": "behind-the-game-pinout",
        "date": "2017-04-06T06:39:58Z",
    },
]


def load_apollo(html_path: Path) -> dict:
    html = html_path.read_text()
    i = html.find('__typename":"Paragraph')
    if i < 0:
        sys.exit(f"error: no Apollo state in {html_path}")
    s = html.rfind("<script>", 0, i)
    e = html.find("</script>", i)
    js = html[s + 8 : e]
    if not js.startswith("window.__APOLLO_STATE__ = "):
        sys.exit(f"error: unexpected script in {html_path}")
    return json.loads(js[len("window.__APOLLO_STATE__ = "):])


def resolve(data: dict, ref):
    if isinstance(ref, dict):
        if "__ref" in ref:
            return data[ref["__ref"]]
        if ref.get("type") == "id":
            return data[ref["id"]]
    return ref


def get_items(data: dict) -> list:
    items = {}
    for k, v in data.items():
        m = re.match(r"Paragraph:(\w+)_(\d+)$", k)
        if m:
            items[int(m.group(2))] = v
    idxs = sorted(items)
    if idxs != list(range(len(idxs))):
        sys.exit(f"error: item indices not contiguous: {idxs[:5]}...{idxs[-5:]}")
    return [items[i] for i in idxs]


def strip_archive(url: str) -> str:
    url = re.sub(r"^https?://web\.archive\.org/web/\d+[a-z_]*/", "", url)
    # The Medium profile link becomes the series page on this site.
    return url.replace("https://medium.com/@stefanlesser", "/series/behind-the-game/")


def esc(text: str) -> str:
    return text.replace("\\", r"\\").replace("[", r"\[").replace("]", r"\]")


def render_item_markups(data: dict, item: dict) -> str:
    """Render an item's text with its inline markups as markdown."""
    text = item["text"]
    mks = []
    for m in item.get("markups") or []:
        m = resolve(data, m)
        if m is None:
            continue
        mks.append((m["type"], m["start"], m["end"], m.get("href")))

    def rec(s: int, e: int, scope: list) -> str:
        if s >= e:
            return ""
        cands = [m for m in scope if m[1] >= s and m[2] <= e]
        if not cands:
            return esc(text[s:e])
        # outermost first: earliest start, then longest span
        cands.sort(key=lambda m: (m[1], -(m[2] - m[1])))
        m = cands[0]
        # Medium sometimes includes edge spaces in a markup range; keep
        # them outside the markers so the markdown emphasis stays valid
        s2, e2 = m[1], m[2]
        while s2 < e2 and text[s2] == " ":
            s2 += 1
        while e2 > s2 and text[e2 - 1] == " ":
            e2 -= 1
        out = esc(text[s : s2])
        inner = rec(
            s2, e2, [x for x in cands if x[1] >= s2 and x[2] <= e2 and x is not m]
        )
        t, _, _, href = m
        if t == "A":
            out += f"[{inner}]({strip_archive(href or '')})"
        elif t == "EM":
            out += f"*{inner}*"
        elif t == "STRONG":
            out += f"**{inner}**"
        else:
            out += inner
        out += esc(text[e2 : m[2]])
        out += rec(m[2], e, [x for x in cands if x[1] >= m[2] and x[2] <= e])
        return out

    return rec(0, len(text), mks)


def iframe_block(data: dict, item: dict) -> str:
    fr = resolve(data, item.get("iframe"))
    mr = resolve(data, fr.get("mediaResource"))
    src = strip_archive(mr.get("iframeSrc", ""))
    title = mr.get("title", "video")
    # embedly widget: the actual target is in the src query parameter
    params = urllib.parse.parse_qs(urllib.parse.urlparse(src).query)
    target = urllib.parse.unquote(params.get("src", [src])[0])
    if "youtube.com" in target:
        m = re.search(r"youtube\.com/embed/([A-Za-z0-9_-]{11})", target)
        if m:
            return '{{< youtube id="%s" >}}' % m.group(1)
    if "url" in params:  # tweet embeds
        return f"[{title}]({params['url'][0]})"
    sys.exit(f"error: unhandled iframe: {src}")


def image_id(data: dict, item: dict) -> str:
    meta = resolve(data, item.get("metadata"))
    return meta["id"]


def download(url: str, dest: Path):
    if dest.exists():
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as resp, open(dest, "wb") as f:
        f.write(resp.read())
    return True


def main():
    downloads = {}  # medium image id -> (url, dest_path)
    bodies = {}
    for post in POSTS:
        data = load_apollo(post["html"])
        items = get_items(data)
        title = items[0]["text"]
        subtitle = items[1]["text"]
        assert items[0]["type"] == "H3" and items[1]["type"] == "H4", (
            title,
            items[1]["type"],
        )

        blocks = []
        for item in items[2:]:
            t = item["type"]
            if t == "P":
                blocks.append(render_item_markups(data, item))
            elif t == "H4":
                blocks.append("### " + render_item_markups(data, item))
            elif t == "PQ":
                blocks.append("> " + render_item_markups(data, item))
            elif t == "ULI":
                blocks.append("- " + render_item_markups(data, item))
            elif t == "IMG":
                mid = image_id(data, item)
                ext = Path(mid).suffix
                # deterministic UUID from the Medium image id
                local = "/images/%s%s" % (uuid.uuid5(uuid.NAMESPACE_URL, mid), ext)
                url = "https://miro.medium.com/v2/%s" % mid
                downloads[mid] = (url, STATIC_IMAGES / Path(local).name)
                caption = item["text"].strip()
                blocks.append(f"![{caption}]({local})")
            elif t == "IFRAME":
                blocks.append(iframe_block(data, item))
            else:
                sys.exit(f"error: unhandled item type {t}: {item['text'][:80]}")

        # merge consecutive list items (no blank line between)
        merged = []
        for b in blocks:
            if b.startswith("- ") and merged and merged[-1].startswith("- "):
                merged[-1] = merged[-1] + "\n" + b
            else:
                merged.append(b)

        bodies[post["slug"]] = {
            "title": title,
            "description": subtitle,
            "date": post["date"],
            "body": "\n\n".join(merged),
        }

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    for post in POSTS:
        b = bodies[post["slug"]]
        out = CONTENT_DIR / (post["slug"] + ".md")
        fm = [
            "---",
            'title: "%s"' % b["title"].replace('"', '\\"'),
            "date: %s" % b["date"],
            "series: behind-the-game",
            'description: "%s"' % b["description"].replace('"', '\\"'),
            "---",
        ]
        out.write_text("\n".join(fm) + "\n\n" + b["body"].rstrip() + "\n")
        print(f"wrote {out.relative_to(HUGO_ROOT)}")

    print(f"\nmedia: {len(downloads)} images")
    for mid, (url, dest) in sorted(downloads.items()):
        if download(url, dest):
            print(f"  downloaded {mid} -> {dest.relative_to(HUGO_ROOT)}")
        else:
            print(f"  exists       {mid} -> {dest.relative_to(HUGO_ROOT)}")


if __name__ == "__main__":
    main()
