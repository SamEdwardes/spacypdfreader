# Reference


## Functions


The main entry point for converting a PDF into a spaCy Doc.


[spacypdfreader.pdf_reader()](spacypdfreader.pdf_reader.md#spacypdfreader.spacypdfreader.pdf_reader)  
Convert a PDF document to a spaCy Doc object.


## Parsers


Built-in PDF-to-text parsers. Pass one of these to the `pdf_parser` argument of `pdf_reader`, or bring your own.


[parsers.pdfminer.parser()](parsers.pdfminer.parser.md#spacypdfreader.parsers.pdfminer.parser)  
Convert PDFs to text using pdfminer.

[parsers.pytesseract.parser()](parsers.pytesseract.parser.md#spacypdfreader.parsers.pytesseract.parser)  
Convert a single PDF page to text using pytesseract.
