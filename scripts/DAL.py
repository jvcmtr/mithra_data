import os

__path = os.path.join(os.path.dirname(__file__), "../raw/")

def __read(file_name):
    f = open( f"{__path}{file_name}" , "r", encoding="utf-8")
    s = f.read()
    f.close()
    return s

def __name_key(name):
    "defines the name of the property based on the name of the file"
    name = name[:name.index(".")]    # Removes ".txt" , ".csv", ect... 
    return name

def get_module(module_name):
    files = os.listdir(__path + module_name)
    data = { "name" : module_name}
    for file in files:
        data[ __name_key(file) ] = __read( f"{module_name}/{file}" )
    return data