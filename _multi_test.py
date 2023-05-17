import time
from functools import wraps

import spacy
from spacypdfreader import pdf_reader
from spacypdfreader.console import console
from spacypdfreader.parsers import pytesseract, pdfminer
from pathlib import Path
from rich.panel import Panel
from rich import inspect


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
def run(n_processes):
    console.rule(f"{n_processes=}")
    doc = pdf_reader(file_name, nlp, pytesseract.PytesseractParser, n_processes=n_processes, verbose=True)
    return doc

doc = run(None)


