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
    
    console.rule(f"Converting pdf to text")
    console.print(f"Using: {pdf_to_text_method}...")
    
    pdf_path = os.path.normpath(pdf_path)
    num_pages = get_number_of_pages(pdf_path)
    
    console.print(f"Extracting text from {num_pages} pdf pages...")
    with console.status("Working..."):
        texts = []
        for page_num in range(1, num_pages + 1):
            text = pdf_to_text_method(pdf_path, page_num, **kwargs)
            texts.append(text)

    console.print("Converting text to [blue bold]spaCy[/] Doc...")
    with console.status("Working..."):
        docs = [doc for doc in nlp.pipe(texts)]

        for idx, doc in enumerate(docs):
            page_num = idx + 1
            for token in doc:
                token._.page_number = page_num

            combined_doc = Doc.from_docs(docs)
    console.print(":white_check_mark: Complete!")
    return combined_doc
