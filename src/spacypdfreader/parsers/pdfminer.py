from io import StringIO
from typing import Dict, Iterable, List

from pdfminer.converter import TextConverter
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

_PAGE_NUMBERS_ERROR = (
    "The `page_numbers` kwarg is not valid when using the pdfminer parser. "
    "Please use `page_range` instead. For example: ",
    "``",
)


def parser(pdf_path: str, page_number: int, **kwargs):
    """Convert PDFs to text using pdfminer.

    The pdfminer library is "pure python" library for converting PDF into text.
    pdfminer is relatively fast, but has low accuracy than other parsers such as
    [pytesseract](/parsers/#pytesseract).

    Parameters:
        pdf_path: Path to a PDF file.
        page_number: The page number of the PDF to convert from PDF to text. Must be one
            digit based indexing (e.g. the first page of the PDF is page 1, as
            opposed to page 0).
        **kwargs: `**kwargs` will be passed to
            [`pdfminer.high_level.extract_text`](https://pdfminersix.readthedocs.io/en/latest/reference/highlevel.html#extract-text).

    Returns:
        str: The PDF page as a string.

    Examples:
        pdfminer is the default PDF to text parser and will be automatically
        used unless otherwise specified.

        >>> import spacy
        >>> from spacypdfreader import pdf_reader
        >>>
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)

        To be more explicit import the parser and pass it into the
        `pdf_reader` function.

        >>> import spacy
        >>> from spacypdfreader import pdf_reader
        >>> from spacypdfreader.parsers.pdfminer import parser
        >>>
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, parser)

        For more fine tuning you can pass in additional parameters to pdfminer.

        >>> import spacy
        >>> from spacypdfreader import pdf_reader
        >>> from spacypdfreader.parsers.pdfminer import parser
        >>>
        >>> nlp = spacy.load("en_core_web_sm")
        >>> params = {"caching": False}
        >>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, parser, **params)

    Info:
        See the [pdfminer section](/parsers/#pdfminer) in the docs for more
        details on the implementation of pdfminer. For more details on pdfminer
        refer to the [pdfminer docs](https://pdfminersix.readthedocs.io/en/latest/).
    """
    # Check to see if the users has provided the `page_numbers` kwarg. This is not
    # valid. So raise an error. See: https://github.com/SamEdwardes/spacypdfreader/issues/16
    if "page_numbers" in kwargs:
        raise ValueError(*_PAGE_NUMBERS_ERROR)

    # pdfminer uses zero indexed page numbers. Therefore need to remove 1
    # from the page count.
    page_number -= 1
    text = extract_text(pdf_path, page_numbers=[page_number], **kwargs)
    return text


def batch_parser(pdf_path: str, pages: Iterable[int], **kwargs) -> List[str]:
    """Convert several PDF pages to text in a single pass with pdfminer.

    Calling [`parser`][spacypdfreader.parsers.pdfminer.parser] once per page
    re-opens and re-parses the entire PDF every time, which is roughly O(n^2)
    work for an n page document. `batch_parser` parses the document a single
    time and returns the text for each requested page. The output for a given
    page is identical to calling `parser` for that page.

    `spacypdfreader.pdf_reader` uses this automatically when the pdfminer
    parser is selected (it is attached as `parser.batch_parser`).

    Parameters:
        pdf_path: Path to a PDF file.
        pages: One indexed page numbers to convert (e.g. the first page of the
            PDF is page 1, as opposed to page 0).
        **kwargs: `**kwargs` will be passed to
            [`pdfminer.high_level.extract_text`](https://pdfminersix.readthedocs.io/en/latest/reference/highlevel.html#extract-text)
            (for example `password`, `caching`, `codec`, `maxpages` or
            `laparams`).

    Returns:
        A list of strings, one per page, in the same order as `pages`.
    """
    if "page_numbers" in kwargs:
        raise ValueError(*_PAGE_NUMBERS_ERROR)

    # pdfminer uses zero indexed page numbers.
    zero_indexed = [page - 1 for page in pages]
    text_by_page = _extract_text_per_page(pdf_path, zero_indexed, **kwargs)
    return [text_by_page[page] for page in zero_indexed]


def _extract_text_per_page(
    pdf_path: str,
    page_numbers: Iterable[int],
    password: str = "",
    maxpages: int = 0,
    caching: bool = True,
    codec: str = "utf-8",
    laparams: LAParams = None,
) -> Dict[int, str]:
    """Extract text from the requested (zero indexed) pages in a single pass.

    This mirrors `pdfminer.high_level.extract_text` but opens and parses the
    document only once, capturing the text for each requested page separately.
    """
    if laparams is None:
        laparams = LAParams()

    # `PDFPage.get_pages` yields the requested pages in document order, so pair
    # the yielded pages with the sorted, de-duplicated page numbers.
    requested = sorted(set(page_numbers))
    text_by_page: Dict[int, str] = {}

    with open(pdf_path, "rb") as in_file:
        rsrcmgr = PDFResourceManager(caching=caching)
        pdf_pages = PDFPage.get_pages(
            in_file,
            requested,
            maxpages=maxpages,
            password=password,
            caching=caching,
        )
        for page_number, page in zip(requested, pdf_pages):
            with StringIO() as output:
                device = TextConverter(
                    rsrcmgr, output, codec=codec, laparams=laparams
                )
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                interpreter.process_page(page)
                text_by_page[page_number] = output.getvalue()
                device.close()

    return text_by_page


# Expose the single-pass extractor on the per-page parser so that
# `spacypdfreader.pdf_reader` can discover and prefer it.
parser.batch_parser = batch_parser


class PdfminerParser:
    """This class has bee included for backwards compatibility. Do not use."""

    def __init__(self):
        return None
