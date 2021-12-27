import spacy

from spacypdfreader import __version__
from spacypdfreader._utils import _get_number_of_pages
from spacypdfreader.spacypdfreader import pdf_reader


def test_version():
    assert __version__ == '0.2.0'


def test_get_number_of_pages():
    assert _get_number_of_pages("tests/data/wikipedia.pdf") == 18
    assert _get_number_of_pages("tests/data/test_pdf_01.pdf") == 4
    

def test_page_numbers():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
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