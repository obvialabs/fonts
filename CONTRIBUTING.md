# Contributing to Obvia Fonts

Thank you for contributing to Obvia Fonts. This repository contains the canonical editable sources, production build configuration, generated font binaries, QA reports, specimen assets, and the `@obvia/fonts` npm package for Obvia Sans, Obvia Mono, and Obvia Pixel.

This guide is intentionally end to end. It covers setup on Windows, Linux, and macOS; safe source editing; deterministic builds; QA; npm packaging; release preparation; Git conventions; and the checks expected before a pull request is merged.

## Repository map

The most important paths are:

- `sources/Obvia.glyphspackage` — Obvia Sans upright masters.
- `sources/Obvia-Italic.glyphspackage` — Obvia Sans italic masters.
- `sources/ObviaMono.glyphspackage` — Obvia Mono upright masters.
- `sources/ObviaMono-Italic.glyphspackage` — Obvia Mono italic masters.
- `sources/ObviaPixel.glyphspackage` — Obvia Pixel source.
- `sources/config-*.yaml` — production `gftools builder` configuration.
- `fonts/` — generated distributable fonts. Never edit these by hand.
- `output/` — generated release, npm, proof, and QA artifacts.
- `scripts/` — deterministic build, validation, packaging, and release helpers.
- `packages/fonts/` — source for the `@obvia/fonts` npm wrapper.
- `Makefile` — short local entry points for the build pipeline.
- `.github/workflows/ci.yaml` — canonical CI build/QA/package pipeline.
- `.github/workflows/release.yaml` — controlled npm staged-publishing workflow.
- `docs/RELEASING.md` — maintainer release runbook.

The canonical design sources are the packages under `sources/*.glyphspackage`. Generated TTF, OTF, WOFF2, variable-font, release ZIP, npm tarball, proof, and report files are outputs, not editing sources.

## Build principles

The repository follows a few rules that are more important than any individual command:

1. **Python is pinned to 3.11.** Do not rely on whatever `python3` happens to point to on the host.
2. **Python dependencies are installed and executed through `uv`.** Do not use system `pip`, `sudo pip`, or `--break-system-packages`.
3. **A failed font build must not destroy the last good generated tree.** The build is completed in a staging directory before generated outputs are replaced.
4. **npm packaging is separate from font building.** The published tarball is assembled from an allow-listed staging directory.
5. **npm lifecycle scripts are not used to prepare a release tarball.** The release artifact is already built and inspected before publishing.
6. **Local machines do not publish directly to npm.** CI stages the exact tested tarball with npm trusted publishing/OIDC; a maintainer approves it separately with 2FA.
7. **Generated outputs are reviewed, but canonical fixes belong in source files.**
8. **Do not silence QA heuristics by blindly modifying outlines.** Visual and interpolation review comes first.

## Required toolchain

For normal font development:

- Git.
- `uv`.
- Python 3.11 managed by `uv`.
- GNU Make on Linux/macOS/WSL2 for the short `make ...` commands.
- `ttfautohint`.
- Cairo development/runtime libraries.
- Fontspector for full QA.

For npm package work:

- Node.js version from `.nvmrc`.
- Corepack.
- pnpm version declared by `packages/fonts/package.json`.
- npm; release CI installs the staged-publishing-capable npm version explicitly.

Run repository commands from the repository root unless stated otherwise.

# Getting the repository

```bash
git clone https://github.com/obvialabs/fonts.git
cd fonts
git status --short
```

Create one focused branch for the work you intend to submit:

```bash
git switch -c fix/<short-description>
```

Examples:

```text
fix/mono-codepoint-coverage
fix/ligature-carets
feat/latin-glyph-extension
docs/contribution-guide
```

Keep related work on that branch and split the history into scoped Conventional Commits instead of creating a branch for every small step.

## Line endings

The repository contains large text-based Glyphs Package sources. A Windows checkout can therefore look catastrophically modified when Git only converted LF/CRLF endings.

