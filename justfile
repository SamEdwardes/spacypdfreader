default:
    @just --list

[group('package')]
publish:
    uv publish --build

[group('lint')]
format:
    # Sort imports
    uvx ruff check --select I --fix .
    # Format code
    uvx ruff format .

[group('lint')]
lint:
    uvx ruff check .

[group('tests')]
test version="3.12":
    uv run --python {{version}} --all-extras pytest

[group('tests')]
test-matrix:
    just test 3.9
    just test 3.10
    just test 3.11
    just test 3.12

[group('tests')]
test-pre-release-python:
    # As of 2024-10-04 3.13 is failing
    just test 3.13

[group('tests')]
test-gha:
    gh workflow run pytest.yml --ref $(git branch --show-current)

[group('docs')]
preview-docs:
    uv run mkdocs serve

[group('docs')]
publish-docs:
    rm -rf site
    uv run mkdocs build
    uv run mkdocs gh-deploy

[group('docs')]
test-docs:
    uv run --python 3.12 --all-extras pytest --doctest-modules spacypdfreader/
