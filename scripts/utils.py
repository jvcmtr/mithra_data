def csv_to_dict_array( text: str, separator=",", first_line_as_model = True):
    start_index = 0
    rows = text.splitlines()
    columns = []

    if first_line_as_model:
        start_index += 1
        columns = rows[0].split(separator)
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
    return lines

