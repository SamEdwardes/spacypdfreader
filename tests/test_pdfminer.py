import spacy

from spacypdfreader.spacypdfreader import pdf_reader
from spacypdfreader.parsers.pdfminer import PdfminerParser

def test_pdfminer():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, PdfminerParser)
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
    

def test_pdfminer_with_params():
    params = {
        "caching": False
    }
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, PdfminerParser, **params)
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