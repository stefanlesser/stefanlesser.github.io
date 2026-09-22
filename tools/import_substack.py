#!/usr/bin/env python3
"""
Import published Substack posts into this Hugo site.

Reads the Substack export (posts.csv + markdown/*.md), generates one
Hugo content file per published newsletter post in content/post/,
backdated to the original publish date from posts.csv, and downloads
linked media (Substack CDN images, one audio file) into static/.

Transformations applied to every post body:
  - Standalone YouTube video links ("> [▶ Video](...)" blockquotes,
    optionally with a ?t= timecode) are converted to the built-in
    Hugo youtube shortcode, which renders the official YouTube embed.
  - Images hosted on Substack's CDN (substack-post-media.s3.amazonaws.com
    and bucketeer-*.s3.amazonaws.com) are downloaded to static/images/
    and rewritten to local /images/<uuid>.<ext> URLs.
  - Internal Substack links are rewritten to this site:
      /p/<slug>           -> the post's new permalink
      /i/<post_id>/<anch> -> the post's new permalink + #<anchor>
      /t/<series>         -> /series/<series>/
  - One-off fixes for individual posts are in SPECIAL_CASES below.

Usage:
    python3 tools/import_substack.py [--substack-dir PATH]

Idempotent: safe to re-run. Content files are regenerated from the
export on every run; media files are only downloaded if missing.
Re-running after manual edits to content files will overwrite them.
"""

import argparse
import csv
import json
import re
import subprocess
import sys
import unicodedata
import urllib.request
from collections import defaultdict
from pathlib import Path

HUGO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SUBSTACK_DIR = HUGO_ROOT.parent / "Substack Posts"

CONTENT_DIR = HUGO_ROOT / "content" / "post"
STATIC_IMAGES = HUGO_ROOT / "static" / "images"
STATIC_AUDIO = HUGO_ROOT / "static" / "audio"

# Markdown images hosted on Substack's CDN. The UUID identifies the
# original image; the optional _WxH suffix is a CDN resize variant.
IMG_RE = re.compile(
    r"!\[(?P<alt>[^\]]*)\]"
    r"\(https://(?P<host>[a-z0-9.-]+\.s3\.amazonaws\.com)/public/images/"
    r"(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})"
    r"(?:_(?P<size>\d+x\d+))?(?P<ext>\.[A-Za-z0-9]+)?\)"
)

# Standalone YouTube video links as exported by Substack, e.g.:
#   > [▶ Video](https://www.youtube.com/watch?v=Wex12GhUFqE&t=1813)
#   > [▶ Video](https://youtu.be/IZyWuD9UqI4?t=1674)
YT_RE = re.compile(
    r"^> \[▶ Video\]\(https://(?:www\.youtube\.com/watch\?v=|youtu\.be/)"
    r"(?P<id>[a-zA-Z0-9_-]+)(?:[?&]t=(?P<t>\d+))?\)\s*$"
)

# Internal Substack links, e.g.:
#   https://stefanlesser.substack.com/p/on-simplicity
#   https://stefanlesser.substack.com/i/99841600/living-things
#   https://stefanlesser.substack.com/t/mirror-of-the-self
# The optional query string on /p/ links (Substack share tracking) is dropped.
P_RE = re.compile(r"https://stefanlesser\.substack\.com/p/([a-z0-9%-]+)(\?[^)\s]*)?")
I_RE = re.compile(r"https://stefanlesser\.substack\.com/i/(\d+)/([a-z0-9-]+)")
T_RE = re.compile(r"https://stefanlesser\.substack\.com/t/([a-z0-9-]+)")
# The Substack archive page is the home page on this site.
ARCHIVE_RE = re.compile(r"https://stefanlesser\.substack\.com/archive")

# One-off fixes for individual posts (post_id numeric prefix -> list of
# (pattern, replacement) regex substitutions applied to the body).
SPECIAL_CASES = {
    # "Upcoming paper and presentation on simplicity":
    #  - The NotebookLM audio embed was lost in the Substack export;
    #    re-embed it from the locally downloaded file.
    #  - Replace the Substack-hosted paper PDF with the official ACM link.
    "149809538": [
        (
            re.compile(r"^> 🎧 Audio \(7:35\)[ \t]*$", re.MULTILINE),
            '<audio controls src="/audio/simplicity-paper-podcast.mp3"></audio>',
        ),
        (
            re.compile(
                r"https://stefanlesser\.substack\.com/api/v1/file/"
                r"7433b46e-ae50-44cc-baa3-12c37abc54bf\.pdf"
            ),
            "https://dl.acm.org/doi/epdf/10.1145/3689492.3689811",
        ),
    ],
}