Before treating thousands of files as changed, inspect the semantic diff:

```bash
git status --short
git diff --ignore-space-at-eol --stat
git diff --ignore-space-at-eol
```

Do not commit repository-wide line-ending churn as part of an unrelated font change.

If the checkout contains no real local work and the only changes are checkout conversion, restore it before starting:

```bash
git reset --hard HEAD
```

Never run that command when you have uncommitted work you need to keep.

# Platform setup

## Windows

### Recommended production-equivalent setup: WSL2

WSL2 is the recommended Windows build environment because the CI runner is Linux and the repository's `Makefile` uses POSIX commands.

From an elevated PowerShell terminal:

```powershell
wsl --install -d Ubuntu
```

After Ubuntu starts, install native prerequisites:

```bash
sudo apt update
sudo apt install -y \
  git make build-essential curl \
  ttfautohint libcairo2-dev python3-cairo-dev pkg-config python3-dev
```

Install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env" 2>/dev/null || true
```

Verify it:

```bash
uv --version
```

Install Rust/Cargo and Fontspector for full QA:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
cargo install fontspector
```

Clone inside the WSL filesystem for better performance than `/mnt/c/...`:

```bash
mkdir -p ~/src
cd ~/src
git clone https://github.com/obvialabs/fonts.git
cd fonts
```

Prepare the Python toolchain:

```bash
make setup
```

Build:

```bash
make build
```

Run release-grade QA and create an npm tarball:

```bash
make package
```

### Native Windows / PowerShell

`uv` itself supports native Windows. Install it in PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then:

```powershell
uv python install 3.11
```

The production Makefile is POSIX-oriented, so WSL2 remains the supported full-build path. If you intentionally run the Python build helpers natively and have the native font dependencies available, use the same pinned environment explicitly rather than system `pip`:

```powershell
uv run --no-project --python 3.11 --with-requirements requirements.txt python scripts/build.py
uv run --no-project --python 3.11 --with-requirements requirements.txt python scripts/check.py
```

For the full QA path, `fontspector` must also be available on `PATH`.

### Editing from Windows

Glyphs is a macOS application. On Windows:

- VS Code is suitable for scripts, docs, configs, metadata, and carefully scoped textual source fixes.
- VS Code + WSL is recommended so Git/build tooling remains inside Linux while the editor UI runs on Windows.
- Do not hand-edit outline coordinates unless you understand the Glyphs Package format, interpolation requirements, and component/anchor semantics.
- Do not round-trip the repository through another font format just to make a visual edit; that can lose Glyphs-specific data.

## Linux

On Debian/Ubuntu:

```bash
sudo apt update
sudo apt install -y \
  git make build-essential curl \
  ttfautohint libcairo2-dev python3-cairo-dev pkg-config python3-dev
```

