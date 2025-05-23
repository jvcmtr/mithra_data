from typing import List, Dict

class Armour:
    def __init__(
        self,
        nome: str,
        classe_de_tamanho: str,
        tipo: str,
        bonus_de_esquiva: str,
        bolsos: str,
        resistencias: List[Dict[str, str]],
        propriedades: List[str],
        modulo: str
    ):
        self.nome = nome
        self.classe_de_tamanho = classe_de_tamanho
        self.tipo = tipo
        self.bonus_de_esquiva = bonus_de_esquiva
        self.bolsos = bolsos
        self.resistencias = resistencias
        self.propriedades = propriedades
        self.modulo = modulo
