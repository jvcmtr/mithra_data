from typing import List, Union

class Doc:
    def __init__(self, linkId: str, type: str, text: str, content: List['Doc']):
        self.linkId = linkId
        self.type = type  # h1, h2, p, table, list
        self.text = text
        self.content = content
