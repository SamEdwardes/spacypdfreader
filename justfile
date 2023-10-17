format:
    # Source code
    poetry run black spacypdfreader
    poetry run isort spacypdfreader
    # Tests
    poetry run black tests
    poetry run isort tests

test:
    poetry run pytest
    poetry run pytest --doctest-modules spacypdfreader/

test-gha:
    gh workflow run pytest.yml --ref $(git branch --show-current)

preview-docs:
    poetry run mkdocs serve

publish-docs:
    rm -rf site
    mkdocs build
    mkdocs gh-deploy

publish:
    poetry publish --build