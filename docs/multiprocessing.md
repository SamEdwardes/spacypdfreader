# Multiprocessing

As of version `0.3.0` spacypdfreader has built in support for multi-processing. This can dramatically improve the time it takes to convert a PDF to text.

## Usage

You can use multiprocessing with an parser.

**pdfminder**

```python
import spacy

from spacypdfreader.spacypdfreader import pdf_reader

nlp = spacy.load("en_core_web_sm")
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, n_processes=4)
```

**pytesseract**

```python
import spacy

from spacypdfreader.parsers import pytesseract
from spacypdfreader.spacypdfreader import pdf_reader

nlp = spacy.load("en_core_web_sm")
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp, pytesseract.parser, n_processes=4)
```

## Benchmark

```python
import time
from functools import wraps

import spacy

from spacypdfreader import pdf_reader
from spacypdfreader.parsers import pytesseract


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Took {end - start:.6f} seconds to complete")
        return result

    return wrapper


nlp = spacy.load("en_core_web_sm")
file_name = "tests/data/wikipedia.pdf"


@timeit
def bench(n_processes):
    doc = pdf_reader(file_name, nlp, pytesseract.parser, n_processes=n_processes)
    return doc


# With no multiprocessing
bench(None)
# Took 42.286371 seconds to complete

# With multiprocessing
bench(8)
# Took 9.051591 seconds to complete
```

