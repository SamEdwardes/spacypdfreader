import pytest
import spacy

from spacypdfreader.parsers import pdfminer
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


def test_default():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
    pdf_assertions(doc)


def test_pdfminer():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pdfminer.parser)
    pdf_assertions(doc)


def test_pdfminer_with_params():
    params = {"caching": False}
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pdfminer.parser, **params)
    pdf_assertions(doc)


def test_pdfminer_multi():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pdfminer.parser, n_processes=4)
    pdf_assertions(doc)


def test_pdfminer_multi_with_params():
    params = {"caching": False}
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader(
        "tests/data/test_pdf_01.pdf", nlp, pdfminer.parser, n_processes=4, **params
    )
    pdf_assertions(doc)


def test_pdfminer_multi_same_as_single():
    nlp = spacy.load("en_core_web_sm")
    doc_multi = pdf_reader(
        "tests/data/test_pdf_01.pdf", nlp, pdfminer.parser, n_processes=4
    )
    doc_single = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pdfminer.parser)
    assert doc_multi.text == doc_single.text


def test_pdfminer_rejects_n_pages():
    nlp = spacy.load("en_core_web_sm")
    with pytest.raises(ValueError):
        doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pdfminer.parser, page_numbers=[1, 2])