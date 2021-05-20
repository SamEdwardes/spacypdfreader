# spaCyPDFreader

Extract text from pdfs using spaCy and capture the page number as a spacy extension.

## Installation

```bash
pip install spacypdfreader
```

## Usage


```python
import spacy
from spacypdfreader import pdf_reader

nlp = spacy.load("en_core_web_sm")
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Extracting text from <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span> pdf pages<span style="color: #808000; text-decoration-color: #808000">...</span>
</pre>



    100%|██████████| 4/4 [00:00<00:00,  5.97it/s]



```python
doc[0:10]
```




    Test PDF 01
    
    This is a simple test pdf




```python
for token in doc[0:10]:
    print(f"Token: `{token}`, page number  {token._.page_number}")
```

    Token: `Test`, page number  1
    Token: `PDF`, page number  1
    Token: `01`, page number  1
    Token: `
    
    `, page number  1
    Token: `This`, page number  1
    Token: `is`, page number  1
    Token: `a`, page number  1
    Token: `simple`, page number  1
    Token: `test`, page number  1
    Token: `pdf`, page number  1



```python
doc[-10:]
```




    U3D or PRC and various other data formats.[15][16][17]
    





```python
for token in doc[-10:]:
    print(f"Token: `{token}`, page number  {token._.page_number}")
```

    Token: `U3D`, page number  4
    Token: `or`, page number  4
    Token: `PRC`, page number  4
    Token: `and`, page number  4
    Token: `various`, page number  4
    Token: `other`, page number  4
    Token: `data`, page number  4
    Token: `formats.[15][16][17`, page number  4
    Token: `]`, page number  4
    Token: `
    
    `, page number  4

