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
from .parsers.base import BaseParser

console = Console()


if not Token.has_extension("page_number"):
    Token.set_extension("page_number", default=None)


def pdf_reader(
    pdf_path: str, 
    nlp: spacy.Language, 
    pdf_parser: BaseParser = pdfminer.Parser,
    **kwargs
) -> spacy.tokens.Doc:
    
    console.rule(f"{pdf_path}")
    console.print(f"PDF to text engine: [blue bold]{pdf_parser.name}[/]...")
    
    pdf_path = os.path.normpath(pdf_path)
    num_pages = get_number_of_pages(pdf_path)
    
    # Convert pdf to text.
    console.print(f"Extracting text from {num_pages} pdf pages...")
    with console.status("Working..."):
        texts = []
        for page_num in range(1, num_pages + 1):
            parser = pdf_parser(pdf_path, page_num)
            text = parser.pdf_to_text(**kwargs)
            texts.append(text)

    # Convert text to spaCy Doc objects.
    console.print("Converting text to [blue bold]spaCy[/] Doc...")
    with console.status("Working..."):
        docs = [doc for doc in nlp.pipe(texts)]

        for idx, doc in enumerate(docs):
            page_num = idx + 1
            for token in doc:
                token._.page_number = page_num

            combined_doc = Doc.from_docs(docs)
    console.print(":white_check_mark: [green]Complete!")
    return combined_doc
