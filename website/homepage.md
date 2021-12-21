# spacypdfreader

Easy PDF to text to *spaCy` text extraction in Python.

<hr></hr>

**Documentation:** []()

**Source code:** [https://github.com/SamEdwardes/spaCyPDFreader](https://github.com/SamEdwardes/spaCyPDFreader)

<hr></hr>

*spacypdfreader* is a python library for extracting text from PDF documents into *spaCy* `Doc` objects. When you use *spacypdfreader* each token is annotated with PDF page number which it was extractedf from.

The key features are:

- Convert a PDF document directly into a *spaCy* `Doc` object.
- Each *spaCy* token will be annotated with the PDF page number from which it was extracted (`token._.page_number`).
- Select between multiple built in PDF to text parsers.
- Bring your own PDF to text parser.

## What is *spaCy*?

*spaCy* is a natural language processing (NLP) tool. It can be used to perform a variety of NLP tasks. For more informaiton check out the excellent documentation at [spacy.io](spacy.io)

## Installation

## Example

```python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
>>> print(f"{doc[0]} -> page: {doc[0]._.page_number}")
Test -> page: 1
```

