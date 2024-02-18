import DAL
import converter

HABILITIES = []
WEAPONS = []
WEAPON_HAB = []
ARMOURS = []
ARMOUR_PROPS = []
ACTIONS = []
CONDITIONS = []

def main():
    load_module("base")
    print(HABILITIES)
    pass

def load_module(name):
    raw_data = DAL.get_module(name)
    formated = converter.format(raw_data)
    append_data(formated)
    
def append_data(data):
    global HABILITIES 
    HABILITIES += data
    pass
















if __name__ == "__main__":
    main()