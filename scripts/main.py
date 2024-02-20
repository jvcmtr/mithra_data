import json
import DAL
import converter
import procedures.linker as linker

DATA = {}

def main():
    global DATA
    
    load_module("base")
    load_module("armory")
    DATA = linker.relate_data(DATA)
    write_to_file()


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

def write_to_file():
    global DATA
    with open("data.json", "w", encoding="utf-8") as data_file:
        json.dump(DATA, data_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()