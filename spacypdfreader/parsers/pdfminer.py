from pdfminer.high_level import extract_text

from .base import BaseParser


class PdfminerParser(BaseParser):
    """Convert PDFs to text using pdfminer.

    The pdfminer library is "pure python" library for converting PDF into text.
    pdfminer is relatively fast, but has low accuracy than other parsers such as
    [pytesseract](/parsers/#pytesseract).

    See the [pdfminer section](/parsers/#pdfminer) in the docs for more
    details. For more details on pdfminer see the
    [pdfminer docs](https://pdfminersix.readthedocs.io/en/latest/).
    """

    name: str = "pdfminer"

    def pdf_to_text(self, **kwargs) -> str:
        """Convert a PDF page to text using the `extract_text` function from
        pdfminer.

        Args:
            **kwargs: Arbitrary keyword arguments. See the pdfminer docs for the
            [`extract_text`](https://pdfminersix.readthedocs.io/en/latest/reference/highlevel.html#extract-text)
            function for the available keywork arguments.

        Returns:
            A string respresentation of the PDf page.
        """
        # pdfminer uses zero indexed page numbers. Therefore need to remove 1
        # from the page count.
        self.page_number -= 1
        text = extract_text(self.pdf_path, page_numbers=[self.page_number], **kwargs)
        return text
