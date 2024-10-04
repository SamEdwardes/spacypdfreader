# Contributing

## Deployment checklist

Before merging changes into main the following must be completed:

- [ ] Bump the version number in *pyproject.toml* and *spacypdfreader.__init__.py*
- [ ] Format the code: `just format`
- [ ] Run pytest:

    ```bash
    just test-matrix
    just test-docs
    ```
- Test publishing to test PyPI: `just publish-test`
- [ ] Check the docs locally: `just preview-docs`

After merging the pull request:

- [ ] Create a new release on GitHub
- [ ] Publish latest docs to GitHub pages: `just publish-docs`
- [ ] Publish latest package to PyPi: `just publish`

## Code style

The ruff code formatter should be run against all code.

```bash
just format
```

## Documentation

Documentation is built using [Material for mkdocs](https://squidfunk.github.io/mkdocs-material/). All of the documentations lives within the `docs/` directory.

### Test the docs locally

To test the docs locally run the following command:

```bash
just preview-docs
```

### Publish the docs

The docs are hosted on using GitHub pages at [https://samedwardes.github.io/spaCyPDFreader/contributing/](https://samedwardes.github.io/spaCyPDFreader/contributing/).

Run the following to update the docs:

```bash
just publish-docs
```