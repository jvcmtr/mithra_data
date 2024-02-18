


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

def format( data ):
    # if data.habilities:
    #   
    return __habilities( data['habilities'] )
        