import spacy
from spacypdfreader import pdf_reader

nlp = spacy.load("en_core_web_sm")
doc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)
print(f"{doc[0]} -> page: {doc[0]._.page_number}")