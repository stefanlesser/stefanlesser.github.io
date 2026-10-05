# Deployment

The site is built by [GitHub Actions](https://github.com/stefanlesser/stefanlesser.github.io/actions)
and served by GitHub Pages. The Hugo source in this directory is the single
source of truth; the generated `public/` directory is never committed.

## How it works

1. Pushes to `master` trigger `.github/workflows/deploy.yml`.
2. The workflow installs the pinned Hugo version (see `HUGO_VERSION` in the
   workflow — keep it in sync with the local development version), checks out
   the repo including the Lithium theme submodule, and runs `hugo --minify`.
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

## One-time setup already performed / required

- [x] Workflow committed at `.github/workflows/deploy.yml`
- [x] Hugo source pushed to `stefanlesser.github.io` (replacing the old
      generated-site commits on `master`)
- [ ] GitHub repo Settings → Pages → Source switched to **GitHub Actions**
      (do this *after* the source push; the first successful run then
      re-deploys the site and the old generated content is retired)

## Notes

- The theme is a git submodule (`themes/hugo-lithium-theme`); the workflow
  checks it out with `submodules: recursive`.
- The old local clone of the generated site (`stefanlesser.github.io/` next
  to this directory) is now obsolete; previews happen locally with
  `hugo server` in this directory.
