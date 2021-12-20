from dataclasses import dataclass, field
from typing import Dict

@dataclass
class BaseParser:
    pdf_path: str
    page_number: int
    name: str = field(init=False)
    kwargs: Dict = field(default_factory=dict)