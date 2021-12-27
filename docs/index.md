# spacypdfreader

Easy PDF to text to *spaCy* text extraction in Python.

<p>
    <a href="https://pypi.org/project/spacypdfreader" target="_blank"><img src="https://img.shields.io/pypi/v/spacypdfreader?color=%2334D058&label=pypi%20package" alt="Package version"></a>
</p>

<hr></hr>

**Documentation:** [https://spacypdfreader.netlify.app](https://spacypdfreader.netlify.app)

**Source code:** [https://github.com/SamEdwardes/spaCyPDFreader](https://github.com/SamEdwardes/spaCyPDFreader)

**PyPi:** [https://pypi.org/project/spacypdfreader/](https://pypi.org/project/spacypdfreader/)

<hr></hr>

*spacypdfreader* is a python library for extracting text from PDF documents into *spaCy* `Doc` objects. When you use *spacypdfreader* each token is annotated with PDF page number which it was extracted from.

The key features are:

- **PDF to spaCy Doc object:** Convert a PDF document directly into a *spaCy* `Doc` object.
- **Token._.page_number:** Each *spaCy* token will be annotated with the PDF page number from which it was extracted (`token._.page_number`).
- **Multiple parsers:** Select between multiple built in PDF to text parsers or bring your own PDF to text parser.

## Installation

Install *spacypdfreader* using pip:

```bash
pip install spacypdfreader
```

To install with the required pytesseract dependencies:

```bash
pip install 'spacypdfreader[pytesseract]'
```

## Usage

```python
import spacy
from spacypdfreader import pdf_reader

nlp = spacy.load("en_core_web_sm")
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
print(doc[0]._.page_number)  # 1
print(doc[-1]._.page_number) # 4
```

## What is *spaCy*?

*spaCy* is a natural language processing (NLP) tool. It can be used to perform a variety of NLP tasks. For more information check out the excellent documentation at [https://spacy.io](https://spacy.io).

## Implementation Notes

spaCyPDFreader behaves a little bit different than your typical [spaCy custom component](https://spacy.io/usage/processing-pipelines#custom-components). Typically a spaCy component should receive and return a `spacy.tokens.Doc` object.

spaCyPDFreader breaks this convention because the text must first be extracted from the PDF. Instead `pdf_reader` takes a path to a PDF file and a `spacy.Language` object as parameters and returns a `spacy.tokens.Doc` object. This allows users an easy way to extract text from PDF files while still allowing them use and customize all of the features spacy has to offer by allowing you to pass in the `spacy.Language` object.

Example of a "traditional" spaCy pipeline component [negspaCy](https://spacy.io/universe/project/negspacy):

```python
import spacy
from negspacy.negation import Negex

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("negex", config={"ent_types":["PERSON","ORG"]})
doc = nlp("She does not like Steve Jobs but likes Apple products.")
```

Example of `spaCyPDFreader` usage:

```python
import spacy
from spacypdfreader import pdf_reader
nlp = spacy.load("en_core_web_sm")

doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
```

Note that the `nlp.add_pipe` is not used by spaCyPDFreader.