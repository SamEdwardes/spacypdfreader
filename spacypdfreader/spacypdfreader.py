import os
from typing import Callable
from dataclasses import dataclass, field

import spacy
from pdfminer.high_level import extract_text
from rich.console import Console
from rich.progress import track
from spacy.tokens import Doc, Token

from .parsers.pdfminer import get_number_of_pages
from .parsers import pdfminer

console = Console()


if not Token.has_extension("page_number"):
    Token.set_extension("page_number", default=None)


def pdf_reader(
    pdf_path: str, 
    nlp: spacy.Language, 
    pdf_to_text_method: Callable = pdfminer.parser, 
    **kwargs
) -> spacy.tokens.Doc:
    pdf_path = os.path.normpath(pdf_path)
    num_pages = get_number_of_pages(pdf_path)
    console.print(f"Extracting text from {num_pages} pdf pages...")

    texts = []
    for page_num in track(
        range(num_pages), f"Extracting text from {num_pages} pdf pages..."
    ):
        text = pdf_to_text_method(pdf_path, page_num, **kwargs)
        texts.append(text)

    docs = [doc for doc in nlp.pipe(texts)]

    for idx, doc in enumerate(docs):
        page_num = idx + 1
        for token in doc:
            token._.page_number = page_num

    combined_doc = Doc.from_docs(docs)
    return combined_doc