AUDIO_URL = (
    "https://stefanlesser.substack.com/api/v1/audio/upload/"
    "aec65f9c-5271-4815-bd1f-1cb5f1c6ff84/src"
)
AUDIO_DEST = STATIC_AUDIO / "simplicity-paper-podcast.mp3"

# Images whose original CDN URL no longer works (403); download them
# through Substack's image proxy instead. Maps uuid -> (url, local_ext).
MEDIA_OVERRIDES = {
    # The bucketeer CDN URL from the export is dead; the proxy serves
    # this image as JPEG.
    "982d6768-6ef4-4321-828c-99dd1e8cc7de": (
        "https://substackcdn.com/image/fetch/$s_!M-rn!,w_1456,c_limit,f_auto,"
        "q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-"
        "baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F"
        "982d6768-6ef4-4321-828c-99dd1e8cc7de_1180x258.png",
        ".jpeg",
    ),
}

# Series membership: post_id numeric prefix -> series slug.
# Mirror of the Self: 27 episodes (01-27) + 2 recaps.
# On simplicity: 8 episodes + 4 "Discussing" companion posts.
# Voices on software design: 6 posts.
SERIES = {
    "75775416": "mirror-of-the-self",
    "77032670": "mirror-of-the-self",
    "78070036": "mirror-of-the-self",
    "78389608": "mirror-of-the-self",
    "79817570": "mirror-of-the-self",
    "79135211": "mirror-of-the-self",
    "83322605": "mirror-of-the-self",
    "84505611": "mirror-of-the-self",
    "85697655": "mirror-of-the-self",
    "86182006": "mirror-of-the-self",
    "85898558": "mirror-of-the-self",
    "90205720": "mirror-of-the-self",
    "90234800": "mirror-of-the-self",
    "95289808": "mirror-of-the-self",
    "96060967": "mirror-of-the-self",
    "99841600": "mirror-of-the-self",
    "100042951": "mirror-of-the-self",
    "100702362": "mirror-of-the-self",
    "104281927": "mirror-of-the-self",
    "104658378": "mirror-of-the-self",
    "106099380": "mirror-of-the-self",
    "105245312": "mirror-of-the-self",
    "110448067": "mirror-of-the-self",
    "111428398": "mirror-of-the-self",
    "111216274": "mirror-of-the-self",
    "107017363": "mirror-of-the-self",
    "108842115": "mirror-of-the-self",
    "90245561": "mirror-of-the-self",
    "117872068": "mirror-of-the-self",
    "138316395": "on-simplicity",
    "138755858": "on-simplicity",
    "139463466": "on-simplicity",
    "140288586": "on-simplicity",
    "140842608": "on-simplicity",
    "141315282": "on-simplicity",
    "141695104": "on-simplicity",
    "142212611": "on-simplicity",
    "142429579": "on-simplicity",
    "142827190": "on-simplicity",
    "143103420": "on-simplicity",
    "144126598": "on-simplicity",
    "143514962": "voices-on-software-design",
    "143515851": "voices-on-software-design",
    "143516408": "voices-on-software-design",
    "145103773": "voices-on-software-design",
    "145641560": "voices-on-software-design",
    "146995170": "voices-on-software-design",
}


def download(url, dest: Path):
    """Download url to dest, skipping if dest already exists."""
    if dest.exists():
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"  downloading {url}")
    print(f"            -> {dest.relative_to(HUGO_ROOT)}")
    # Substack's CDN blocks the default Python user agent.
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp, open(dest, "wb") as f:
        f.write(resp.read())
    return True


def convert_tif_to_png(tif: Path) -> Path:
    """Convert a TIFF to PNG using macOS sips; returns the PNG path."""
    png = tif.with_suffix(".png")
    if not png.exists():
        subprocess.run(
            ["sips", "-s", "format", "png", str(tif), "--out", str(png)],
            check=True,
        )
    if tif.exists():
        tif.unlink()
    return png


def hugo_url_slug(title: str) -> str:
    """Reimplement Hugo's URL slugger (verified against the built sitemap
    for all imported posts): x/text latin transliteration, lowercase,
    spaces to dashes, keep [a-z0-9.-#], collapse dashes, '#' -> %23."""
    t = title.replace("\u2026", "")  # ellipsis: x/text drops it, NFKD would not
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower().replace(" ", "-")
    t = re.sub(r"[^a-z0-9.\-#]", "", t)
    t = re.sub(r"-+", "-", t).strip("-")
    return t.replace("#", "%23")


