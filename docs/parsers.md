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
params = {"caching": False}
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, PdfminerParser, **params)
```

## *pytesseract*

A PDf to text extraction engine that uses Googles *tesseract* OCR engine.

**Installation**

You can install most of the dependencies by pip installing *spacypdfreader* with some optional dependencies:

```bash
pip install 'spacypdfreader[pytesseract]'
```

For pytesseract to work you have to install some additional tools. Installing pytesseract can be a little bit tricky for beginners. Please refer to [https://github.com/madmaze/pytesseract#installation](https://github.com/madmaze/pytesseract#installation) for details on how to install *pytesseract* if the above does not work.

### Linux

```bash
sudo apt-get install poppler-utils
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```

### Mac

```bash
brew install poppler
brew install tesseract
```

### Windows

To install poppler see the instructions here [https://stackoverflow.com/a/53960829](https://stackoverflow.com/a/53960829).

Then install tesseract with:

```bash
scoop install tesseract
```

Or you can follow the instructions here to install tesseract using the windows installer: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki).

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

*spacypdfreader* allows your to bring your custom PDF parser. For examples of how to implement your own parser refer to:

- <https://github.com/SamEdwardes/spacypdfreader/blob/main/spacypdfreader/parsers/pdfminer.py>, or
- <https://github.com/SamEdwardes/spacypdfreader/blob/main/spacypdfreader/parsers/pytesseract.py>.

To work with spacypdfreader a parser must be a function that:

- Has an argument named `pdf_path`.
- Has an argument named `page_number`. This argument should use *1 based indexing*. E.g. the value 1 refers to the first page of the PDF.
- The function should return the text only for a single page of the PDF. This allows spacypdfreader to execute faster with multi-processing.

!!! warning
    Version `0.3.0` changed how parsers are implemented. If you have created a custom parser that works with an older version of spacypdfreader it will need to be reimplemented.