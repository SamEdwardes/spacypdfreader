# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

spacypdfreader is a Python library that extracts text from PDF documents and converts them into spaCy `Doc` objects with custom extensions for page tracking. The library supports multiple PDF parsing backends and multiprocessing for performance. Refer to @README.md for more details about the library.

## Development Commands

This project uses `uv` for dependency management and `just` as a command runner.

### Testing

```bash
# Run tests with a specific Python version (default 3.12)
just test 3.12

# Run tests across multiple Python versions
just test-matrix

# Test doctests in the code
just test-docs

# Trigger GitHub Actions workflow
just test-gha
```

### Code Quality

```bash
# Format code (imports and style)
just format

# Run linting
just lint
```

### Documentation

```bash
# Preview docs locally
just preview-docs

# Publish docs to GitHub Pages
just publish-docs
```

### Building and Publishing

```bash
# Build the package
just build

# Publish to test PyPI
just publish-test

# Publish to PyPI
just publish
```

## Architecture

### Core Components

- **`spacypdfreader.spacypdfreader.pdf_reader()`**: Main entry point function that converts a PDF to a spaCy `Doc` object
  - Takes a PDF path and a spaCy `Language` object
  - Returns a `Doc` object with custom extensions
  - Supports multiprocessing via `n_processes` parameter
  - Supports page range extraction via `page_range` parameter

### Parser System

The library uses a pluggable parser architecture in `spacypdfreader/parsers/`:

- **pdfminer** (`parsers/pdfminer.py`): Default parser, fast but lower accuracy
  - Uses `pdfminer.high_level.extract_text()`
  - Zero-indexed internally but converts from 1-indexed API

- **pytesseract** (`parsers/pytesseract.py`): OCR-based parser, slower but higher accuracy
  - Converts PDF pages to images first
  - Requires optional dependencies: `pip install 'spacypdfreader[pytesseract]'`

Each parser implements a `parser(pdf_path: str, page_number: int, **kwargs)` function that returns text for a single page.

### spaCy Custom Extensions

The library registers several custom attributes on spaCy tokens and docs:

- `token._.page_number`: Page number for each token (1-indexed)
- `doc._.pdf_file_name`: Original PDF file path
- `doc._.first_page`: First page number in the doc
- `doc._.last_page`: Last page number in the doc
- `doc._.page_range`: Tuple of (first_page, last_page)
- `doc._.page(int)`: Method to extract text from a specific page

These extensions are registered in `spacypdfreader/spacypdfreader.py` at module import time.

### Processing Flow

1. PDF path and spaCy Language object provided to `pdf_reader()`
2. PDF page count determined using pdfminer's `PDFParser`
3. Pages extracted in parallel (if `n_processes` specified) or sequentially
4. Each page text converted to a spaCy `Doc` via `nlp.pipe()`
5. Page numbers assigned to all tokens
6. Individual page `Doc` objects combined using `Doc.from_docs()`
7. Custom extensions set on the combined doc

## Important Notes

- This library breaks spaCy convention: it does NOT use `nlp.add_pipe()` because text extraction must happen before spaCy processing
- Page numbers use 1-based indexing in the public API (but pdfminer uses 0-based internally)
- When using pdfminer parser, do NOT pass `page_numbers` kwarg - use `page_range` instead
- Multiprocessing uses `ThreadPool` not `ProcessPool` (see imports in spacypdfreader.py:4)

## Testing Notes

- Test files are in `tests/data/` directory
- Tests use spaCy model `en_core_web_sm` which is installed via uv from a wheel URL
- The project supports Python 3.9 through 3.13 (Python 3.14+ not supported)

## Python Version Support

This project supports Python 3.9 through 3.13. **Python 3.14 is not supported** due to a dependency constraint:

- spaCy (the core dependency) requires `Python <3.14, >=3.9`
- spaCy uses Pydantic v1 internally, which is incompatible with Python 3.14
- This is a known upstream issue tracked in spaCy issue #13885
- Support for Python 3.14 will be added once spaCy releases a compatible version
