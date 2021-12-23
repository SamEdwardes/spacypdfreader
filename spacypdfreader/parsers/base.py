from typing import Dict


class BaseParser:
    """
    Base parser class. ...
    """
    name: str = "base"
    
    def __init__(self, pdf_path: str, page_number: int) -> None:
        self.pdf_path = pdf_path
        self.page_number = page_number
    