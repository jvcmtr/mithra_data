### `loadModules( folder )`
Vasculha a pasta designada e carrega os modulos com os respectivos interpretadores 

###### 1. Verificar se há atualizações 
Verificar se existe algum modulo na pasta `raw/` que ainda não foi adicionada à `Data.json`
Isso pode ser feito atravéz da propriedade `version` existente no `config.json` de cada modulo.
> caso não haja atualizaçoes, o programa avisa e termina a execução
##### 2. Carregar os modulos nescessários
Carrega as informações de cada modulo utilizando os interpretadores apontados em `config.json`. 
Cada interpretador é definido por: 
- **Um tipo de dado**, como `.md`, `.json`, `.csv`
- **Um tipo de retorno**, que é hard coded dependendo do arquivo interpretado, por exemplo: um arquivo `weapons` sempre é transformado em [[WebSis/API/Interfaces#Weapon Interface|Weapon Interface]]
Uma vez carregados, os dados são armazenados em memoria para futuras operações