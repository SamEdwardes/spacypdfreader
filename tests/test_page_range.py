import pytest
import spacy

from spacypdfreader.parsers import pdfminer, pytesseract
from spacypdfreader.spacypdfreader import pdf_reader


def pdf_assertions(doc: spacy.tokens.Doc):
    # Page numbers.
    assert doc[0]._.page_number == 2
    assert doc[-1]._.page_number == 3
    # Doc attributes.
    assert doc._.page_range == (2, 3)
    assert doc._.first_page == 2
    assert doc._.last_page == 3
    assert doc._.pdf_file_name == "tests/data/test_pdf_01.pdf"


def test_page_range_pdfminer_single():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader(
        "tests/data/test_pdf_01.pdf", nlp, pdfminer.parser, page_range=(2, 3)
    )
    pdf_assertions(doc)


def test_page_range_pdfminer_multi():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader(
        "tests/data/test_pdf_01.pdf",
        nlp,
        pdfminer.parser,
        page_range=(2, 3),
        n_processes=2,
    )
    pdf_assertions(doc)


def test_page_range_pytesseract_single():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader(
        "tests/data/test_pdf_01.pdf", nlp, pytesseract.parser, page_range=(2, 3)
    )
    pdf_assertions(doc)


def test_page_range_pytesseract_multi():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader(
        "tests/data/test_pdf_01.pdf",
        nlp,
        pytesseract.parser,
        page_range=(2, 3),
        n_processes=2,
    )
    pdf_assertions(doc)


def test_page_range_logic():
    nlp = spacy.load("en_core_web_sm")
    with pytest.raises(ValueError):
        doc = pdf_reader(
            "tests/data/test_pdf_01.pdf",
            nlp,
            pytesseract.parser,
            page_range=(10, 20),
            n_processes=2,
        )
    with pytest.raises(ValueError):
        doc = pdf_reader(
            "tests/data/test_pdf_01.pdf",
            nlp,
            pytesseract.parser,
            page_range=(-1, 2),
            n_processes=2,
        )
    with pytest.raises(ValueError):
        doc = pdf_reader(
            "tests/data/test_pdf_01.pdf",
            nlp,
            pytesseract.parser,
            page_range=(3, 1),
            n_processes=2,
        )
