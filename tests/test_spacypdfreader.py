import spacy

from spacypdfreader import __version__
from spacypdfreader.spacypdfreader import get_number_of_pages, pdf_reader


def test_version():
    assert __version__ == '0.1.0'


def test_get_number_of_pages():
    assert get_number_of_pages("tests/data/wikipedia.pdf") == 18
    assert get_number_of_pages("tests/data/test_pdf_01.pdf") == 4


def test_pdf_reader():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
    assert doc[0]._.page_number == 1
    assert doc[-1]._.page_number == 4