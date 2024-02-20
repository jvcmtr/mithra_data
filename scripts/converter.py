import utils

__PROPS = [
    "habilities",
    "weapons",
    "weapon_habilities", 
    "armours",
    "armour_props",
    "conditions"
]


def __habilities( raw_text :str ):
    raw_text = raw_text.replace("\t"," ").replace("  ", " ").strip()
            
    lines = raw_text.splitlines()
    habilities = []
    current = {}

    for l in lines:
        line = l.strip()
        if (not line) and current=={}:
            continue
        if not line:
            habilities.append(current)
            current = {}
            continue
        
        if not "nome" in current:
            current["nome"] = line
            current["tipo"] = ""
            current["requerimentos"] = ""
            current["descrição"] = ""
            continue
        if line.startswith("("):
            current["tipo"] = line.replace("(","").replace(")","")
            continue
        if line.startswith("Requer"):
            current["requerimento"] = line.replace("(","").replace(")","")
            continue
        
        current["descrição"] += (line + "\n")
    
    return habilities

def __weapons( raw_text : str):
    # TO DO : SEPARATE HABILITIES
    weapons =  utils.csv_to_dict_array(raw_text, separator="\t")
    weapons = __set_boolean_from_strings( weapons )
    return  weapons

def __weapon_habilities( raw_text : str):
    return utils.read_name_and_definition(raw_text)
    pass

def __armours( raw_text : str):
    # TO DO : CHANGE NAME COLUMN
    return utils.csv_to_dict_array(raw_text, separator="\t")

def __armour_props( raw_text : str):
    return utils.read_name_and_definition(raw_text)

def __conditions( raw_text : str):
    return utils.read_name_and_definition(raw_text)

def __include_module( data : list , module : str):
    data
    for d in data:
        d["modulo"] = module
    return data

def __set_boolean_from_strings( dict_array ):
    for item in dict_array:
        for key in item.keys():
            if item["key"] == "FALSO" or "FALSE":
                item["key"] = False
            if item["key"] == "VERDADEIRO" or "TRUE":
                item["key"] = True
    return dict_array

def format( data ):
    d = {}
    for prop in __PROPS:
        func = globals()["__" + prop]
        if prop in data :
            d[prop] = func( data[prop] )
            d[prop] = __include_module( d[prop], data["name"])        
    return d
 
    
        