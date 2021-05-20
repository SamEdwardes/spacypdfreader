import os

import spacy
from pdfminer.high_level import extract_text
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from rich import inspect
from rich.console import Console
from rich.progress import track
from spacy.tokens import Doc, Token
from tqdm import tqdm

if not Token.has_extension("page_number"):
    Token.set_extension("page_number", default=None)

console = Console()


def get_number_of_pages(pdf_path: str) -> int:
    with open(os.path.normpath(pdf_path), 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        num_pages =  len(list(PDFPage.create_pages(doc)))
    return num_pages


def pdf_reader(pdf_path: str, nlp: spacy.Language) -> spacy.tokens.Doc:
    pdf_path = os.path.normpath(pdf_path)
    num_pages = get_number_of_pages(pdf_path)
    console.print(f"Extracting text from {num_pages} pdf pages...")
    
    texts = []
    for page_num in tqdm(range(num_pages)):
        text = extract_text(pdf_path, page_numbers=[page_num])
        texts.append(text)
        
    docs = [doc for doc in nlp.pipe(texts)]
    
    for idx, doc in enumerate(docs):
        page_num = idx + 1
        for token in doc:
            token._.page_number = page_num
            
    combined_doc = Doc.from_docs(docs)
    return combined_doc
