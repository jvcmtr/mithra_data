from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Union

@dataclass
class Doc:
    linkId: str
    type: str
    text: str
    content: List['Doc']  # Information bounded to the component
    children: List['Doc'] # Child Information
    

# class DocTypes(Enum):
#     MODULE = auto()
#     H1 = auto()
#     H2 = auto()
#     H3 = auto()
#     H4 = auto()
#     H5 = auto()
#     H6 = auto()
#     CALLOUT = auto()
#     CODE_BLOCK = auto()
#     O_ITEM = auto()
#     U_ITEM = auto()
#     P = auto()
#     TAG = auto()
#     CLOSE_TAG = auto()
#     TABLE = auto()
#     BOLD = auto()
#     ITALIC = auto()
#     CUT = auto()
#     LINK = auto()
#     FOOTNOTE = auto()
#     CODE = auto()
#     INDENT = auto()