def _transliterate(t: str) -> str:
    t = t.replace("\u2026", "")
    t = unicodedata.normalize("NFKD", t)
    return "".join(c for c in t if not unicodedata.combining(c))


def heading_id(text: str) -> str:
    """Reimplement the heading ID goldmark/Hugo generates (verified against
    the built HTML for all headings): lowercase, spaces to dashes, keep
    [a-z0-9-], no dash collapsing."""
    t = _transliterate(text).lower().replace(" ", "-")
    return re.sub(r"[^a-z0-9\-]", "", t)


def heading_ids(body: str) -> list:
    """Compute the heading IDs of a markdown body, in document order,
    including blockquoted headings; duplicates get -1, -2, ... suffixes."""
    ids = []
    seen = defaultdict(int)
    for line in body.split("\n"):
        m = re.match(r"^(?:>\s*)*#{1,6}\s+(.*)$", line)
        if not m:
            continue
        text = m.group(1).strip()
        text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links
        text = re.sub(r"[*_`]+", "", text)  # emphasis/code markers
        base = heading_id(text)
        n = seen[base]
        seen[base] += 1
        ids.append(base if n == 0 else f"{base}-{n}")
    return ids


def transform_body(body: str, post_id: str, downloads: dict):
    """Apply all body transformations; returns (new_body, yt_count, img_count)."""
    yt_count = 0

    def yt_sub(m):
        nonlocal yt_count
        yt_count += 1
        sc = '{{< youtube id="%s"' % m.group("id")
        if m.group("t"):
            sc += ' start=%s' % m.group("t")
        return sc + " >}}"

    lines = body.split("\n")
    lines = [YT_RE.sub(yt_sub, line) if "▶" in line else line for line in lines]
    body = "\n".join(lines)

    img_count = 0

    def img_sub(m):
        nonlocal img_count
        img_count += 1
        host = m.group("host")
        uuid = m.group("uuid")
        ext = (m.group("ext") or ".png").lower()
        suffix = ("_" + m.group("size")) if m.group("size") else ""
        url = "https://%s/public/images/%s%s%s" % (host, uuid, suffix, ext)
        if uuid in MEDIA_OVERRIDES:
            url, ext = MEDIA_OVERRIDES[uuid]
        if ext == ".tif":
            # Browsers cannot render TIFF; the import converts it to PNG.
            ext = ".png"
        local = "/images/%s%s" % (uuid, ext)
        downloads.setdefault(uuid, (url, ext))
        return "![%s](%s)" % (m.group("alt"), local)

    body = IMG_RE.sub(img_sub, body)

    for pattern, replacement in SPECIAL_CASES.get(post_id, []):
        body = pattern.sub(replacement, body)

    return body, yt_count, img_count


