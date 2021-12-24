# Contributing

## Documentation

## Generating API docs with pydoc-markdown

The documentation is built using pydoc-markdown. If you make a change to the documentation please verify that it works and is rendered correctly by running:

```bash
pydoc-markdown --server --open
```

Create a *requirements.txt file:

```bash
poetry export --without-hashes --output requirements.txt
```