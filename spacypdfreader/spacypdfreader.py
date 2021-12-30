import os
from dataclasses import dataclass, field
from typing import Any, Callable

import spacy
from pdfminer.high_level import extract_text

from rich.progress import track
from spacy.tokens import Doc, Token, Span

from .console import console
from .parsers import pdfminer
from .parsers.base import BaseParser
from ._utils import _filter_doc_by_page, _get_number_of_pages


# Set up the spacy custom extensions.

if not Token.has_extension("page_number"):
    Token.set_extension("page_number", default=None)

if not Doc.has_extension("pdf_file_name"):
    Doc.set_extension("pdf_file_name", default=None)

if not Doc.has_extension("page"):
    Doc.set_extension("page", method=_filter_doc_by_page)

if not Doc.has_extension("first_page"):
    Doc.set_extension("first_page", getter=lambda doc: doc[0]._.page_number)

if not Doc.has_extension("last_page"):
    Doc.set_extension("last_page", getter=lambda doc: doc[-1]._.page_number)

if not Doc.has_extension("page_range"):
    Doc.set_extension(
        "page_range", getter=lambda doc: (doc._.first_page, doc._.last_page)
    )


def pdf_reader(
    pdf_path: str,
    nlp: spacy.Language,
    pdf_parser: BaseParser = pdfminer.PdfminerParser,
    verbose: bool = False,
    **kwargs: Any,
) -> spacy.tokens.Doc:
    """Convert a PDF document to a spaCy Doc object.

    Args:
        pdf_path: Path to a PDF file.
        nlp: A spaCy Language object with a loaded pipeline. For example
            `spacy.load("en_core_web_sm")`.
        pdf_parser: The parser to convert PDF file to text. Read the docs for
            more detailsDefaults to pdfminer.Parser.
        verbose: If True details will be printed to the terminal. By default,
            False.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        A spacy Doc object with the custom extensions.
    """
    if verbose:
        console.print(f"PDF to text engine: [blue bold]{pdf_parser.name}[/]...")

    pdf_path = os.path.normpath(pdf_path)
    num_pages = _get_number_of_pages(pdf_path)

    # Convert pdf to text.
    if verbose:
        console.print(f"Extracting text from {num_pages} pdf pages...")
    texts = []
    for page_num in range(1, num_pages + 1):
        parser = pdf_parser(pdf_path, page_num)
        text = parser.pdf_to_text(**kwargs)
        texts.append(text)

    # Convert text to spaCy Doc objects.
    if verbose:
        console.print("Converting text to [blue bold]spaCy[/] Doc...")

    docs = [doc for doc in nlp.pipe(texts)]
    for idx, doc in enumerate(docs):
        page_num = idx + 1
        for token in doc:
            token._.page_number = page_num

    combined_doc = Doc.from_docs(docs)
    combined_doc._.pdf_file_name = pdf_path

    if verbose:
        console.print(":white_check_mark: [green]Complete!")

    return combined_doc
