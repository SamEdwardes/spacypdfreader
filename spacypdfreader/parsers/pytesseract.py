"""
Convert pdf to text using the pytesseract library.

Reference:
----------
https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/
"""

import os
import tempfile

from pdf2image import convert_from_path
from PIL import Image

from pytesseract import image_to_string

from ..console import console
from .base import BaseParser


def parser(pdf_path: str, page_number: int, **kwargs):
    
    with tempfile.TemporaryDirectory() as tmp_dir:
        
        # Convert pdf page to image.
        file_name = convert_from_path(
            pdf_path,
            output_folder=tmp_dir,
            paths_only=True,
            first_page=page_number,
            last_page=page_number + 1
        )[0]
        
        # Convert images to text.
        file_path = os.path.join(tmp_dir, file_name)
        text = str(image_to_string(Image.open(file_path)))
        
    return text


class Parser(BaseParser):
    name: str = "pytesseract"
    
    def pdf_to_text(self, **kwargs) -> str:
        with tempfile.TemporaryDirectory() as tmp_dir:
            
            # Convert pdf page to image.
            file_name = convert_from_path(
                self.pdf_path,
                output_folder=tmp_dir,
                paths_only=True,
                first_page=self.page_number,
                last_page=self.page_number + 1
            )[0]
            
            # Convert images to text.
            file_path = os.path.join(tmp_dir, file_name)
            text = str(image_to_string(Image.open(file_path)))
        
        return text
        
        
        
        
        
        