from typing import List

class Weapon:
    def __init__(
        self,
        nome: str,
        classe_de_tamanho: str,
        tipo_de_dano: List[str],
        habilidades: List[str],
        modulo: str,
        a_distancia: str = "falso",
        escudo: str = "falso",
        bonus_de_dano: str = "",
        bonus_de_manuseio: str = "",
        bonus_de_peso: str = "",
        bonus_de_defesa: str = ""
    ):
        self.nome = nome
        self.classe_de_tamanho = classe_de_tamanho
        self.tipo_de_dano = tipo_de_dano
        self.habilidades = habilidades
        self.modulo = modulo
        self.a_distancia = a_distancia
        self.escudo = escudo
        self.bonus_de_dano = bonus_de_dano
        self.bonus_de_manuseio = bonus_de_manuseio
        self.bonus_de_peso = bonus_de_peso
        self.bonus_de_defesa = bonus_de_defesa
