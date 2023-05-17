import tempfile
from pathlib import Path

from pdf2image import convert_from_path
from PIL import Image
from pytesseract import image_to_string
from pathlib import Path


def parser(pdf_path: str, page_number: int, **kwargs):
    """Convert a single PDF page to text using pytesseract.

    The pytesseract library has the highest accuracy of all the PDF to text
    parsers included in spacypdfreader. It takes a different approach than other
    parsers. It first converts the PDF to an image, then runs an OCR engine on
    the image to extract the text. pytesseract results in the best quality but
    can be very slow compared to other parsers.

    Parameters:
        pdf_path: Path to a PDF file.
        page_number: The page number of the PDF to convert from PDF to text. Must be one 
            digit based indexing (e.g. the first page of the PDF is page 1, as 
            opposed to page 0).
        **kwargs: `**kwargs` will be passed to 
            [`pytesseract.image_to_string`](https://github.com/madmaze/pytesseract/blob/8fe7cd1faf4abc0946cb69813d535198772dbb6c/pytesseract/pytesseract.py#L409-L426).

    Returns:
        str: The PDF page as a string.

    Examples:
        To use pytesseract it must be explicitly imported and passed
        into the `pdf_reader` function.

        >>> import spacy
        >>> from spacypdfreader import pdf_reader
        >>> from spacypdfreader.parsers.pytesseract import parser
        >>>
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, parser)

        For more fine tuning you can pass in additional parameters to
        pytesseract.

        >>> import spacy
        >>> from spacypdfreader import pdf_reader
        >>> from spacypdfreader.parsers.pytesseract import parser
        >>>
        >>> nlp = spacy.load("en_core_web_sm")
        >>> params = {"nice": 1}
        >>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, parser, **params)

    Info:
        See the [pytesseract section](/parsers/#pytesseract) in the docs for
        more details on the implementation of pytesseract. For more details on
        pytesseract see the [pytesseract docs](https://github.com/madmaze/pytesseract).
    """
     
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Convert pdf page to image.
        file_name = convert_from_path(
            pdf_path=pdf_path,
            output_folder=tmp_dir,
            paths_only=True,
            first_page=page_number,
            last_page=page_number + 1,
        )[0]

        # Convert images to text.
        file_path = Path(tmp_dir, str(file_name))
        text = str(image_to_string(Image.open(file_path), **kwargs))

    return text

class PytesseractParser:
    """This class has bee included for backwards compatibility. Do not use."""
    def __init__(self):
        return None