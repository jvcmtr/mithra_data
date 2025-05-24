# This file defines witch properties on the config.json should be interpreted when loaded

from program.DLL import *
from program.Utils.ObjHelper import object # This is just to make the access to the object easier

# Loadable fields are the files that should be interpreted by the parser, such as 'wiki_entries' or 'weapons'
# they are called fields because they are also properties of the module object
# for more details check out https://github.com/jvcmtr/mithra_data/blob/master/docs/Module%20Structure.md 
LOADABLE_FIELDS = [
    object({
        "name" : "rules",
        "type_reference" : Doc
    }),
    object({
        "name" : "wiki_entries",
        "type_reference" : Doc
    }),
    object({
        "name" : "weapons",
        "type_reference" : Weapon
    }),
    object({
        "name" : "weapon_abilities",
        "type_reference" : Descriptor
    }),
    object({
        "name" : "armours",
        "type_reference" : Armour
    }),
    object({
        "name" : "armour_properties",
        "type_reference" : Descriptor
    }),
    object({
        "name" : "items",
        "type_reference" : Item
    }),
    object({
        "name" : "conditions",
        "type_reference" : Descriptor
    }),
    object({
        "name" : "habilities",
        "type_reference" : Hability
    })
]