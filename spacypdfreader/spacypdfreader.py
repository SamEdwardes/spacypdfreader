import os
import warnings
from functools import partial
from multiprocessing.pool import ThreadPool as Pool
from typing import Any, Callable, Iterable, Optional

import spacy
from spacy.tokens import Doc, Token

from ._utils import _filter_doc_by_page, _get_number_of_pages
from .console import console
from .parsers import pdfminer, pytesseract

# Set up the spacy custom extensions.

if not Token.has_extension("page_number"):
    Token.set_extension("page_number", default=None)

if not Doc.has_extension("pdf_file_name"):
    Doc.set_extension("pdf_file_name", default=None)

if not Doc.has_extension("page"):
    Doc.set_extension("page", method=_filter_doc_by_page)

if not Doc.has_extension("first_page"):
    Doc.set_extension("first_page", getter=lambda doc: doc[0]._.page_number)

if not Doc.has_extension("last_page"):
    Doc.set_extension("last_page", getter=lambda doc: doc[-1]._.page_number)

if not Doc.has_extension("page_range"):
    Doc.set_extension(
        "page_range", getter=lambda doc: (doc._.first_page, doc._.last_page)
    )


def pdf_reader(
    pdf_path: str,
    nlp: spacy.Language,
    pdf_parser: Callable = pdfminer.parser,
    verbose: bool = False,
    n_processes: Optional[int] = None,
    page_range: Optional[Iterable[int]] = None,
    **kwargs: Any,
) -> spacy.tokens.Doc:
    """Convert a PDF document to a spaCy Doc object.

    Args:
        pdf_path: Path to a PDF file.
        nlp: A spaCy Language object with a loaded pipeline. For example
            `spacy.load("en_core_web_sm")`.
        pdf_parser: The parser to convert PDF file to text. Read the docs for
            more details. Defaults to pdfminer.parser.
        verbose: If True details will be printed to the terminal. By default,
            False.
        n_processes: The number of process to use for multi-processing. If `None`,
            multi-processing will not be used.
        page_range: The page range of the PDF to convert from PDF to text. Must be
            one digit based indexing (e.g. the first page of the PDF is page 1, as
            opposed to page 0). If `None` all pages will be converted.
        **kwargs: Arbitrary keyword arguments to pass to the underlying functions
            that extract text from the PDFs. If using pdfminer (the default)
            `**kwargs` will be passed to
            [`pdfminer.high_level.extract_text`](https://pdfminersix.readthedocs.io/en/latest/reference/highlevel.html#extract-text). If using
            `spacypdfreader.parsers.pytesseract.parser` `**kwargs` will
            be passed to
            [`pytesseract.image_to_string`](https://github.com/madmaze/pytesseract/blob/8fe7cd1faf4abc0946cb69813d535198772dbb6c/pytesseract/pytesseract.py#L409-L426).

    Returns:
        A spacy Doc object with the custom extensions.

    Examples:
        By default pdfminer is used to extract text from the PDF.

        >>> import spacy
        >>> from spacypdfreader import pdf_reader
        >>>
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)

        To be more explicit import `pdfminer.parser` and pass it into the
        `pdf_reader` function.

        >>> import spacy
        >>> from spacypdfreader import pdf_reader
        >>> from spacypdfreader.parsers import pdfminer
        >>>
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pdfminer.parser)

        Alternative parsers can be used as well such as pytesseract.

        >>> import spacy
        >>> from spacypdfreader import pdf_reader
        >>> from spacypdfreader.parsers import pytesseract
        >>>
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pytesseract.parser)

        For more fine tuning you can pass in additional parameters to
        pytesseract.

        >>> import spacy
        >>> from spacypdfreader import pdf_reader
        >>> from spacypdfreader.parsers import pytesseract
        >>>
        >>> nlp = spacy.load("en_core_web_sm")
        >>> params = {"nice": 1}
        >>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pytesseract.parser, **params)

        You can speed up spacypdfreader by using multiple processes.

        >>> import spacy
        >>> from spacypdfreader import pdf_reader
        >>> from spacypdfreader.parsers import pytesseract
        >>>
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pytesseract.parser, n_processes=4)

        To extract a specific range of pages, use the `page_range` argument.

        >>> import spacy
        >>> from spacypdfreader import pdf_reader
        >>> from spacypdfreader.parsers import pytesseract
        >>>
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pytesseract.parser, n_processes=4, page_range=(1, 2))
    """
    # For backwards compatibility, if someone passes in PdfMinerParser or
    # PyTesseractParser replace with the correct function
    if pdf_parser.__name__ == "PdfminerParser":
        warnings.warn(
            "`spacypdfreader.parser.pdfminer.PdfminerParser` has been depreciated "
            "in favour of `spacypdfreader.parser.pdfminer.parser`. Please use "
            "`spacypdfreader.parser.pdfminer.parser` in the future.",
            DeprecationWarning,
            stacklevel=2,
        )
        pdf_parser = pdfminer.parser
    elif pdf_parser.__name__ == "PytesseractParser":
        warnings.warn(
            "`spacypdfreader.parser.pdfminer.PytesseractParser` has been depreciated "
            "in favour of `spacypdfreader.parser.pytesseract.parser`. Please use "
            "`spacypdfreader.parser.pytesseract.parser` in the future.",
            DeprecationWarning,
            stacklevel=2,
        )
        pdf_parser = pytesseract.parser

    if verbose:
        console.print(
            f"PDF to text engine: [blue bold]{pdf_parser.__module__}.{pdf_parser.__name__}[/]..."
        )

    pdf_path = os.path.normpath(pdf_path)
    num_pages = _get_number_of_pages(pdf_path)

    # Get page range:
    if page_range:
        start_page, end_page = page_range
    else:
        start_page = 1
        end_page = num_pages

    # Validate the page_range argument.
    if start_page > end_page:
        raise ValueError("The start page must be less than or equal to the end page.")
    elif start_page < 1:
        raise ValueError("The start page must be greater than or equal to 1.")
    elif end_page > num_pages:
        raise ValueError(f"The end page must be less than or equal to the number of pages in the PDF ({num_pages}).")

    if verbose:
        console.print(f"PDF contains {num_pages} pages.")
        console.print(f"Extracting text from {start_page} to {end_page}...")

    # Handle multiprocessing
    if n_processes:
        with Pool(n_processes) as p:
            partial_worker = partial(pdf_parser, pdf_path, **kwargs)
            args = list(range(start_page, end_page + 1))
            texts = p.map(partial_worker, args)

    # Handle non-multiprocessing
    else:
        texts = []
        for page_num in range(start_page, end_page + 1):
            text = pdf_parser(pdf_path=pdf_path, page_number=page_num, **kwargs)
            texts.append(text)

    # Convert text to spaCy Doc objects.
    if verbose:
        console.print("Converting text to [blue bold]spaCy[/] Doc...")

    docs = [doc for doc in nlp.pipe(texts)]
    for idx, doc in enumerate(docs):
        page_num = idx + start_page
        for token in doc:
            token._.page_number = page_num

    combined_doc = Doc.from_docs(docs)
    combined_doc._.pdf_file_name = pdf_path

    if verbose:
        console.print(":white_check_mark: [green]Complete!")

    return combined_doc
