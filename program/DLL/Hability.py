from dataclasses import dataclass
from typing import List

@dataclass
class Hability:
        nome: str
        tipo: str
        requerimentos: List[str]
        descricao: str
        modulo: str
        