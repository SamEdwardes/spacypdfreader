## spacypdfreader.pdf_reader()


Convert a PDF document to a spaCy Doc object.


Usage

``` python
spacypdfreader.pdf_reader(
    pdf_path,
    nlp,
    pdf_parser=pdfminer.parser,
    verbose=False,
    n_processes=None,
    page_range=None,
    **kwargs
)
```


## Parameters


`pdf_path: str`  
Path to a PDF file.

`nlp: spacy.Language`  
A spaCy Language object with a loaded pipeline. For example `spacy.load("en_core_web_sm")`.

`pdf_parser: Callable = pdfminer.parser`    
The parser to convert PDF file to text. Read the docs for more details. Defaults to pdfminer.parser.

`verbose: bool = ``False`  
If True details will be printed to the terminal. By default, False.

`n_processes: Optional[int] = None`  
The number of process to use for multi-processing. If `None`, multi-processing will not be used.

`page_range: Optional[Iterable[int]] = None`  
The page range of the PDF to convert from PDF to text. Must be one digit based indexing (e.g. the first page of the PDF is page 1, as opposed to page 0). If `None` all pages will be converted.

`**kwargs: Any`  
Arbitrary keyword arguments to pass to the underlying functions that extract text from the PDFs. If using pdfminer (the default) `**kwargs` will be passed to [`pdfminer.high_level.extract_text`](https://pdfminersix.readthedocs.io/en/latest/reference/highlevel.html#extract-text). If using [spacypdfreader.parsers.pytesseract.parser](parsers.pytesseract.parser.md#spacypdfreader.parsers.pytesseract.parser) `**kwargs` will be passed to [`pytesseract.image_to_string`](https://github.com/madmaze/pytesseract/blob/8fe7cd1faf4abc0946cb69813d535198772dbb6c/pytesseract/pytesseract.py#L409-L426).


## Returns


`spacy.tokens.Doc`  
A spacy Doc object with the custom extensions.


## Examples

By default pdfminer is used to extract text from the PDF.

``` python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
```

To be more explicit import [pdfminer.parser](parsers.pdfminer.parser.md#spacypdfreader.parsers.pdfminer.parser) and pass it into the [pdf_reader](spacypdfreader.pdf_reader.md#spacypdfreader.spacypdfreader.pdf_reader) function.

``` python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>> from spacypdfreader.parsers import pdfminer
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pdfminer.parser)
```

Alternative parsers can be used as well such as pytesseract.

``` python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>> from spacypdfreader.parsers import pytesseract
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pytesseract.parser)
```

For more fine tuning you can pass in additional parameters to pytesseract.

``` python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>> from spacypdfreader.parsers import pytesseract
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> params = {"nice": 1}
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pytesseract.parser, **params)
```

You can speed up spacypdfreader by using multiple processes.

``` python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>> from spacypdfreader.parsers import pytesseract
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pytesseract.parser, n_processes=4)
```

To extract a specific range of pages, use the `page_range` argument.

``` python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>> from spacypdfreader.parsers import pytesseract
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pytesseract.parser, n_processes=4, page_range=(2, 3))
```
