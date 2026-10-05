# Deployment

The site is built by [GitHub Actions](https://github.com/stefanlesser/stefanlesser.github.io/actions)
and served by GitHub Pages. The Hugo source in this directory is the single
source of truth; the generated `public/` directory is never committed.

## How it works

1. Pushes to `master` trigger `.github/workflows/deploy.yml`.
2. The workflow installs the pinned Hugo version (see `HUGO_VERSION` in the
   workflow — keep it in sync with the local development version) and runs
   `hugo --minify`.
3. The `public/` output is uploaded as a Pages artifact and deployed by
   `actions/deploy-pages` to the `stefanlesser.github.io` repository, whose
   Pages source is set to **GitHub Actions** (Settings → Pages → Build and
   deployment → Source).
4. The custom domain comes from `static/CNAME` (`stefan-lesser.com`), which
   Hugo copies into the build output.

## Day-to-day publishing

```sh
git add -A && git commit -m "..."
git push
```

Watch the run in the repo's Actions tab. No further steps are needed.

## Notes

- The Lithium theme is vendored at `themes/hugo-lithium-theme` (a copy of
  https://github.com/jrutheiser/hugo-lithium-theme with local
  customizations committed on top). Upstream updates, if ever wanted, must
  be applied manually.
- Local previews happen with `hugo server` in this directory.
