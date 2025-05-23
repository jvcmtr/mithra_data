
# API Module Folder
```
nome_do_modulo/
	config.json
	rules.md
	wiki_entries.md
	weapons.csv
	weapon_abilities.csv 
	armours.csv
	armour_properties.csv 
	items.csv 
	condition.md 
	habilities.md
```

### config.json
``` json
{
	name: nome_do_modulo, // Se não for definido usa o nome da pasta
	theme: { color: hex , contrast: hex }, // default: {#fff, #000} 
	version: "versão", // opcional
	module_dependencies: [ nome_da_dependencia ], // só para debug
	
	// interpretador : json, csv, md
	// cada interface de retorno da api possui o seu proprio interpretador. 
	// exemplo: csvToWeapon, mdToDoc, mdToHability, etc...
	// caso um interpretador não esteja definido aqui, este arquivo será ignorado
	
	rules : interpretador, 
	wiki_entries: interpretador, 
	weapons: interpretador, 
	weapon_abilities: interpretador,  
	armours: interpretador,       
	armour_properties: interpretador,  
	items: interpretador,           
	conditions: interpretador, 
	habilities: interpretador
}
```

