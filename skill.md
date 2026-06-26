---
name: spacypdfreader
description: >
  A PDF to text extraction pipeline component for spaCy. Use when writing Python code that uses the spacypdfreader package.
license: MIT
compatibility: Requires Python >=3.9, <3.14.
---

# spacypdfreader

A PDF to text extraction pipeline component for spaCy.

## Installation

```bash
pip install spacypdfreader
```

## API overview

### Functions

The main entry point for converting a PDF into a spaCy Doc.

- `spacypdfreader.pdf_reader`

### Parsers

Built-in PDF-to-text parsers. Pass one of these to the `pdf_parser` argument of `pdf_reader`, or bring your own.

- `parsers.pdfminer.parser`
- `parsers.pytesseract.parser`

## Resources

- [Full documentation](https://samedwardes.github.io/spacypdfreader/)
- [llms.txt](llms.txt) — Indexed API reference for LLMs
- [llms-full.txt](llms-full.txt) — Comprehensive documentation for LLMs
- [Source code](https://github.com/SamEdwardes/spaCyPDFreader.git)
