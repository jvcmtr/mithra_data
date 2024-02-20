# LINK FORMAT    [[resource:id|name]]
LINKS = []

def relate_data(data):
    __init_links(data)
    
    data = __link_armour(data)
    data = __link_weapon(data)  
    data = __link_hability_requirements(data)
    data = __link_descriptions(data)
    
    return data
    

### INITIALIZATION FUNCTIONS
def __init_links(data : dict):
    global LINKS
    
    for resource_name in data.keys():
        resource = data[resource_name]
        for item in resource:
            LINKS.append(__generate_link(resource_name, resource, item))
            
def __generate_link(group, resource, item):
    name = item["nome"]
    alias = " "+name+" "
    id = resource.index(item)
    link = f" [[{group}:{id}|{name}]] "
    
    if (name == "") or (name == " "):
        name = " # E R R O R "
        
    return {
        "alias": alias,
        "link" : link
    }


### REPLACING FUNCTIONS
def __link_armour(data): 
    new_armour = data["armours"]
    
    for a_index in range(len(new_armour)) :
        a = new_armour[a_index]
        
        for p_index in range(len( a["propriedades"])):
            new_armour[a_index]["propriedades"][p_index] = __replace_link( new_armour[a_index]["propriedades"][p_index]  )
    
    new_data = data
    new_data["armours"] = new_armour
    return new_data   
    pass

def __link_weapon(data):
    new_weapons = data["weapons"]
    
    for w_index in range(len(new_weapons)) :
        w = new_weapons[w_index]
        
        for h_index in range(len( w["habilidades"]) ):
            new_weapons[w_index]["habilidades"][h_index] = __replace_link( new_weapons[w_index]["habilidades"][h_index]  )
    
    new_data = data
    new_data["weapons"] = new_weapons
    return new_data

def __link_hability_requirements(data):
    new_habilities = data["habilities"]
    
    for index in range(len(new_habilities)):
        new_habilities[index]["requerimentos"] = __replace_link( new_habilities[index]["requerimentos"] )
    
    new_data = data
    new_data["habilities"] = new_habilities
    return new_data

def __link_descriptions(data :dict):
    new_data = data

    for resource_name in data.keys():
        resource = data[resource_name]
        
        if "descrição" not in resource[0].keys():
            continue
        
        for i in range(len(resource)):
            new_data[resource_name][i]["descrição"] = __replace_link( new_data[resource_name][i]["descrição"] )
    
    return new_data

def __replace_link(text :str):
    global LINKS
    output = text
    for link in LINKS:
        if text.__contains__(link["alias"]):
                output = output.replace(link["alias"], link["link"])
    
    return output