import DAL
import converter

DATA = {}

def main():
    load_module("base")
    load_module("armory")

    for w in DATA["weapons"]:
        print(w["nome"])
    
    pass

def load_module(name):
    raw_data = DAL.get_module(name)
    formated = converter.format(raw_data)
    append_data(formated, name)
    
def append_data(data, module):
    global DATA 
    for key in data.keys():
        if key in DATA.keys():
            DATA[key] += data[key]
        else:
            DATA[key] = data[key]


















if __name__ == "__main__":
    main()