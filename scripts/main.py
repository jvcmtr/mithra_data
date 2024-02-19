import DAL
import converter

DATA = {}

def main():
    load_module("base")

    print(DATA["weapons"])
    
    pass

def load_module(name):
    raw_data = DAL.get_module(name)
    formated = converter.format(raw_data)
    append_data(formated)
    
def append_data(data):
    global DATA 
    DATA = data
    pass
















if __name__ == "__main__":
    main()