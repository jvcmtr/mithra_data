from typing import List, Optional

from .Armour import Armour
from .Descriptor import Descriptor
from .Doc import Doc
from .Hability import Hability
from .Item import Item
from .Weapon import Weapon

class Theme:
    def __init__(self, color: str = "#fff", contrast: str = "#000"):
        self.color = color
        self.contrast = contrast

class MModule:
    def __init__(
        self,
        name: str,
        theme: Optional[Theme] = None,
        version: Optional[str] = None,
        module_dependencies: Optional[List[str]] = None,
        rules: Optional[List[Doc]] = None,
        wiki_entries: Optional[List[Doc]] = None,
        weapons: Optional[List[Weapon]] = None,
        weapon_abilities: Optional[List[Descriptor]] = None,
        armours: Optional[List[Armour]] = None,
        armour_properties: Optional[List[Descriptor]] = None,
        items: Optional[List[Item]] = None,
        conditions: Optional[List[Descriptor]] = None,
        habilities: Optional[List[Hability]] = None,
    ):
        self.name = name
        self.theme = theme or Theme()
        self.version = version
        self.module_dependencies = module_dependencies or []
        self.rules = rules or []
        self.wiki_entries = wiki_entries or []
        self.weapons = weapons or []
        self.weapon_abilities = weapon_abilities or []
        self.armours = armours or []
        self.armour_properties = armour_properties or []
        self.items = items or []
        self.conditions = conditions or []
        self.habilities = habilities or []
