format:
    poetry run shed

test:
    poetry run pytest
    poetry run pytest --doctest-modules spacypdfreader/

preview-docs:
    poetry run mkdocs serve

publish-docs:
    rm -rf site
    mkdocs build
    mkdocs gh-deploy