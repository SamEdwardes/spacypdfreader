"""
Convert pdf to text using the pdfminer library.
"""

import os

from pdfminer.high_level import extract_text
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

from rich import inspect

from .base import BaseParser


def get_number_of_pages(pdf_path: str) -> int:
    with open(os.path.normpath(pdf_path), 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        num_pages =  len(list(PDFPage.create_pages(doc)))
    return num_pages


class Parser(BaseParser):
    name: str = "pdfminer"
    
    def pdf_to_text(self, **kwargs) -> str:
        # pdfminer uses zero indexed page numbers. Therefore need to remove 1
        # from the page count.
        self.page_number -= 1
        text = extract_text(self.pdf_path, page_numbers=[self.page_number], **kwargs)
        return text
        
        


