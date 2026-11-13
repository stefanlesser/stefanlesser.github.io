# Deployment

The site is built by [GitHub Actions](https://github.com/stefanlesser/stefanlesser.github.io/actions)
and served by GitHub Pages. The Hugo source in this directory is the single
source of truth; the generated `public/` directory is never committed.

## How it works

1. Pushes to `master` trigger `.github/workflows/deploy.yml`.
2. The workflow installs the Hugo version from `.hugo-version` and runs
   `hugo --minify`. Run `./check.sh` locally before pushing: it builds,
   verifies the generated output contains the expected tokens, and keeps
   `.hugo-version` in sync with your local Hugo install (so a `brew upgrade`
   is picked up automatically).
3. The `public/` output is uploaded as a Pages artifact and deployed by
   `actions/deploy-pages` to the `stefanlesser.github.io` repository, whose
   Pages source is set to **GitHub Actions** (Settings → Pages → Build and
   deployment → Source).
4. The custom domain comes from `static/CNAME` (`stefan-lesser.com`), which
   Hugo copies into the build output.

## Day-to-day publishing

```sh
./check.sh
git add -A && git commit -m "..."
git push
```

Watch the run in the repo's Actions tab. No further steps are needed.

## Notes

- The site has no theme: all layouts live in `layouts/` (the Lithium theme
  was vendored earlier and has been fully absorbed into the site's own
  layouts). Live CSS/JS live in `assets/` — Hugo's resource pipeline
  (`resources.Get`) reads `assets/`, not a `static/` directory.
- Local previews happen with `hugo server` in this directory.
