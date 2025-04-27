# desafiocadastra
[![Status do Projeto](https://img.shields.io/badge/status-concluído-brightgreen)](https://github.com/danioandrey/desafiocadastra)
[![Linguagem](https://img.shields.io/badge/linguagem-Python-blue)](https://www.python.org/)
[![Últimos Commits](https://img.shields.io/github/last-commit/danioandrey/desafiocadastra)](https://github.com/danioandrey/desafiocadastra/commits/main)

## Descrição

Coleta os ativos(todos ou filtrando) da API da Crypto Market Cap e salva no banco mysql.

## Como Começar

Necessário ter instalado o python 3.9.5 ou superior e o mysql server.

### Pré-requisitos


* Python 3.9.5 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
* pip (geralmente instalado com Python)
* Mysql Server 8.0.42 ([link](https://dev.mysql.com/downloads/installer/))

### Instalação

1.  Clone o repositório:
    ```bash
    git clone https://github.com/danioandrey/desafiocadastra.git
    cd desafiocadastra
    ```
2.  Instale as dependências Python (se houver):
    ```bash
    pip install -r requirements.txt
    ```
3.  Deve ser criado um arquivo chamado config.py e incluir os valores abaixo:
    ```bash
        mysql_connection = {
        'host':'seu host',
        'user':'seu usuário',
        'password':'sua senha',
        'database':'seu database'
        }
    ```
    ```bash
    api_config = {
        'key':'sua key da api'}
    ```

4. Caso a tabela ainda não exista, executar o scrit que contem no arquivo ddl.sql em seu banco de dados.

### Execução

O projeto pode ser executado para trazer todas as moedas disponíveis na api ou filtrando:

1. Para trazer todos os ativos e salvar no banco pasta executar o comando abaixo:
    ```bash
    python main.py
    ```
   Caseo queira filtrar  por exemplo o ativo bitcoin basta executar o comando:
   ```bash
    python main.py
    ```