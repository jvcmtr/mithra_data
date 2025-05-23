from typing import List
from ..DLL.MModule import MModule

import program.Services.DocPreformater as DocPreformater
import program.Services.Linker as Linker

# Lista de procedimentos a serem executados, em ordem
PROCEDURES = [
    lambda data: DocPreformater.apply(data),
    lambda data: Linker.apply(data)
]

def exec(data: List[MModule]) -> List[MModule] :
    # Aplica todos os procedimentos
    for procedure in PROCEDURES:
        data = procedure(data)
    return data
