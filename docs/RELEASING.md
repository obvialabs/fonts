# Releasing Obvia Fonts

`@obvia/fonts` uses a review-first, staged publishing model. A local developer machine never needs npm publish credentials.

The release flow is:

```text
version change through PR
    -> CI builds + runs full QA + packs tarball
    -> merge to main
    -> maintainer dispatches Stage npm Release
    -> clean GitHub-hosted runner rebuilds exact commit
    -> exact tested .tgz is submitted with npm trusted publishing (OIDC)
    -> package remains private in npm staging
    -> maintainer reviews it
    -> maintainer approves with 2FA
    -> version becomes public
```

## One-time npm configuration

Configure a trusted publisher for `@obvia/fonts` on npmjs.com with:

- provider: GitHub Actions;
- organization/user: `obvialabs`;
- repository: `fonts`;
- workflow filename: `release.yaml`;
- environment: `npm-staging`;
- allowed action: staged publishing only.

The workflow uses `id-token: write` and does not use `NPM_TOKEN` for publishing.

After trusted publishing has been tested successfully, configure the package for the strongest practical publishing policy:

- require 2FA;
- disallow traditional publishing tokens;
- keep the trusted publisher stage-only rather than allowing direct `npm publish`.

Official references:

- <https://docs.npmjs.com/trusted-publishers/>
- <https://docs.npmjs.com/staged-publishing/>
- <https://docs.npmjs.com/generating-provenance-statements/>

The workflow currently uses Node `24.12.0` from `.nvmrc` and installs npm `11.20.0` before staging. This is intentionally newer than npm's minimum staged-publishing requirement.

## One-time GitHub configuration

Create a GitHub Environment named:

```text
npm-staging
```

For additional control, require maintainer approval on that environment. The npm trusted-publisher configuration must use the same environment name if you configure an environment restriction there.

Do not add an `NPM_TOKEN` publishing secret to the workflow.

## Prepare a version PR

Start from current `main` and create the normal release-preparation branch used by your project workflow:

```bash
git switch main
git pull --ff-only
git switch -c release/fonts-1.4.0
```

Change the package version with the repository helper:

```bash
make version VERSION=1.4.0
```

Update:

```text
packages/fonts/changelog.md
```

when there are user-visible changes.

Do not use Changesets, `npm version`, or direct JSON search/replace for the release version.

## Build the exact release candidate locally

Run:

```bash
make package
```

`make package` is intentionally the full release gate. It performs:

1. deterministic font build;
2. build-manifest/integrity checks;
3. OpenType checks;
4. blocking Fontspector QA;
5. npm wrapper compilation;
6. npm dry-run inspection;
7. creation of the release npm tarball.

Review these artifacts:

```text
output/build-manifest.json
output/release/obvia-font.zip
output/release/obvia-font/SHA256SUMS.txt
output/npm/*.tgz
output/npm/*.tgz.sha256
```

Inspect the npm tarball contents before merging the version PR.

Commit the version/changelog change with a scoped Conventional Commit and merge it through review. Do not publish from the branch.

## Stage the package from GitHub Actions

After the version PR reaches `main`:

1. open **GitHub → Actions → Stage npm Release**;
2. choose **Run workflow** on `main`;
3. enter the exact version already present in `packages/fonts/package.json`;
4. approve the `npm-staging` GitHub Environment if environment protection is enabled.

The workflow validates:

- it was dispatched from `main`;
- the requested version exactly matches `package.json`;
- package name is `@obvia/fonts`;
- repository metadata matches `obvialabs/fonts`;
- public access is explicitly configured;
- the checkout is clean before build.

It then runs the same full `make package` gate on a clean GitHub-hosted runner.

The workflow stages **the exact `.tgz` produced by that successful run**:

```bash
npm stage publish <tarball> --access public
```

The workflow does not run direct `npm publish`.

## Review the staged npm package

A staged package is not yet public.

Use npmjs.com's staged packages UI, or an interactively authenticated npm CLI, to inspect it.

Useful commands include:

```bash
npm stage list @obvia/fonts
npm stage view <stage-id>
npm stage download <stage-id>
```

Compare the downloaded tarball with the GitHub Actions artifact and its SHA-256 file when performing a high-assurance release review.

## Approve

When the staged package is correct:

```bash
npm stage approve <stage-id>
```

Approval requires proof of presence/2FA. OIDC automation intentionally cannot perform this final approval step.

If the staged artifact is wrong:

```bash
npm stage reject <stage-id>
```

Fix the repository through a new PR and prepare an appropriate new package version. Do not bypass the staged workflow with a local direct publish.

## GitHub release

After npm approval, create the matching GitHub release/tag and attach the `output/release/obvia-font.zip` artifact from the successful staging workflow.

Keep the GitHub release version aligned with the npm package version that was actually approved.

## Release invariants

A production release is acceptable only when all of these remain true:

- the version is reviewed in Git before staging;
- build inputs are committed;
- the clean runner rebuild succeeds;
- Fontspector is blocking for release packaging;
- package contents pass the staging allow-list;
- the staged tarball is the same tarball uploaded as the workflow artifact;
- no long-lived npm publishing token is used;
- CI can stage but cannot perform the final 2FA approval;
- direct local `npm publish` is not used as an emergency shortcut.

## Recovery

### Workflow fails before staging

Fix the source/pipeline problem in a PR. Nothing has been published.

### Staging fails

Check:

- trusted publisher repository name;
- trusted publisher workflow filename (`release.yaml`);
- GitHub Environment name (`npm-staging`);
- package `repository.url`;
- Node/npm versions;
- whether the version already exists or is already staged.

Do not add an automation token just to bypass OIDC configuration.

### Staged package is wrong

Reject it. Fix the repository and prepare a corrected version through a PR.

### npm is public but GitHub release is missing

Do not republish the npm version. Create the matching GitHub release using the already successful workflow artifact and verify its checksum.
