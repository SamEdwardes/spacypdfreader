# Changelog

## 0.3.1 (2023-10-17)

**Changes**

Nonepo

**Fixes**

- Remove `shed` as a depdency. It was removing unused imports that were required ([#17](https://github.com/SamEdwardes/spacypdfreader/issues/17)).

## 0.3.0 (2023-05-17)

**Changes**

- Added support for multi-processing. For example:

    ```python
    import spacy

    from spacypdfreader.parsers import pytesseract
    from spacypdfreader.spacypdfreader import pdf_reader

    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pytesseract.parser, n_processes=4)
    print(doc._.first_page)
    print(doc._.last_page)
    print(doc[12].text)
    print(doc[12]._.page_number)
    ```

- Changed the way in which parsers are implemented. They are now implemented with a function as opposed to a class. See <https://github.com/SamEdwardes/spacypdfreader/tree/feature/multi-processing/spacypdfreader/parsers> for examples.

**Fixes**

None

## 0.2.1 (2022-01-09)

- Added examples to the API docs.
- Added continuous deployment for GitHub pages.

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
