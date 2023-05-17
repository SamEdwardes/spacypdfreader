import spacy
from spacypdfreader import __version__
from spacypdfreader.parsers import pdfminer
from spacypdfreader.parsers import pytesseract
from spacypdfreader.spacypdfreader import pdf_reader
import pytest


def pdf_assertions(doc: spacy.tokens.Doc):
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
    assert doc._.pdf_file_name == "tests/data/test_pdf_01.pdf"

# ------------------------------------------------------------------------------
# pdfminer
# ------------------------------------------------------------------------------


def test_pdfminer():
    nlp = spacy.load("en_core_web_sm")
    with pytest.deprecated_call():
        doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pdfminer.PdfminerParser)
    pdf_assertions(doc)


def test_pytesseract():
    nlp = spacy.load("en_core_web_sm")
    with pytest.deprecated_call():
        doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pytesseract.PytesseractParser)
    pdf_assertions(doc)