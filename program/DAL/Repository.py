from typing import List
from pathlib import Path

from ..Utils import FileHelper as fileHelper 
from ..Utils import JsonHelper as jsonHelper 
from ..DLL import MModule


ModulesConfig = []



# Inicializa uma lista de modulos no formato json
def load_modules_from(folder_path : Path) -> List[MModule] :
        
        # Para cada modulo no diretorio especificado, carrega o arquivo de configuração daquele modulo
        fileHelper.foreach_subfolder(folder_path, lambda f : _save_module_config(f) )



#_____________________________________________________________________________________

def _save_module_config(module_folder : Path):
        try:
                conf = jsonHelper.read_file(module_folder/"config.json")
                conf["path"] = module_folder
                ModulesConfig.append(conf)
        except:
                raise OSError(f"O modulo {module_folder.name} não contem um arquivo config.json")

            
