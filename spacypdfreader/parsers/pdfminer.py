from pdfminer.high_level import extract_text


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
    # pdfminer uses zero indexed page numbers. Therefore need to remove 1
    # from the page count.
    page_number -= 1
    text = extract_text(pdf_path, page_numbers=[page_number], **kwargs)
    return text


class PdfminerParser:
    """This class has bee included for backwards compatibility. Do not use."""
    def __init__(self):
        return None