# Contributing

## Code style

The black code formatter should be run against all code.

```bash
black spacypdfreader
```

## Documentation

Documentation is built using [Material for mkdocs](https://squidfunk.github.io/mkdocs-material/). All of the documentations lives within the `docs/` directory.

Note that the `README.md` and `docs/index.md` contain the exact same content. This is done by mirroring the `README.md` file:

```bash
ln - s README.md docs/index.md
```

### Test the docs locally

To test the docs locally run the following command:

```bash
mkdocs serve
```

### Publish the docs

The docs are hosted on using GitHub pages at [https://samedwardes.github.io/spaCyPDFreader/contributing/](https://samedwardes.github.io/spaCyPDFreader/contributing/). Every commit or pull request against the main branch will trigger a build.