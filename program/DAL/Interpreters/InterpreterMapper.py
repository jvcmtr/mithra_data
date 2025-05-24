from program.DLL import * 
from .Implementations import MdToDoc

def nameof(cls):
    return cls.__name__

_NO_PARSER = None

_INTERPRETERS = {
    "md" : {
        nameof(Armour) :      _NO_PARSER, 
        nameof(Descriptor) :  _NO_PARSER, 
        nameof(Doc) :         MdToDoc,
        nameof(Hability) :    _NO_PARSER,
        nameof(Item) :        _NO_PARSER,
        nameof(Weapon) :      _NO_PARSER
    },
    "csv" : {
        nameof(Armour) :      _NO_PARSER, 
        nameof(Descriptor) :  _NO_PARSER, 
        nameof(Doc) :         _NO_PARSER,
        nameof(Hability) :    _NO_PARSER,
        nameof(Item) :        _NO_PARSER,
        nameof(Weapon) :      _NO_PARSER
    },
    "tsv" : {
        nameof(Armour) :      _NO_PARSER, 
        nameof(Descriptor) :  _NO_PARSER, 
        nameof(Doc) :         _NO_PARSER,
        nameof(Hability) :    _NO_PARSER,
        nameof(Item) :        _NO_PARSER,
        nameof(Weapon) :      _NO_PARSER
    }
}


def find(file_type, target):
    
    if not _suport_file(file_type):
        suported_file_types = [x for x in _INTERPRETERS.keys()]
        raise NotImplementedError(f"O tipo de arquivo '{file_type}' não é suportado. Os tipos suportados são: { suported_file_types }")  
    
    parser = _INTERPRETERS[file_type][nameof(target)]
        
    if parser == _NO_PARSER:
        raise NotImplementedError(f"Mapeamento inexistente entre arquivo: {file_type} e {nameof(target)}")  
    
    return parser


def _suport_file(file_type):
    return _INTERPRETERS.get(file_type, None) != None


