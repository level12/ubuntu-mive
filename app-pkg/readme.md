# mivepy

## Copier Template

Project structure and tooling mostly derives from the [copier-py-package](https://github.com/level12/copier-py-package),
see its documentation for context and additional instructions.

This project can be updated from the upstream repo, see [updates](https://github.com/level12/copier-py-package?tab=readme-ov-file#updates)

## Project Setup

From zero to hero (passing tests that is):

1. Ensure host dependencies are installed:

  - [reqs](https://github.com/level12/reqs): for virtualenv python deps
  - [mise](https://mise.jdx.dev/): for everything else, e.g. terraform, npm

2. Start docker service dependencies (if applicable):

   `docker compose up -d`

3. Run tests:

   `nox`

4. Use mise to activate the virtualenv for local dev

5. Install deps in active virtualenv:

    - `reqs bootstrap`
    - `reqs sync`

6. Configure pre-commit:

   `pre-commit install`


## Versions

Versions are date based.  Tools:

- Current version: `hatch version`
- Bump version based on date, tag, push: `mise run bump`
   - Options: `mise run bump -- --help`
