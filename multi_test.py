import time
from functools import wraps

import spacy
from spacypdfreader import pdf_reader
from spacypdfreader.parsers.pytesseract import PytesseractParser
from spacypdfreader.parsers.pdfminer import PdfminerParser
from spacypdfreader.console import console
from rich.panel import Panel



def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        console.print(f'[bold]{func.__name__} took {end - start:.6f} seconds to complete')
        return result
    return wrapper


nlp = spacy.load("en_core_web_sm")
# file_name = "tests/data/wikipedia.pdf"
file_name = "tests/data/test_pdf_01.pdf"

@timeit
def no_multi_tesseract():
    console.rule("No multi - pytesseract")
    doc = pdf_reader(file_name, nlp, PytesseractParser, n_processes=None, verbose=True)
    # console.print(Panel(doc.text[100:200]))
    return doc

@timeit
def with_multi_tesseract():
    console.rule("With multi - pytesseract")
    doc = pdf_reader(file_name, nlp, PytesseractParser, n_processes=8, verbose=True)
    # console.print(Panel(doc.text[100:200]))
    return doc

@timeit
def no_multi_pdfminer():
    console.rule("No multi - pdfminer")
    doc = pdf_reader(file_name, nlp, PdfminerParser, n_processes=None, verbose=True)
    # console.print(Panel(doc.text[100:200]))
    return doc

@timeit
def with_multi_pdfminer():
    console.rule("With multi - pdfminer")
    doc = pdf_reader(file_name, nlp, PdfminerParser, n_processes=8, verbose=True)
    # console.print(Panel(doc.text[100:200]))
    return doc

# Pytesseract
# no_multi_doc_pytesseract = no_multi_tesseract()
with_multi_doc_pytesseract = with_multi_tesseract()
# assert no_multi_doc_pytesseract.text == with_multi_doc_pytesseract.text

# PDF miner
# no_multi_doc_pdfminer = no_multi_pdfminer()
# with_multi_doc_pdfminer = with_multi_pdfminer()
# assert no_multi_doc_pdfminer.text == with_multi_doc_pdfminer.text
