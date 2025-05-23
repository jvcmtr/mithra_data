link service serve para mapear links entre os documentos e modulos.

## Formato
o formato de um link deve ser: `\\modulo#componente#item#alias\\` onde:
- `modulo`: O modulo ao qual aquele item pertence
- `componente` é qual recurso aquele item é referente (ex: `habilities`, `wiki_entry`)
- `item` é a chave para aquele item, normalmente extraido do nome ou cabeçalho
- `alias` é o texto opcional pelo qual este item será chamado

## Procedimento
para o serviço de link funcionar, são nescessarias 3 etapas. 
1. Carrega todas as entradas do sistema para gerar uma lista de items (ou links possiveis)
2. Mapeia os links existentes no sistema
3. Troca o texto existente nos campos por links segundo o formato

#### Carregando items
O sistema deve, para cada modulo e recurso dentro do modulo, carregar uma lista de links que correspondem a todos os links existentes no sistema. Chamamos esta lista de **Links_Possiveis**
O carregamento de itens ignora capitalização para o nome de itens, modulos e recursos.

Este carregamento, também valida o nome de cada item, garantindo que podemos mapear um link para um item. Para isso seguimos a seguinte validação
###### Validação de nomes
- **O nome de um item deve ser unico dentro de seu grupo de recursos**
	Ou seja, dentro do grupo de recursos `weapons` não deve haver duas armas chamadas `espada curva` , independentemente do modulo do qual elas fazem parte.
	Falha nesta validação gera um **Erro** dizendo: o item x  possui o mesmo nome do item Y (especificando o modulo e o recurso de cada item)

- **O nome de um item é de preferencia unico dentro de seu modulo**
	Ou seja, dentro de um mesmo modulo não deve haver uma `weapon` chamada `tridente dourado` e ao mesmo tempo uma `wiki_entry` chamada `tridente_dourado`. 
	Falha nesta validação gera um **Alerta** dizendo o recurso x  possui o mesmo nome do recurso Y no modulo Z, considere alterar o nome segundo as diretivas de [[LinkService#Evitando conflitos manualmente|Evitar conflitos manualmente]] 

- **O nome de um item é preferivelmente unico**
	Ou seja, o nome de um topico idealmente não deve ser repetido independentemente do modulo ou tipo de recurso, ou seja, um recurso `rule` chamado `ataque furtivo` no modulo `base` entraria em conflito caso existisse um recurso `hability` de mesmo nome no modulo `guilda_dos_assassinos`.
	Cada caso onde isso acontece é contabilizado por nome (exemplo X entradas possuem o nome `ataque furtivo`). Ao final do carregamento de itens, o sistema deve gerar um **Alerta** dizendo: `N` nomes não são unicas no sistema, totalizando em `Y` items repetidos (onde N é a soma do numero de nomes unicos e Y é a soma de X)

#### Mapeando links existentes no sistema
procura em campos predeterminados para cada resurso por links do tipo: obsidian, formato_suportado e texto_simples ( texto simples para os casos de arquivos csv e tsv)
> Isso deve ser mapeado manualmente

cada link é mapeado para um objeto link na lista de **Links_Possiveis**. A principio, somente o nome do `item` é nescessário para definir a qual link este está associado. Contudo, caso existam dois links com o mesmo nome, este caso é passado para o [[LinkService#Gerenciador de conflitos|Gerenciador de conflitos]] para que ele avalie qual link deve ser usado.

Uma vez que estes links sejam identificados, eles são colocados em uma nova lista chamada **Links Efetivos**. esta lista mapeia um seletor:  modulo.recurso.item.campo (exemplo: `(data) => data.base.weapons.weapon_habilities.alcance.description`) para um link existente na lista de **Links_Possiveis**.

### Trocando links existentes
para cada item na lista de **Links Efetivos**, selecionar o campo do item que deve ter seu link transformado e o transforma para o  [[LinkService#Formato|Formato padrão]]  

## Conflitos
#### Gerenciador de conflitos
Em teoria, somente o nome do item é nescessario para identificar a qual a qual item ele está associado, contudo, dois itens podem possuir o mesmo nome. Para resolver este conflito, podemos nos apoiar na [[LinkService#Validação de nomes|Validação de nomes]] para garantir que o nome é unico dentro de um mesmo tipo de recurso. 

#### Evitando conflitos manualmente
Para evitar conflitos manualmente podemos mudar o nome dos topicos dentro do .md e definir um alias.
(tudo depois de _ é ignorado? ´´e uma maneira de gerar um alias)
( Caso queiramos uma entrada na wiki sobre um item existente em outro topico, podemos colocar um "O" na frente. por exemplo: "Tridente dourado" --> "O Tridente dourado")

## Link interface (formato intermediario)
``` json
{
	item: "", 
	module: "", 
	component: "", 
	aliases: [] // ?????
}
```

