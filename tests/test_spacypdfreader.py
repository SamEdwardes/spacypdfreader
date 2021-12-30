import spacy
from spacypdfreader import __version__
from spacypdfreader._utils import _get_number_of_pages
from spacypdfreader.parsers.pdfminer import PdfminerParser
from spacypdfreader.parsers.pytesseract import PytesseractParser
from spacypdfreader.spacypdfreader import pdf_reader


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


def test_version():
    assert __version__ == "0.2.0"


def test_get_number_of_pages():
    assert _get_number_of_pages("tests/data/wikipedia.pdf") == 18
    assert _get_number_of_pages("tests/data/test_pdf_01.pdf") == 4


def test_page_numbers():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
    pdf_assertions(doc)


def test_pdfminer():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, PdfminerParser)
    pdf_assertions(doc)


def test_pdfminer_with_params():
    params = {"caching": False}
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, PdfminerParser, **params)
    pdf_assertions(doc)


def test_pytesseract():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, PytesseractParser)
    pdf_assertions(doc)


def test_pytesseract_with_params():
    params = {"nice": 1}
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, PytesseractParser, **params)
    pdf_assertions(doc)
