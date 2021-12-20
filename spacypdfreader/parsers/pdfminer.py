"""
Convert pdf to text using the pdfminer library.
"""

import os

from rich import inspect

from pdfminer.high_level import extract_text

from .base import BaseParser


class Parser(BaseParser):
    name: str = "pdfminer"
    
    def pdf_to_text(self, **kwargs) -> str:
        # pdfminer uses zero indexed page numbers. Therefore need to remove 1
        # from the page count.
        self.page_number -= 1
        text = extract_text(self.pdf_path, page_numbers=[self.page_number], **kwargs)
        return text
        
        


