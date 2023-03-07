# Parsers

Extracting text from PDF documents can be challenging. There are several different options in the python ecosystem. *spacypdfreader* makes it easy to extract text from PDF documents. At this time *spacypdfreader* has built in support for two options:

- *pdfminer*: the default option ([GitHub](https://github.com/pdfminer/pdfminer.six) | [PyPi](https://pypi.org/project/pdfminer.six/) | [Docs](https://pdfminersix.readthedocs.io/en/latest/))
- *pytesseract*: alternative option ([GitHub](https://github.com/madmaze/pytesseract) | [PyPi](https://pypi.org/project/pytesseract/))

You can also bring your own custom PDF to text parser to use in *spacypdfreader*.

!!! tip

    💁‍♂️ Would you like to see another parser added? Please submit an issue on [GitHub](https://github.com/SamEdwardes/spaCyPDFreader/issues/new/choose) and the maintainer will look into adding support.

!!! tip

    Parsing big PDFs can be slow. For example, parsing a 166 page PDF document on an M1 mac took 166 seconds. If you are working with larger documents try breaking them into smaller documents and use multiprocessing.

## Comparison of built in parsers

All PDF to text parsers have their tradeoffs. The table below summaries the pros and cons of the built in parsers.

|              | *pdfminer*                                                   | *pytesseract*                                                |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| When to use  | ⚡️ When speed is more important than accuracy.                | 🎓 When accuracy is more important than speed.                |
| Accuracy     | 👌 **Medium:** from my experience *pdfminer* struggles with documents where the text is in one or more columns. | 👍 **High:** very good. Performs well on messy documents (e.g hand written text, PDFs with multiple columns of text on a single page). |
| Speed        | 👌 **Medium:** the text extraction is not instant, but it does not take forever. | 👎 **Slow:** the text extraction is very slow and will take hours on hundreds of pages. |
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

You could also be more verbose and pass in additional parameters. For a list of available parameters please refer to the pdfminer documentation for the [`extract_function`](https://pdfminersix.readthedocs.io/en/latest/reference/highlevel.html#extract-text) function.

```python
import spacy
from spacypdfreader import pdf_reader
from spacypdfreader.parsers.pdfminer import PdfminerParser

nlp = spacy.load("en_core_web_sm")
params = {
  "caching": False
}
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, PdfminerParser, **params)
```

## *pytesseract*

A PDf to text extraction engine that uses Googles *tesseract* OCR engine.

**Installation**

You can install most of the dependencies by pip installing *spacypdfreader* with some optional dependencies:

```bash
pip install 'spacypdfreader[pytesseract]'
```

Unfortunately this will not always install all of the dependencies because some of them are non-python related. I find that installing pytesseract can be a little bit tricky for beginners. Please refer to [https://github.com/madmaze/pytesseract#installation](https://github.com/madmaze/pytesseract#installation) for details on how to install *pytesseract* if the above does not work.

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

*spacypdfreader* allows your to bring your custom PDF parser. The only requirement is that the parser must have a way for you to specify which page of the PDF document you would like to extract.

The code below demonstrates the implementation of a new custom parser:

```python
from typing import Any

import spacy
from pdfminer.high_level import extract_text

from spacypdfreader import pdf_reader
from spacypdfreader.parsers.base import BaseParser # (1)


class CustomParser(BaseParser): # (2)
    name: str = "custom" # (3)

    def pdf_to_text(self, **kwargs: Any) -> str: # (4)
        # pdfminer uses zero indexed page numbers. Therefore need to remove 1
        # from the page count.
        self.page_number -= 1
        text = extract_text(self.pdf_path, page_numbers=[self.page_number], **kwargs)
        return text


nlp = spacy.load("en_core_web_sm")
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, CustomParser)
print(doc._.page_range)  # (1, 4)
```

1. `BaseParser` is the base class that all parsers inherit from in *spacypdfreader*.
2. When creating a new class it must inherit from the `BaseParser` class.
3. The new class must have a `name` attribute.
4. The new class must have a method called `pdf_to_text`. This method should only convert one pdf page at a time.


!!! note

    *spacypdfreader* uses "1 based indexing". The first page of the PDF is considered page 1, as opposed to page 0.