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
ln ../README.md index.md
```

### Test the docs locally

To test the docs locally run the following command:

```bash
mkdocs serve
```

> See [https://docs.civicrm.org/dev/en/latest/extensions/documentation/#:readme-mirrored](https://docs.civicrm.org/dev/en/latest/extensions/documentation/#:readme-mirrored) for reference.