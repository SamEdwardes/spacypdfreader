"""
Convert pdf to text using the pytesseract library.
"""

import spacy
from spacypdfreader.parsers.pytesseract import PytesseractParser
from spacypdfreader.spacypdfreader import pdf_reader


def test_pytesseract():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, PytesseractParser)
    # Page numbers.
    assert doc[0]._.page_number == 1
    assert doc[-1]._.page_number == 4
    # Tokens.
    assert doc[0].text == "Test"
    assert doc[-4].text == "data"
    # Doc attributes.
    assert doc._.page_range == (1, 4)
    assert doc._.first_page == 1
    assert doc._.last_page == 4


def test_pytesseract_with_params():
    params = {
        "nice": 1
    }
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, PytesseractParser, **params)
    # Page numbers.
    assert doc[0]._.page_number == 1
    assert doc[-1]._.page_number == 4
    # Tokens.
    assert doc[0].text == "Test"
    assert doc[-4].text == "data"
    # Doc attributes.
    assert doc._.page_range == (1, 4)
    assert doc._.first_page == 1
    assert doc._.last_page == 4

