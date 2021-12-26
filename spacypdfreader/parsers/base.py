class BaseParser:
    """The base parser class.

    The `BaseParser` is used to extend spacypdfreader with additional PDF to
    text parsers. See [Parsers](/parsers) in the documentation for additional
    details.

    Args:
        pdf_path: Path to a PDF file.
        page_number: The page number of the PDF to convert from PDF to text.
            Must be one digit based indexing (e.g. the first page of the PDF is
            page 1, as opposed to page 0).

    Attributes:
        name: A string name representation of the class. Will only be used for
            information purposes by being printed to the terminal when running.
        pdf_path: Path to a PDF file.
        page_number: The page number of the PDF to convert from PDF to text.
            Must be one digit based indexing (e.g. the first page of the PDF is
            page 1, as opposed to page 0).

    """

    name: str = "base"

    def __init__(self, pdf_path: str, page_number: int) -> None:
        self.pdf_path = pdf_path
        self.page_number = page_number
