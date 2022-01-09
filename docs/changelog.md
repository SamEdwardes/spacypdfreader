# Changelog

## 0.2.1 (2022-01-09)

- Added examples to the API docs.
- Added continuos deployment for GitHub pages.

## 0.2.0 (2021-12-10)

- Added support for additional pdf to text extraction engines:
    - [pytesseract](https://pypi.org/project/pytesseract/)
    - [textract](https://textract.readthedocs.io/en/stable/index.html)
- Added the ability to bring your own pdf to text extraction engine.
- Added new spacy extension attributes and methods:
    - `doc._.page_range`
    - `doc._.first_page`
    - `doc._.last_page`
    - `doc._.pdf_file_name`
    - `doc._.page(int)`
- Built a new documentation site: [https://samedwardes.github.io/spaCyPDFreader/](https://samedwardes.github.io/spaCyPDFreader/)

## 0.1.1 (2021-12-10)

- 0.1.1 Python ^3.7 support by @SamEdwardes in [https://github.com/SamEdwardes/spaCyPDFreader/pull/2](https://github.com/SamEdwardes/spaCyPDFreader/pull/2)

