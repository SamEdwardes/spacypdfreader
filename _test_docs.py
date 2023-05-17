# ------------------------------------------------------------------------------
# PDF miner
# ------------------------------------------------------------------------------

import spacy
from spacypdfreader import pdf_reader

nlp = spacy.load("en_core_web_sm")
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)

import spacy
from spacypdfreader import pdf_reader
from spacypdfreader.parsers.pdfminer import parser

nlp = spacy.load("en_core_web_sm")
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, parser)

import spacy
from spacypdfreader import pdf_reader
from spacypdfreader.parsers.pdfminer import parser

nlp = spacy.load("en_core_web_sm")
params = {"caching": False}
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, parser, **params)

# ------------------------------------------------------------------------------
# Pytesseract
# ------------------------------------------------------------------------------
import spacy
from spacypdfreader import pdf_reader
from spacypdfreader.parsers.pytesseract import parser

nlp = spacy.load("en_core_web_sm")
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, parser)

import spacy
from spacypdfreader import pdf_reader
from spacypdfreader.parsers.pytesseract import parser

nlp = spacy.load("en_core_web_sm")
params = {"nice": 1}
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, parser, **params)