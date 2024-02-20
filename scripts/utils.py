def csv_to_dict_array( text: str, separator=",", first_line_as_model = True):
    start_index = 0
    rows = text.splitlines()
    columns = []

    if first_line_as_model:
        start_index += 1
        columns = rows[0].lower().split(separator)
    else :
        columns = range(len(rows[0].split(separator)))

    dicts = []
    current = {}
    
    for i in range(start_index, len(rows) ):
        values = rows[i].split(separator)

        for j in range( len(columns) ):
            current[columns[j]] = values[j] or ""
        
        dicts.append(current)
        current = {}

    return dicts

def read_name_and_definition(text: str, separator=":"):
    "returns a array of dicts containing [nome] and [descrição] properties"
    lines = text.replace("  ", " ").strip().splitlines()
    habilities = []
    d = {}

    for line in lines:
        if line == "":
            continue

        props = line.split(separator, 1)
        habilities.append({
            "nome" : props[0],
            "descrição" : props[1]
        })
    return habilities

def reasign_boolean_strings( item ):
    item = replace_dict_values(item, "VERDADEIRO", True)
    item = replace_dict_values(item, "FALSO", False)
    return item


def smart_string_split (string: str, separators = ";, ", trim_results=True):
    "Try to find the correct separators from an array. Items at lower indexes are tested first, first match is used as argument for str.split()"
    separator = separators[0]
    for c in separators:
        if string.__contains__(c):
            separator = c
            break
    
    if trim_results:
        string = string.replace(" " + separator, separator)
        string = string.replace(separator + " ", separator)
        
    return string.split(separator)

def replace_dict_values(dict, old_value, new_value):
    "replace all ocourrences of a value with a new one"
    for key in dict.keys():
        if dict[key] == old_value :
            dict[key] = new_value
    return dict

    
