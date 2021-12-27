# Parsers

Extracting text from PDF documents can be challenging. There are several different options in the python ecosystem. *spacypdfreader* makes it easy to extract text from PDF documents. At this time *spacypdfreader* has built in support for two options:

- *pdfminer*: the default option ([GitHub]() | [PyPi]() | [Docs]())
- *pytesseract*: alternative option ([GitHub]() | [PyPi]() | [Docs]())

You can also bring your own custom PDF to text parser to use in *spacypdfreader*.

>  💁‍♂️ Would you like to see another parser added? Please submit an issue on [GitHub](https://github.com/SamEdwardes/spaCyPDFreader) and the maintainer will look into adding support.

## Comparison of built in parsers

All PDF to text parsers have their tradeoffs. The table below summaries the pros and cons of the built in parsers.

|              | *pdfminer*                                                   | *pytesseract*                                                |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| When to use  | ⚡️ When speed is more important than accuracy.                | 🎓 When accuracy is more important than speed.                |
| Accuracy     | 👌**Medium:** from my experience *pdfminer* struggles with documents where the text is in one or more columns. | 👍 **High:** very good. Performs well on messy documents (e.g hand written text, pdfs with multiple columns of text on a single page). |
| Speed        | 👌 **Medium:** the text extraction is not instant, but it does not take forever. | 👎 **Slow:** the text extraction is very slow and will take hours on hundres of pages. |
| Installation | 👍 **Easy:** pure python, if you have installed *spacypdfreader* you already have everything you need. | 👎 **Complicated:** relies on additional non-python dependencies that can be complicated for beginners to install. |
| How it works | Text is extracted directly from PDF using only Python.       | Each pdf page is converted into an image. Optical character recognition is then run on each image. |

## *pdfminer*

A pure Python library for extracting text from PDFs.

**Installation** 

No action required, *pdfminer* will automatically be installed when you install *spacypdfreader*.

**Usage**

*pdfminer* is the default PDF to text extraction parser for *spacypdfreader*:

```python
import spacy
from spacypdfreader import pdf_reader

nlp = spacy.load("en_core_web_sm")
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
```

You could also be more verbose and pass in aditional parameters. For a list of availble parameters please refer to the pdfminer documentation for the [`extract_function`](https://pdfminersix.readthedocs.io/en/latest/reference/highlevel.html#extract-text) function.

```python
import spacy
from spacypdfreader import pdf_reader
from spacypdfreader.parsers.pdfminer import PdfminerParser

nlp = spacy.load("en_core_web_sm")
params = {
		"caching": False
}
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, PdfminerParser)
```

## *pytesseract*

A PDf to text extraction engine that uses Googles *tesseract* OCR engine.

**Installation**

You can install most of the dependencies by pip installing *spacypdfreader* with some optional dependencies:

```bash
pip install 'spacypdfreader[pytesseract]'
```

Unfortunately this will not always install all of the depencies because some of them are non-python related. I find that installing pytesseract can be a little bit tricky for beginners. I will not go into detail here, but will instead provide a few links I have found helpful:

- []()
- []()

**Usage**

To use *pytesseract* you must pass the *pytesseract* parser into the `pdf_parser` argument. For a list of available parameters you can pass in refer the documentation for the [`image_to_string`](https://github.com/madmaze/pytesseract) function from *pytesseract*.

```python
import spacy
from spacypdfreader import pdf_reader
from spacypdfreader.parsers.pytesseract import PytesseractParser

nlp = spacy.load("en_core_web_sm")
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, PytesseractParser)
```

## Bring your own parser

*spacypdfreader* allows your to bring your custom PDF parser. *pypdf2* ([GitHub]() | [PyPi]() | [Docs]()) is a library that is currently not supported. However, you can still use it with *spacypdfreader*. The only requirement is that the parser must have a way for you to specify which page of the PDF document you would like to extract.

The code below demonstrates how you could implement  *pypdf2* with only a few lines of code.

```python
import spacy
from spacypdfreader import pdf_reader
from spacypdfreader.parsers.base import BaseParser

class Parser(BaseParser):
		name: str = "pypdf2"
    
    def pdf_to_text(self, **kwargs):
      	text = do_this()
        return text

nlp = spacy.load("en_core_web_sm")
pdf_path = "tests/data/test_pdf_01.pdf"
doc = pdf_reader(pdf_path, nlp, Parser)

```

How does it work?

- `BaseParser` is the base class that all parsers inherit from in *spacypdfreader*.
- Create a new class that inherits from the `BaseParser` class. This new class must have:
    - A `name` attribute.
    - A method called `pdf_to_text`. This method should only convert one pdf page at a time.

> ⚠️ *spacypdfreader* uses "1 based indexing". The first page of the PDF is considered page 1, as opposed to page 0.

For reference please refer to:

- [spacypdfreader/parsers/pdfminer.py](): example of how `BaseParser` was used to enable *pdfminer*. Note that *pdfminer* uses 0 based indexing, so the `pdf_to_text` method needs to adjust accordingly.
- [spacypdfreader/parsers/pytesseract.py]() example of how `BaseParser` was used to enable *pytesseract*.

