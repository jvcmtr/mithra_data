import utils

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
        
        if not "name" in current:
            current["name"] = line
            current["type"] = ""
            current["requirement"] = ""
            current["description"] = ""
            continue
        if line.startswith("("):
            current["type"] = line.replace("(","").replace(")","")
            continue
        if line.startswith("Requer"):
            current["type"] = line.replace("(","").replace(")","")
            continue
        
        current["description"] += (line + "\n")
    
    return habilities

def __weapons( raw_text : str):
    return utils.csv_to_dict_array(raw_text, separator="\t")
    pass

def format( data ):
    d = {}
    if "habilities" in data :
    #if data.habilities:
        d["habilities"] = __habilities( data['habilities'] )

    if "weapons" in data :
    #if data. weapons:
        d["weapons"] = __weapons( data['weapons'] )

    return d
    
        