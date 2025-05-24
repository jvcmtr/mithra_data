from dataclasses import dataclass
from typing import List, Union

@dataclass
class Doc:
    linkId: str
    type: str
    text: str
    content: List['Doc']