# spaCyPDFreader

Extract text from pdfs using spaCy and capture the page number as a spacy extension.

**Links**

- [GitHub](https://github.com/SamEdwardes/spaCyPDFreader)
- [PyPi](https://pypi.org/project/spacypdfreader/)

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [Implementation Notes](#implementation-notes)
- [API Reference](#api-reference)

## Installation

```bash
pip install spacypdfreader
```

## Usage

```python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
Extracting text from 4 pdf pages... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
```

Each token will now have an additional extension `._.page_number` that indcates the pdf page number the token came from.

```python
>>> [print(f"Token: `{token}`, page number  {token._.page_number}") for token in doc[0:3]]
Token: `Test`, page number  1
Token: `PDF`, page number  1
Token: `01`, page number  1
[None, None, None]
```

## Implementation Notes

spaCyPDFreader behaves a litte bit different than your typical [spaCy custom component](https://spacy.io/usage/processing-pipelines#custom-components). Typically a spaCy component should receive and return a `spacy.tokens.Doc` object.

spaCyPDFreader breaks this convention because the text must first be extracted from the PDF. Instead `pdf_reader` takes a path to a PDF file and a `spacy.Language` object as parameters and returns a `spacy.tokens.Doc` object. This allows users an easy way to extract text from PDF files while still allowing them use and customize all of the features spacy has to offer by allowing you to pass in the `spacy.Language` object.

Example of a "traditional" spaCy pipeline component [negspaCy](https://spacy.io/universe/project/negspacy):

```python
>>> import spacy
>>> from negspacy.negation import Negex
>>> 
>>> nlp = spacy.load("en_core_web_sm")
>>> nlp.add_pipe("negex", config={"ent_types":["PERSON","ORG"]})
>>> 
>>> doc = nlp("She does not like Steve Jobs but likes Apple products.")
```

Example of `spaCyPDFreader` usage:

```python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
Extracting text from 4 pdf pages... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
```

Note that the `nlp.add_pipe` is not used by spaCyPDFreader.

## API Reference

### spacypdfreader.pdf_reader

Extract text from PDF files directly into a `spacy.Doc` object while capturing the page number of each token.


| Name        | Type               | Description                                                                                |
| ------------- | -------------------- | -------------------------------------------------------------------------------------------- |
| `pdf_path`  | `str`              | Path to a PDF file.                                                                        |
| `nlp`       | `spacy.Language`   | A spaCy Language object with a loaded pipeline. For example`spacy.load("en_core_web_sm")`. |
| **RETURNS** | `spacy.tokens.Doc` | A spacy Doc object with the custom extension`._.page_number`.                              |

When using `spacypdfreader.pdf_reader` a `spacy.tokens.Doc` object with custom extensions is returned.


| Extension   | Type   | Description   | Default   |
| ------ | ------ | ------ | ------ |
| token._.page_number |  int      | The PDF page number in which the token was extracted from. The first page is `1`.      |  `None`      |

**Example**

```python
>>> import spacy
>>> from spacypdfreader import pdf_reader
>>>
>>> nlp = spacy.load("en_core_web_sm")
>>> doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
Extracting text from 4 pdf pages... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
```

Each token will now have an additional extension `._.page_number` that indcates the pdf page number the token came from.

```python
>>> [print(f"Token: `{token}`, page number  {token._.page_number}") for token in doc[0:3]]
Token: `Test`, page number  1
Token: `PDF`, page number  1
Token: `01`, page number  1
[None, None, None]
```

