## parsers.pdfminer.parser()


Convert PDFs to text using pdfminer.


Usage

``` python
parsers.pdfminer.parser(
    pdf_path,
    page_number,
    **kwargs,
)
```


The pdfminer library is "pure python" library for converting PDF into text. pdfminer is relatively fast, but has low accuracy than other parsers such as [pytesseract](../parsers/#pytesseract).


## Parameters


`pdf_path: str`  
Path to a PDF file.

`page_number: int`  
The page number of the PDF to convert from PDF to text. Must be one digit based indexing (e.g. the first page of the PDF is page 1, as opposed to page 0).

`**kwargs`  
`**kwargs` will be passed to [`pdfminer.high_level.extract_text`](https://pdfminersix.readthedocs.io/en/latest/reference/highlevel.html#extract-text).


## Returns


`str`  
The PDF page as a string.


## Examples

pdfminer is the default PDF to text parser and will be automatically used unless otherwise specified.

``` python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
```

To be more explicit import the parser and pass it into the [pdf_reader](spacypdfreader.pdf_reader.md#spacypdfreader.spacypdfreader.pdf_reader) function.

``` python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>> from spacypdfreader.parsers.pdfminer import parser
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, parser)
```

For more fine tuning you can pass in additional parameters to pdfminer.

``` python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>> from spacypdfreader.parsers.pdfminer import parser
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> params = {"caching": False}
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, parser, **params)
```


## Info

See the [pdfminer section](../parsers/#pdfminer) in the docs for more details on the implementation of pdfminer. For more details on pdfminer refer to the [pdfminer docs](https://pdfminersix.readthedocs.io/en/latest/).
