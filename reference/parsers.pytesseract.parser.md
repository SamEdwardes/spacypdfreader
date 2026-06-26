## parsers.pytesseract.parser()


Convert a single PDF page to text using pytesseract.


Usage

``` python
parsers.pytesseract.parser(
    pdf_path,
    page_number,
    **kwargs,
)
```


The pytesseract library has the highest accuracy of all the PDF to text parsers included in spacypdfreader. It takes a different approach than other parsers. It first converts the PDF to an image, then runs an OCR engine on the image to extract the text. pytesseract results in the best quality but can be very slow compared to other parsers.


## Parameters


`pdf_path: str`  
Path to a PDF file.

`page_number: int`  
The page number of the PDF to convert from PDF to text. Must be one digit based indexing (e.g. the first page of the PDF is page 1, as opposed to page 0).

`**kwargs`  
`**kwargs` will be passed to [`pytesseract.image_to_string`](https://github.com/madmaze/pytesseract/blob/8fe7cd1faf4abc0946cb69813d535198772dbb6c/pytesseract/pytesseract.py#L409-L426).


## Returns


`str`  
The PDF page as a string.


## Examples

To use pytesseract it must be explicitly imported and passed into the [pdf_reader](spacypdfreader.pdf_reader.md#spacypdfreader.spacypdfreader.pdf_reader) function.

``` python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>> from spacypdfreader.parsers.pytesseract import parser
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, parser)
```

For more fine tuning you can pass in additional parameters to pytesseract.

``` python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>> from spacypdfreader.parsers.pytesseract import parser
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> params = {"nice": 1}
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, parser, **params)
```


## Info

See the [pytesseract section](../parsers/#pytesseract) in the docs for more details on the implementation of pytesseract. For more details on pytesseract see the [pytesseract docs](https://github.com/madmaze/pytesseract).
