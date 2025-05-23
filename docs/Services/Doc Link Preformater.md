## Sobre
Este serviço tem como proposito preformatar todos os headers de um arquivo (em geral extraido de um .md) antes do serviço linker ser usado.

segundo a regra de [[LinkService#Validação de nomes|Validação de links]] do [[LinkService]], Dois itens do mesmo tipo não podem possuir o mesmo link, para evitar este conflito em caso de docs (que sendo documentos podem possuir o mesmo nome), a hierarquia de topicos é incluida dentro do nome de cada topico.

### Exemplo
**Isso**
```
# My Header
### my subheader
```
**Se torna**
```
# My Header
## my_header>my_subheader
```

contudo, este serviço opera sobre a interface [[Interfaces#Doc Interface|Doc]] , então, na prática:
**Isso**
``` json
{
	"linkId": null,  
	"type": "h1",
	"text": "My Header",
	"content": [
		{
			"linkId": null,  
			"type": "h2",
			"text": "my subheader",
			"content": [] 
		},	
	] 
},
```
**Se torna**
``` json
{
	"linkId": "my_header",  
	"type": "h1",
	"text": "My Header",
	"content": [
		{
			"linkId": "my_header>mysubheader",  
			"type": "h2",
			"text": "my subheader",
			"content": [] 
		},	
	] 
},
```