from spacypdfreader import __version__
from spacypdfreader._utils import _get_number_of_pages


def test_version():
    assert __version__ == "0.3.2"


def test_get_number_of_pages():
    assert _get_number_of_pages("tests/data/wikipedia.pdf") == 18
    assert _get_number_of_pages("tests/data/test_pdf_01.pdf") == 4
