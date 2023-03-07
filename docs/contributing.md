# Contributing

## Deployment checklist

Before merging changes into main the following must be completed:

- [ ] Bump the version number in *pyproject.toml* and *spacypdfreader.__init__.py*
- [ ] Format the code: `poetry run shed`
- [ ] Run pytest: `pytest`
- [ ] Check the docs locally: `mkdocs serve`

After merging the pull request:

- [ ] Create a new release on GitHub
- [ ] Publish latest docs to GitHub pages: `rm -rf site; mkdocs build; mkdocs gh-deploy;`
- [ ] Publish latest package to PyPi: `poetry publish --build`

## Code style

The black code formatter should be run against all code.

```bash
black spacypdfreader
```

## Documentation

Documentation is built using [Material for mkdocs](https://squidfunk.github.io/mkdocs-material/). All of the documentations lives within the `docs/` directory.

### Test the docs locally

To test the docs locally run the following command:

```bash
mkdocs serve
```

### Publish the docs

The docs are hosted on using GitHub pages at [https://samedwardes.github.io/spaCyPDFreader/contributing/](https://samedwardes.github.io/spaCyPDFreader/contributing/).

Run the following to update the docs:

```bash
rm -rf site
mkdocs build
mkdocs gh-deploy
```