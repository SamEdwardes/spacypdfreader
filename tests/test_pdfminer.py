import spacy

from spacypdfreader.spacypdfreader import pdf_reader
from spacypdfreader.parsers.pdfminer import Parser

def test_pdfminer():
    nlp = spacy.load("en_core_web_sm")
    doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, Parser)
    assert doc[0]._.page_number == 1
    assert doc[-1]._.page_number == 4