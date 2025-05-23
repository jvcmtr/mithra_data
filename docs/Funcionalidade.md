
# Main
Ao rodar `Python main.py` o sistema deve executar as seguintes ações:
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
##### 3. Processa os dados
aplica os serviços aos dados em memoria.
##### 4. Salva Um Backup
Copia o arquivo `Data.json` e o salva na pasta `backup/` sob o nome `yyyy-mm-dd.bak.json` onde `yyyy-mm-dd` representa o dia mês e ano (BR)
##### 5. Atualiza os Dados
Salva os dados atualizados no arquivo `data.json`, alterando a propriedade `dt_update` de cada modulo alterado

# Test
Ao rodar `Python test.py` o sistema deve executar as seguintes ações:
###### 1. Verificar se há atualizações
Verificar se existe algum modulo na pasta `raw/` que ainda não foi adicionada à `Data.json`
Isso pode ser feito atravéz da propriedade `version` existente no `config.json` de cada modulo.
> caso não haja atualizaçoes, o programa avisa e termina a execução
##### 2. Carregar os modulos nescessários
Carrega as informações de cada modulo utilizando os interpretadores apontados em `config.json`. 
Cada interpretador é definido por: 
- **Um tipo de dado**, como `.md`, `.json`, `.csv`
- **Um tipo de retorno**, que é hard coded dependendo do arquivo interpretado, por exemplo: um arquivo `weapons` sempre é transformado em [[WebSis/API/Interfaces#Weapon Interface|Weapon Interface]]
##### 3. Processa os dados
aplica os serviços aos dados em memoria.
##### 3. Atualiza os Dados de Teste
Salva os dados atualizados no arquivo `testdata.json`, alterando a propriedade `dt_update` de cada modulo alterado


# User Interface
Na etapa 1 o programa deve comunicar
- Quais modulos foram encontrados
- Qual a ultima data de atualização deste modulo (no `Data.json`)  -verbose
- Qual a ultima versão carregada deste modulo ( no `Data.json` ) 
- Qual a versão mais rescente deste modulo segundo o arquivo `config.json`

Na etapa 2 o programa deve comunicar
- O programa deve avisar para cada modulo, qual arquivo está carrecando e com qual interpretdor -verbose

Na etapa 3 o programa deve comunicar
- Se foi bem sucedido ou não em gravar o backup e qual o nome dado para o arquivo 

Na etapa 4 o programa deve comunicar
-  Quais modulos foram atualizados e qual a versão atual deles