Install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install Fontspector when you need full QA:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
cargo install fontspector
```

Clone and prepare:

```bash
git clone https://github.com/obvialabs/fonts.git
cd fonts
make setup
```

Then use the normal commands:

```bash
make build
make check
make package
make proof
```

## macOS

Install Xcode Command Line Tools:

```bash
xcode-select --install
```

With Homebrew:

```bash
brew install git make pkg-config cairo ttfautohint rust
```

Install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install Fontspector:

```bash
cargo install fontspector
```

Clone and prepare:

```bash
git clone https://github.com/obvialabs/fonts.git
cd fonts
make setup
```

Build and validate:

```bash
make build
make check
make package
make proof
```

### Editing with Glyphs on macOS

Glyphs 3 is the preferred visual editor for the canonical `.glyphspackage` sources.

Open the package you actually intend to edit:

```text
sources/Obvia.glyphspackage
sources/Obvia-Italic.glyphspackage
sources/ObviaMono.glyphspackage
sources/ObviaMono-Italic.glyphspackage
sources/ObviaPixel.glyphspackage
```

Save in Glyphs Package format. Do not export fonts from Glyphs and copy them over `fonts/` as a substitute for the repository build. `sources/config-*.yaml` + `gftools builder` are the production build path.

# Everyday commands

## `make setup`

```bash
make setup
```

This asks `uv` to install/use Python 3.11 and verifies that the pinned font tooling from `requirements.txt` can be imported.

There is no repository-managed `venv/` that you need to activate. `uv` creates/reuses its isolated environment and cache automatically.

If your shell currently displays an old `(venv)`, leave it before diagnosing this repository:

```bash
deactivate 2>/dev/null || true
```

Do not use:

```text
sudo pip install ...
pip install --break-system-packages ...
```

## `make build`

```bash
make build
```

The build pipeline:

1. runs each `sources/config-*.yaml` through `gftools builder`;
2. builds into `output/.build-work/` first;
3. refuses to replace the previous good output unless every configured family finishes;
4. publishes the completed generated tree into `fonts/`;
5. prepares npm font assets in `packages/fonts/dist/fonts/`;
6. creates `output/release/obvia-font/`;
7. creates the reproducible `output/release/obvia-font.zip`;
8. writes per-file SHA-256 checksums into the release tree;
9. writes `output/build-manifest.json` with the build-input digest and artifact hashes.

A failed family build should therefore leave the last successful `fonts/` tree intact instead of replacing it with partial output.

## `make check`

```bash
make check
```

This rebuilds and performs fast deterministic checks including:

- OpenType parsing with `fontTools`;
- required table presence;
- expected Unicode coverage introduced by repository fixes;
- variable-font `fvar` presence;
- npm font-layout checks;
- build-manifest/input-digest validation;
- release ZIP integrity against the manifest.

Use this during normal development.

## `make check-full`

```bash
make check-full
```

This performs the same build and deterministic checks plus blocking Fontspector QA. Network-dependent Fontspector checks are skipped so external service outages do not masquerade as font defects.

Reports are written under:

```text
output/fontspector/
output/badges/
```

## `make package`

```bash
make package
```

This is the local **release-candidate gate**. It intentionally performs:

```text
build -> deterministic checks -> blocking Fontspector QA -> npm wrapper build -> npm dry-run -> npm tarball
```

The final package is written under:

```text
output/npm/*.tgz
output/npm/*.tgz.sha256
```

The npm tarball is assembled from a temporary allow-listed staging directory containing only:

```text
package.json
README.md
LICENSE.txt
dist/
```

The package staging process strips development dependencies and lifecycle scripts from the published manifest. Packaging uses `--ignore-scripts`, so creating the release tarball does not execute repository-local npm lifecycle code.

Always inspect the tarball before a release PR is merged.

## `make proof`

```bash
make proof
```

This rebuilds first and generates Diffenator2 proof material under `output/proof/`.

Use proofs for design changes, interpolation review, spacing review, and visual regressions that automated QA cannot judge.

## `make version`

For a release PR:

```bash
make version VERSION=1.4.0
```

This validates SemVer and changes only `packages/fonts/package.json`. Review the diff and update `packages/fonts/changelog.md` for user-visible changes.

Do not run `npm version`, Changesets versioning, or ad-hoc search/replace version bumps for the package.

## `make clean`

```bash
make clean
```

This removes local ephemeral release/package/proof outputs and generated npm font assets. It does **not** delete the `uv` cache or a global Python installation.

It is not a Git reset command.

# Editing font sources

## Choose the correct source

| Family | Canonical source |
| --- | --- |
| Obvia Sans upright | `sources/Obvia.glyphspackage` |
| Obvia Sans italic | `sources/Obvia-Italic.glyphspackage` |
| Obvia Mono upright | `sources/ObviaMono.glyphspackage` |
| Obvia Mono italic | `sources/ObviaMono-Italic.glyphspackage` |
| Obvia Pixel | `sources/ObviaPixel.glyphspackage` |

Do not make an upright fix in an italic source, or a Sans fix in Mono, unless the change is intentionally family-wide.

A Glyphs Package is a directory-backed document. Typical content includes:

- `fontinfo.plist` — masters, axes, instances, custom parameters, metrics, classes, and features;
- `glyphs/*.glyph` — glyph layers, outlines, anchors, components, metrics, Unicode, and export metadata;
- `order.plist` — glyph ordering.

## Adding or changing a glyph

Before adding a glyph:

1. confirm the intended Unicode code point and canonical glyph name;
2. confirm whether the glyph already exists under another name;
3. decide whether upright, italic, Sans, Mono, Pixel, or several families require it;
4. verify whether it should export;
5. identify components and anchors needed in every master;
6. check whether glyph order should change.

After editing:

```bash
make build
make check
```

For a release-quality validation:

```bash
make package
```

Do not consider a glyph complete because one source layer looks correct. Verify generated static and variable binaries.

## Unicode coverage

When changing Unicode coverage:

- use one canonical Unicode assignment unless the project intentionally aliases code points;
- ensure `export` behavior is consistent across related sources;
- compare family/style coverage rather than checking only Regular;
- verify the generated cmap, not just the text source;
- check combining marks and script support where applicable.

## Components

For component glyphs:

- ensure the component exists and exports;
- verify transforms in every master;
- verify interpolation compatibility;
- avoid needless decomposition;
- inspect generated outlines when feature compilation or overlap removal can alter results.

## Anchors and marks

For mark-related changes:

- keep anchor names consistent across masters;
- verify base and mark anchors as a system;
- check uppercase, lowercase, localized, alternate, and composite glyphs that reuse the anchor model;
- test stacked marks and soft-dotted behavior;
- review italic placement independently from upright placement.

## Ligatures and caret positions

Ligatures representing multiple input characters should expose caret positions when text engines need cursor placement inside the ligature.

For a two-character ligature, define `caret_1` in every master/layer at the intended boundary. More complex ligatures may require `caret_2`, `caret_3`, and so on.

Rebuild after changing ligature width, components, or caret anchors.

## Kerning

For kerning changes:

- prefer class kerning for genuinely shared behavior;
- add exceptions only when the form requires one;
- check every master;
- review punctuation and related pairs;
- test the generated font, not only the source-editor preview.

Do not perform a repository-wide kerning normalization inside an unrelated fix.

## OpenType features

When changing feature/class definitions:

- keep upright/italic behavior aligned where expected;
- verify compilation through `make build`;
- test default shaping and explicitly enabled discretionary/stylistic features;
- pay particular attention to `locl`, mark/mkmk positioning, ligatures, stylistic sets, and language-specific forms.

## Metrics

Review:

- advance widths and sidebearings;
- vertical metrics and clipping;
- cap height/x-height relationships;
- monospaced invariants in Obvia Mono;
- symbol/math width consistency where the design expects it;
- family extremes and variable interpolation.

Obvia Mono must remain monospaced in generated binaries.

## Variable fonts

For variable-family changes:

- verify axes and master locations in `fontinfo.plist`;
- check interpolation compatibility;
- inspect intermediate locations, not only named instances;
- compare static and variable naming/coverage/metrics;
- investigate variable-only warnings separately from static warnings.

# Build configuration changes

Production builder configuration is under `sources/config-*.yaml`.

Do not change a builder flag merely to hide a QA warning. A builder setting can change every generated binary in a family.

When changing build configuration:

1. explain why a source-level fix is not appropriate;
2. rebuild every affected family;
3. compare filenames, names, axes, tables, and package layout;
4. include the behavioral impact in the PR description.

# QA and review

## Fontspector

Use:

```bash
make check-full
```

Classify findings before fixing them:

- **build/schema error** — fix before merging;
- **family inconsistency** — normally fix unless intentional and documented;
- **shaping/anchor error** — reproduce with the relevant script/language;
- **naming/metadata error** — verify distribution and OpenType requirements;
- **outline heuristic warning** — inspect visually before modifying contours;
- **network/service failure** — treat as infrastructure, not as a font defect.

## Binary inspection

For ad-hoc inspection without activating a venv:

```bash
uv run --no-project --python 3.11 --with-requirements requirements.txt python - <<'PY'
from fontTools.ttLib import TTFont
font = TTFont("fonts/Obvia/ttf/Obvia-Regular.ttf")
print(font.keys())
print(font["head"].unitsPerEm)
PY
```

For cmap coverage:

```bash
uv run --no-project --python 3.11 --with-requirements requirements.txt python - <<'PY'
from fontTools.ttLib import TTFont
font = TTFont("fonts/Obvia/ttf/Obvia-Regular.ttf")
codepoints = set()
for table in font["cmap"].tables:
    if table.isUnicode():
        codepoints.update(table.cmap)
print(f"Unicode codepoints: {len(codepoints)}")
PY
```

For a family coverage fix, compare every generated style that should share the coverage.

# npm package development

The npm package lives under `packages/fonts`.

Check the pinned Node version:

```bash
cat .nvmrc
```

Enable Corepack:

```bash
corepack enable
```

The package manifest pins pnpm through `packageManager`. If you need to work directly inside the package:

```bash
cd packages/fonts
corepack pnpm install --frozen-lockfile
corepack pnpm run build
cd ../..
```

Do not manually copy or rename font files under `packages/fonts/dist/fonts/`; `make build` owns that generated tree.

Before a package-related PR is considered release-ready, run from the repository root:

```bash
make package
```

# Release model

Contributors do not publish from local machines.

The intended flow is:

```text
feature/fix branch
    -> pull request
    -> CI: make package
    -> merge to main
    -> release version PR when needed
    -> merge version PR
    -> maintainer runs "Stage npm Release" on main
    -> clean GitHub-hosted runner rebuilds everything
    -> full QA
    -> exact npm tarball is staged with OIDC
    -> maintainer reviews staged package
    -> maintainer approves with 2FA
    -> package becomes public
```

There is no long-lived `NPM_TOKEN` in the publishing workflow.

The trusted npm publisher should be limited to `.github/workflows/release.yaml`, the `npm-staging` GitHub Environment, and staged publishing only. Direct `npm publish` is intentionally not part of the workflow.

Maintainers should follow `docs/RELEASING.md`.

# Reviewing your diff

Before committing:

```bash
git status --short
git diff --stat
git diff
```

Check for:

- CRLF/LF churn;
- unrelated generated files;
- accidental Glyphs metadata rewrites;
- unrelated kerning/glyph-order/custom-parameter changes;
- temporary build config files;
- local credentials or signing material;
- proof/report output that is not intended to be versioned.

Review source changes separately when useful:

```bash
git diff -- sources/
```

# Commit conventions

Use scoped Conventional Commits and keep each commit internally coherent:

```text
fix(fonts): restore mono codepoint coverage
fix(shaping): add ligature caret positions
build(fonts): modernize deterministic build pipeline
ci(release): stage verified npm artifacts with oidc
docs(contributing): document release and platform workflow
```

Do not use unscoped messages such as `fix: ...`, `updates`, or `changes`.

If commits are signed, verify them before pushing:

```bash
git log --show-signature -1
```

# Pull request checklist

Before opening a PR, confirm all applicable items:

- [ ] The branch contains only work related to the stated purpose.
- [ ] Canonical design fixes were made under `sources/`, not directly in generated binaries.
- [ ] `make build` succeeds.
- [ ] `make check` succeeds.
- [ ] `make package` succeeds before release-affecting changes are merged.
- [ ] Fontspector failures are fixed or explicitly explained.
- [ ] `make proof` was reviewed for visual/design-affecting changes.
- [ ] Static and variable outputs were checked where applicable.
- [ ] Interpolation was reviewed for master/outline changes.
- [ ] Kerning and anchors were checked for spacing/shaping changes.
- [ ] Obvia Mono remains monospaced when Mono changes.
- [ ] Generated filenames and OpenType naming are intentional.
- [ ] npm tarball contents were inspected for package/release changes.
- [ ] No unrelated line-ending churn exists.
- [ ] No tokens, private keys, local env files, or credentials are included.
- [ ] The PR explains intentionally unresolved QA warnings.
- [ ] Visual changes include proof/screenshot evidence when useful.

# What should not be automated blindly

Treat these as design-review candidates rather than automatic rewrite instructions:

- short segments;
- nearly horizontal/vertical segments;
- collinear vectors;
- alignment misses;
- point simplification;
- extrema insertion;
- global width normalization;
- automatic kerning rewrites;
- automatic anchor relocation across a script.

Prefer a small, explainable source correction over a large rewrite that merely lowers the warning count.

# Troubleshooting

## `skia-python` cannot be installed

If the resolver only offers a newer `skia-python` build and rejects the pinned version, verify that you are not using Python 3.14 or another unsupported interpreter:

```bash
python3 --version
uv python find 3.11
```

Use the repository command instead of manually creating a host venv:

```bash
make setup
make build
```

The repository explicitly requests Python 3.11 through `uv`.

## `externally-managed-environment`

This comes from PEP 668 protection on a system Python. Do not bypass it with `--break-system-packages`.

Do not run system `pip install -r requirements.txt`. Use:

```bash
make setup
```

or the direct `uv run ...` commands documented above.

## `uv: command not found`

Linux/macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Restart/reload the shell if the installer updated `PATH`.

## `fontspector: command not found`

Install Rust/Cargo and:

```bash
cargo install fontspector
fontspector --version
```

Full package validation intentionally fails when Fontspector is missing.

## Cairo installation errors

Ubuntu/WSL:

```bash
sudo apt install libcairo2-dev python3-cairo-dev pkg-config python3-dev
```

macOS:

```bash
brew install cairo pkg-config
```

## Corepack or pnpm is unavailable

Use the Node version in `.nvmrc`, then:

```bash
corepack enable
corepack pnpm --version
```

Do not silently switch package managers and generate `package-lock.json`.

## Build fails halfway through

The build happens under `output/.build-work/` and only replaces final generated trees after every configured source family succeeds.

Fix the failure and rerun:

```bash
make build
```

The previous completed `fonts/` output should remain available after a failed build.

## npm package contains an unexpected file

`make package` performs `npm pack --dry-run --json` against the package staging directory and rejects unexpected top-level content. Fix the staging/package configuration; do not weaken the allow-list simply to make the check pass.

## Thousands of files are modified after checkout

Check line endings:

```bash
git diff --ignore-space-at-eol --stat
```

Do not include repository-wide line-ending churn in your PR.

# Security and licensing

All contributions must remain compatible with the SIL Open Font License in `OFL.txt` and any other project licensing requirements.

Do not copy glyph outlines, kerning data, or design material from fonts with incompatible licenses.

Never commit:

- GPG/private signing keys;
- npm tokens;
- GitHub tokens;
- `.env` secrets;
- registry credentials;
- local certificate/key files.

Publishing credentials belong to the npm/GitHub trusted-publisher configuration, not to the repository.

# Need help?

For a font-specific issue or PR, include:

- family and style;
- glyph name and Unicode code point where relevant;
- static/variable/both;
- OS/application where the problem reproduces;
- shaping language/script and feature settings;
- screenshot or minimal text sample for rendering defects;
- Fontspector check identifier when applicable.

For release/pipeline problems, include the failing command and the relevant CI step, but never paste secrets or authentication tokens.
