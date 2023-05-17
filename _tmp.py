from rich import inspect
from spacypdfreader.parsers import pytesseract, pdfminer

x = pdfminer.PdfminerParser("hello", "1")
inspect(x, all=True)