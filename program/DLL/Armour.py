from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Armour:
    nome: str
    classe_de_tamanho: str
    tipo: str
    bonus_de_esquiva: str
    bolsos: str
    resistencias: List[Dict[str, str]]
    propriedades: List[str]
    modulo: str