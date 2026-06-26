# Contributing


# Deployment checklist

Before merging changes into main the following must be completed:

Bump the version number in *pyproject.toml* and *spacypdfreader.\_\_init\_\_*.py\_

Format the code: `just format`

Lint: `just lint`

Run pytest:

``` bash
just test-matrix
just test-docs
```

Test publishing to test PyPI: `just publish-test`

Check the docs locally: `just preview-docs`

After merging the pull request:

Create a new release on GitHub

Publish latest package to PyPi: `just publish`

The documentation is published automatically to GitHub Pages by the `CI Docs` GitHub Actions workflow on every push to `main`, so no manual docs deployment step is required.


# Code style

The ruff code formatter should be run against all code.

``` bash
just format
```


# Pre-commit hooks

This project uses [prek](https://github.com/j178/prek) to manage Git pre-commit hooks. prek is a drop-in replacement for `pre-commit` and reads its configuration from `prek.toml`. The hooks run ruff (import sorting, linting, and formatting), rumdl (Markdown formatting), and a set of basic file checks.

prek is included in the `dev` dependency group, so no separate install is required. Enable the hooks once after cloning the repository:

``` bash
uv run prek install
```

The hooks then run automatically on every `git commit`. To run them against all files on demand:

``` bash
uv run prek run --all-files
```


# Documentation

Documentation is built using [Great Docs](https://posit-dev.github.io/great-docs/), a Quarto-based documentation generator for Python packages. All of the documentation content lives in `great-docs.yml`, the `user_guide/` directory, and the docstrings within the package source code.

Building the docs requires [Quarto](https://quarto.org/docs/get-started/) to be installed locally. Great Docs itself is run through `uvx`, so it does not need to be added to the project dependencies.


## Test the docs locally

To preview the docs locally run the following command:

``` bash
just preview-docs
```


## Publish the docs

The docs are hosted using GitHub Pages at <https://samedwardes.github.io/spacypdfreader/>. They are rebuilt and published automatically by the `CI Docs` workflow (`.github/workflows/docs.yml`) on every push to the `main` branch.
