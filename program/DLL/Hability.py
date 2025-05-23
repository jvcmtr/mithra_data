from typing import List

class Hability:
    def __init__(
        self,
        nome: str,
        tipo: str,
        requerimentos: List[str],
        descricao: str,
        modulo: str
    ):
        self.nome = nome
        self.tipo = tipo
        self.requerimentos = requerimentos
        self.descricao = descricao
        self.modulo = modulo
