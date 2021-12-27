import os

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from spacy.tokens import Doc, Span


def _filter_doc_by_page(doc: Doc, page_number: str) -> Span:
    """Filter the doc by page number.

    Args:
        doc: The doc to filter.
        page_number: The page number to filter on.

    Returns:
        The doc filtered on a specific page.
    """
    # Validate the input.
    first_page = doc[0]._.page_number
    last_page = doc[-1]._.page_number
    if page_number > last_page or page_number < first_page:
        msg = f"The doc has pages {first_page} to {last_page}. Page {page_number} is out of range."
        raise ValueError(msg)

    for idx, token in enumerate(doc):
        if token._.page_number == page_number:
            start_idx = idx
            break

    for idx, token in enumerate(doc):
        if idx == len(doc) - 1:
            end_idx = idx
            break
        elif token._.page_number > page_number:
            end_idx = idx
            break

    return doc[start_idx:end_idx]


def _get_number_of_pages(pdf_path: str) -> int:
    """Find the number of pages in a pdf document.
    
    Args:
        pdf_path: Path to a PDF file.
        
    Returns:
        The number of pages in a pdf file.
    """
    with open(os.path.normpath(pdf_path), "rb") as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        num_pages = len(list(PDFPage.create_pages(doc)))
    return num_pages
