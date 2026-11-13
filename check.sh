#!/bin/sh
# Pre-push check for the Hugo site.
#
# Usage: ./check.sh   (run before `git push`)
#
# What it does:
#   1. Keeps .hugo-version in sync with the local Hugo install.
#      CI installs the Hugo version from this file, so after a
#      `brew upgrade` this keeps the two in sync with zero manual steps.
#   2. Builds the site with --minify.
#   3. Verifies the generated public/ output actually contains the tokens
#      the live pages depend on. A build can "succeed" while the wrong
#      source files are used (the live CSS/JS live in assets/ - Hugo's
#      resource pipeline reads assets/, never a theme's static/); the
#      token check is what proves the build used the right ones.
set -eu
cd "$(dirname "$0")"

hugo_version=$(hugo version | sed -n 's/^hugo v\([0-9.]*\).*/\1/p')
if [ -f .hugo-version ] && [ "$(cat .hugo-version)" != "$hugo_version" ]; then
  printf '%s\n' "$hugo_version" > .hugo-version
  echo "updated .hugo-version to $hugo_version"
elif [ ! -f .hugo-version ]; then
  printf '%s\n' "$hugo_version" > .hugo-version
fi

hugo --minify

css=$(ls public/css/main.min.*.css) || {
  echo "FAIL: no fingerprinted CSS in public/css/" >&2
  exit 1
}
grep -q 'data-theme' "$css" || {
  echo "FAIL: built CSS lacks data-theme tokens - is the live CSS (assets/css/main.css) shadowed?" >&2
  exit 1
}
grep -q 'theme-toggle' public/index.html || {
  echo "FAIL: index.html lacks the theme-toggle JS reference" >&2
  exit 1
}
echo "check OK: build output contains expected tokens (hugo $hugo_version)"
