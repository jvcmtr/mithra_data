class Item:
    def __init__(
        self,
        nome: str,
        tamanho: str,
        raridade: str,
        preco: int,
        construcao: str,
        efeito: str,
        composicao: str,
        module: str
    ):
        self.nome = nome
        self.tamanho = tamanho
        self.raridade = raridade
        self.preco = preco
        self.construcao = construcao
        self.efeito = efeito
        self.composicao = composicao
        self.module = module
