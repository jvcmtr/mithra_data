from dataclasses import dataclass

@dataclass
class Item:
    nome: str
    tamanho: str
    raridade: str
    preco: int
    construcao: str
    efeito: str
    composicao: str
    module: str