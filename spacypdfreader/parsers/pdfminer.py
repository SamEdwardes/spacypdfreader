from pdfminer.high_level import extract_text

from .base import BaseParser
from typing import Any


class PdfminerParser(BaseParser):
    """Convert PDFs to text using pdfminer.

    The pdfminer library is "pure python" library for converting PDF into text.
    pdfminer is relatively fast, but has low accuracy than other parsers such as
    [pytesseract](/parsers/#pytesseract).

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
        See the [pdfminer section](/parsers/#pdfminer) in the docs for more
        details on the implementation of pdfminer. For more details on pdfminer
        refer to the
        [pdfminer docs](https://pdfminersix.readthedocs.io/en/latest/).
    """

    name: str = "pdfminer"

    def pdf_to_text(self, **kwargs: Any) -> str:
        """Convert a PDF page to text using the `extract_text` function from
        pdfminer.

        Args:
            **kwargs: Arbitrary keyword arguments. See the pdfminer docs for the
                [extract_text](https://pdfminersix.readthedocs.io/en/latest/reference/highlevel.html#extract-text)
                function for the available keywork arguments.

        Returns:
            A string respresentation of the PDF page.
        """
        # pdfminer uses zero indexed page numbers. Therefore need to remove 1
        # from the page count.
        self.page_number -= 1
        text = extract_text(self.pdf_path, page_numbers=[self.page_number], **kwargs)
        return text
