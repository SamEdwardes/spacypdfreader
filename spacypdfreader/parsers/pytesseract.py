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

    Refer to [spacypdfreader.parsers.base.BaseParser][] for a list of attributes
    and the `__init__` method.

    Examples:
        `PdfminerParser` is the default PDF to text parser and will be
        automatically used unless otherwise specificied.

        >>> import spacy
        >>> from spacypdfreader import pdf_reader
        >>>
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)

        To be more explicit import `PdfminerParser` and pass it into the
        `pdf_reader` function.

        >>> import spacy
        >>> from spacypdfreader import pdf_reader
        >>> from spacypdfreader.parsers.pdfminer import PdfminerParser
        >>>
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, PdfminerParser)

        For more fine tuning you can pass in additional parameters to pdfminer.

        >>> import spacy
        >>> from spacypdfreader import pdf_reader
        >>> from spacypdfreader.parsers.pdfminer import PdfminerParser
        >>>
        >>> nlp = spacy.load("en_core_web_sm")
        >>> params = {"caching": False}
        >>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, PdfminerParser, **params)

    Info:
        See the [pytesseract section](/parsers/#pytesseract) in the docs for
        more details on the implementation of pytesseract. For more details on
        pytesseract see the
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
