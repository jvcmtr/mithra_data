from typing import List
from pathlib import Path

from ..Utils.ObjHelper import object  
from ..Utils import ObjHelper as objHelper  
from ..Utils import FileHelper as fileHelper 
from ..Utils import JsonHelper as jsonHelper 
from ..DLL import MModule

from .modules_config import LOADABLE_FIELDS
from .Interpreters import InterpreterMapper



# Inicializa uma lista de modulos no formato json
def load_modules_from(folder_path : Path) -> List[MModule] :
        
        configuration_files = []
        
        # Para cada modulo no diretorio especificado, carrega o arquivo de configuração daquele modulo
        fileHelper.foreach_subfolder(folder_path, lambda f :
                configuration_files.append ( _get_module_configuration(f) ) )
        
        loaded_modules = []

        # Para cada arquivo de configuração encontrado, carrega os arquivos so modulo
        for config in configuration_files:
                loaded_modules.append( _load_config_as_module(config) )
        
        return loaded_modules



#_____________________________________________________________________________________

def _get_module_configuration(module_folder : Path):
        try:
                conf = jsonHelper.read_file(module_folder/"config.json")
                conf["path"] = module_folder
                return object(conf)
        except:
                raise OSError(f"O modulo {module_folder.name} não contem um arquivo config.json")
        
# Inicializa um modulo a partir do seu arquivo de configuração
def _load_config_as_module(config):

        # Loadable fields are the files that should be interpreted by the parser, such as 'wiki_entries' or 'weapons'
        # they are called fields because they are also properties of the module object
        # for more details check out https://github.com/jvcmtr/mithra_data/blob/master/docs/Module%20Structure.md 
        for field in LOADABLE_FIELDS:  
                target_type = field.type_reference
                file_type = config[ field.name ]
                
                if file_type == None:
                        continue
                
                parser = InterpreterMapper.find(file_type, target_type)
                path = Path( config.path ) / f"{field.name}.{file_type}"
                file_to_parse = fileHelper.read_file( path )

                config[ field.name ] = parser.parse(file_to_parse) 
        
        return objHelper.create_instance(config, MModule)    
