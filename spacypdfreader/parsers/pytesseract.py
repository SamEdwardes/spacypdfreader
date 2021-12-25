"""
Convert pdf to text using the pytesseract library.


"""

import os
import tempfile

from pdf2image import convert_from_path
from PIL import Image

from pytesseract import image_to_string

from .base import BaseParser


class PytesseractParser(BaseParser):
    """Convert PDFs to text using pytesseract.
    
    The pytesseract library has the highest accuracy of all the PDF to text
    parsers included in spacypdfreader. It takes a different approach than other
    parsers. It first converts the PDF to an image, then runs an OCR engine on
    the image to extract the text. pytesseract results in the best quality but
    can be very slow compared to other parsers.
    
    See the [pytesseract](/parsers/#pytesseract) section in the docs for more
    details.
    
    Args:
        **kwargs: Arbitrary keyword arguments.
        
    Reference:
        - https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/
    """
    name: str = "pytesseract"
    
    def pdf_to_text(self, **kwargs) -> str:
        """Convert a PDF page to text.
        
        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            A string respresentation of the PDf page.
        """        
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
            text = str(image_to_string(Image.open(file_path), **kwargs))
        
        return text
        
        
        
        
        
        