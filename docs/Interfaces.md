# Response ( Data.json ) 
``` json
[
	{
		name: nome_do_modulo,
		theme: { color: hex , contrast: hex },
		"version" : versao, // extraida de config.json
		dt_update: "data do ultimo update", // gerada em runtime
		module_dependencies: [ nome_da_dependencia ], // só para debug
		rules : [], // doc interface
		wiki_entries: [], // doc interface
		weapons: [], // weapon interface
		weapon_abilities: [], // descriptor interface
		armours: [],       // armour interface
		armour_properties: [], // descriptor interface
		items: [],             // item interface
		conditions: [], // { name, description, module } 
		habilities: [], // hability interface
	}
]
```

### Doc Interface
``` json
{
	"linkId": "my_header\my_subheader" // hierarquia de 
	"type":"h2", //h1, p, table, list
	"text": "my subheader",
	"content": [] // doc interface
},
```
#### Weapon Interface
``` json
"weapons": [
{
  "a distancia": "falso",
  "escudo": "falso",
  "classe de tamanho": "a",
  "bônus de dano": "1",
  "nome": "lâminas pequenas",
  "tipo de dano": [
	"cortante",
	"perfurante"
  ],
  "bônus de manuseio": "1",
  "bônus de peso": "",
  "bônus de defesa": "",
  "habilidades": [
	"defensivo",
	"ignorar armadura",
	"arremessavel"
  ],
  "modulo": "base"
},
```

### Armour Interface
```json
{
  "classe de tamanho": "c",
  "tipo": "armadura leve",
  "nome": "armadura acolchoada",
  "bônus de esquiva": "-1",
  "bolsos": "3",
  "resistências": [
	  {
		  "tipo de dano" : "impacto"
		  "valor": 2 
	  }
  ],
  "propriedades": [
	""
  ],
  "modulo": "base"
},
```

### Habilitiy Interface
``` json
{
  "nome": "arco convicto",
  "tipo": "habilidade ofensiva",
  "requerimentos": [
	  "ataque convicto",
  ],
  "descrição": "você realiza um ataque conduzido corpo a corpo contra qualquer criatura dentro do alcance e reduz à metade o seu modificador de precisão, quando faz isso, você pode somar o seu modificador de convicção para calcular o impacto do seu ataque. além disso, o seu dano aumenta em 2.",
  "modulo": "base"
},
```

### Item interface
``` json
{ 
	nome: nome, 
	tamanho: descrição,  // A, B, C, D
	raridade: raridade, // A, B, C, D
	preço: 1, // em gp
	construção: "", // qual item pode ser usado para construir este
	efeito: "", // o que faz
	composição: "", // descrição, se for um kit, o que pode ser encontrado nele
	module: modulo_ao_qual_pertence 
	
} 
```
### Descriptor interface
``` json
{ 
	name: nome, 
	description: descrição, 
	module: modulo_ao_qual_pertence 
} 
```