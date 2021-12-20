import os

from pdfminer.high_level import extract_text
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def get_number_of_pages(pdf_path: str) -> int:
    with open(os.path.normpath(pdf_path), 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        num_pages =  len(list(PDFPage.create_pages(doc)))
    return num_pages


def parser(pdf_path: str, page_number: int, **kwargs):
    text = extract_text(pdf_path, page_numbers=[page_number], **kwargs)
    return text
    
