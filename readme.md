[![mive](https://github.com/level12/ubuntu-mive/actions/workflows/mive.yaml/badge.svg)](https://github.com/level12/ubuntu-mive/actions/workflows/mive.yaml)
[![app](https://github.com/level12/ubuntu-mive/actions/workflows/app.yaml/badge.svg)](https://github.com/level12/ubuntu-mive/actions/workflows/app.yaml)

This repo has three sub-projects:

* base: a Docker ubuntu based image prepped for our dev needs
    * Pushes to: [ghcr.io/level12/ubuntu-base](https://github.com/level12/ubuntu-mive/pkgs/container/ubuntu-base)
    * Tags: 22.04, 24.04, etc.
* mive: uses `base` and installs mise, uv, and a Python version
    * Pushes to: [ghcr.io/level12/ubuntu-mive](https://github.com/level12/ubuntu-mive/pkgs/container/ubuntu-mive)
    * Tags `{ubuntu}-{py}`: 24.04-3.12, 24.04-3.13, etc.
    * Includes a `mive-version-checks` script which can be ran in an app's CI to ensure the images
      are up-to-date.
* app-pkg
    * A [copier-py](https://github.com/level12/copier-py-package) based app
    * A [workflow](https://github.com/level12/ubuntu-mive/actions/workflows/app.yaml) to ensure and
      demonstrate how to use a `mive` image to run the nox tests


# Dev

- No CircleCI, just GH workflows
- Mive workflow is scheduled to build nightly
- Use `mise build-all` for docker builds to ensure latest images are pulled
