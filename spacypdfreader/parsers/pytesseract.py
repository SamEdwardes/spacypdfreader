import os
import tempfile
from typing import Any

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

    See the [pytesseract section](/parsers/#pytesseract) in the docs for more
    details. For more details on pytesseract see the
    [pytesseract docs](https://github.com/madmaze/pytesseract).
    """

    name: str = "pytesseract"

    def pdf_to_text(self, **kwargs: Any) -> str:
        """Convert a PDF page to text using the `image_to_string` function from
        pytesseract.

        Args:
            **kwargs: Arbitrary keyword arguments. See the pytesseract docs for
                the [image_to_string](https://github.com/madmaze/pytesseract)
                function for the available keyword arguments.

        Returns:
            A string respresentation of the PDF page.
        """
        with tempfile.TemporaryDirectory() as tmp_dir:

            # Convert pdf page to image.
            file_name = convert_from_path(
                self.pdf_path,
                output_folder=tmp_dir,
                paths_only=True,
                first_page=self.page_number,
                last_page=self.page_number + 1,
            )[0]

            # Convert images to text.
            file_path = os.path.join(tmp_dir, file_name)
            text = str(image_to_string(Image.open(file_path), **kwargs))

        return text