def rewrite_links(body: str, permalinks: dict, slug_to_id: dict,
                  id_to_headings: dict, adjustments: list):
    """Rewrite internal Substack links to this site. Returns
    (new_body, p_count, i_count, t_count)."""
    p_count = i_count = t_count = 0

    def p_sub(m):
        nonlocal p_count
        p_count += 1
        slug = m.group(1)
        if slug not in slug_to_id:
            raise ValueError(f"unresolved /p/ link: {slug}")
        return permalinks[slug_to_id[slug]]

    def i_sub(m):
        nonlocal i_count
        i_count += 1
        post_id, anchor = m.group(1), m.group(2)
        if post_id not in permalinks:
            raise ValueError(f"unresolved /i/ link target: {post_id}")
        ids = id_to_headings[post_id]
        if anchor in ids:
            resolved = anchor
        else:
            # Substack's slugger collapses consecutive dashes (and once
            # dropped a leading number); find the matching Hugo heading.
            candidates = [i for i in ids
                          if i.replace("--", "-") == anchor
                          or i.endswith("-" + anchor)]
            if len(candidates) != 1:
                raise ValueError(
                    f"ambiguous/unresolved anchor {anchor!r} in {post_id}: "
                    f"{candidates}")
            resolved = candidates[0]
            adjustments.append((post_id, anchor, resolved))
        return permalinks[post_id] + "#" + resolved

    def t_sub(m):
        nonlocal t_count
        t_count += 1
        return "/series/%s/" % m.group(1)

    body = P_RE.sub(p_sub, body)
    body = I_RE.sub(i_sub, body)
    body = T_RE.sub(t_sub, body)
    body = ARCHIVE_RE.sub("/", body)
    return body, p_count, i_count, t_count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--substack-dir",
        type=Path,
        default=DEFAULT_SUBSTACK_DIR,
        help="path to the Substack export folder (default: %(default)s)",
    )
    args = parser.parse_args()

    substack_dir = args.substack_dir
    csv_path = substack_dir / "posts.csv"
    markdown_dir = substack_dir / "markdown"
    if not csv_path.exists():
        sys.exit(f"error: {csv_path} not found")

    with open(csv_path, newline="") as f:
        rows = list(csv.DictReader(f))

    published = [
        r
        for r in rows
        if r["is_published"] == "true" and r["type"] == "newsletter"
    ]
    print(f"importing {len(published)} published posts from {substack_dir}")

    # Pass 1: transform all bodies, collect per-post info.
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    downloads = {}
    posts = {}  # post_id -> dict
    for row in published:
        post_id = row["post_id"].split(".")[0]
        slug = row["post_id"].split(".", 1)[1]
        md_path = markdown_dir / (row["post_id"] + ".md")
        text = md_path.read_text()

        # Split off the H1 title and (if present) the subtitle, which is
        # the first paragraph and always equals the CSV subtitle field.
        h1, _, rest = text.partition("\n")
        assert h1.startswith("# "), f"{slug}: unexpected first line {h1!r}"
        title = h1[2:].strip()
        assert title == row["title"].strip(), f"{slug}: title mismatch"
        rest = rest.lstrip("\n")
        first_para, _, body = rest.partition("\n\n")
        if row["subtitle"].strip() and first_para.strip() == row["subtitle"].strip():
            body = body.lstrip("\n")
        else:
            # No subtitle (or unexpected first paragraph): keep it in body.
            body = (first_para + "\n\n" + body).lstrip("\n") if first_para.strip() else body

        # Backdate to the original publish date (UTC, from posts.csv).
        date = row["post_date"][:19] + "Z"
        y, m, d = row["post_date"][:10].split("-")

        body, yt_count, img_count = transform_body(body, post_id, downloads)

        posts[post_id] = {
            "slug": slug,
            "title": title,
            "date": date,
            "permalink": f"/{y}/{m}/{d}/{hugo_url_slug(title)}/",
            "body": body,
            "headings": heading_ids(body),
            "yt": yt_count,
            "img": img_count,
        }

    slug_to_id = {p["slug"]: pid for pid, p in posts.items()}

    # Pass 2: rewrite internal Substack links.
    total_p = total_i = total_t = 0
    adjustments = []
    for pid, p in posts.items():
        body, pc, ic, tc = rewrite_links(
            p["body"], {q: r["permalink"] for q, r in posts.items()},
            slug_to_id, {q: r["headings"] for q, r in posts.items()},
            adjustments)
        p["body"] = body
        total_p += pc
        total_i += ic
        total_t += tc

    # Write content files.
    written = 0
    for pid, p in posts.items():
        out = CONTENT_DIR / (p["slug"] + ".md")
        fm = [
            "---",
            "title: %s" % json.dumps(p["title"], ensure_ascii=False),
            "date: %s" % p["date"],
        ]
        if pid in SERIES:
            fm.append("series: %s" % SERIES[pid])
        fm.append("---")
        out.write_text("\n".join(fm) + "\n\n" + p["body"].rstrip() + "\n")
        written += 1
        if p["yt"] or p["img"]:
            print(f"  {p['slug']}: {p['yt']} youtube, {p['img']} images")

    # Download media.
    print(f"\nmedia: {len(downloads)} images")
    for uuid, (url, local_ext) in sorted(downloads.items()):
        src_ext = Path(url).suffix.lower()
        if src_ext == ".tif":
            # Browsers cannot render TIFF; download it (if needed), then
            # convert to PNG. convert_tif_to_png also removes any
            # leftover source file from an interrupted earlier run.
            dest = STATIC_IMAGES / (uuid + ".tif")
            if not dest.with_suffix(".png").exists():
                download(url, dest)
            convert_tif_to_png(dest)
        else:
            dest = STATIC_IMAGES / (uuid + local_ext)
            download(url, dest)

    if download(AUDIO_URL, AUDIO_DEST):
        print(f"  audio: {AUDIO_DEST.relative_to(HUGO_ROOT)} ({AUDIO_DEST.stat().st_size} bytes)")

    print(f"\ndone: {written} posts written to content/post/, "
          f"{sum(p['yt'] for p in posts.values())} youtube embeds, "
          f"{sum(p['img'] for p in posts.values())} local images")
    print(f"links rewritten: {total_p} post, {total_i} in-post anchor, "
          f"{total_t} series")
    for post_id, anchor, resolved in adjustments:
        print(f"  anchor adjusted: {post_id} #{anchor} -> #{resolved}")


if __name__ == "__main__":
    main()
