from dataclasses import dataclass
from typing import List, Optional

from .Armour import Armour
from .Descriptor import Descriptor
from .Doc import Doc
from .Hability import Hability
from .Item import Item
from .Weapon import Weapon

@dataclass
class Theme:
    color: str = "#fff"
    contrast: str = "#000"
    
@dataclass
class MModule:
    name: str
    theme: Optional[Theme] = None
    version: Optional[str] = None
    module_dependencies: Optional[List[str]] = None
    rules: Optional[List[Doc]] = None
    wiki_entries: Optional[List[Doc]] = None
    weapons: Optional[List[Weapon]] = None
    weapon_abilities: Optional[List[Descriptor]] = None
    armours: Optional[List[Armour]] = None
    armour_properties: Optional[List[Descriptor]] = None
    items: Optional[List[Item]] = None
    conditions: Optional[List[Descriptor]] = None
    habilities: Optional[List[Hability]] = None
