# Scrap CNAE Receita Federal

Aplicativo para extrair dados da receita federal usando o CNAE como filtro. Ao final da extração, armazena os dados em um arquivo Excel formatado em Português.

## Tecnologias Usadas

* Python
* Pandas
* Requests

---

## Dados obtidos na extração

* CNPJ
* Nome
* Situação Cadastral
* Data Situação Cadastral
* Data de Início de atividades
* Endereço
* Bairro
* Município
* UF
* CEP
* Telefone
* CNAE Principal
* CNAE Descrição

---

## Como executar o projeto

### 1- Clone este repositório para seu computador.

No seu terminal, execute:

```
git clone https://github.com/nanic1/receita-api-cnae-scrap
cd receita-api-cnae-scrap
```

### 2- Instale as dependências necessárias

Ainda no terminal, execute:

```
pip install pandas
```

### 3- Defina o CNAE e UF para filtrar

Na variável cnae e data, você vai ver algo parecido com:

```
cnae = "8112500"
data = scrap_companies(cnae, limite_paginas=1, uf="RJ")
```

Mude o cnae, limite_paginas e uf para o CNAE, quantas páginas você deseja ler e o estado que deseja filtrar suas empresas. Cada página tem 100 empresas, o máximo de páginas que você consegue ler atualmente nesta API é 1000.

### 4- Execute o programa

Abra o terminal e digite

```
python app.py
```

Após isso, deixe o programa carregar até exibir a mensagem "Arquivo salvo com sucesso!". Depois disso, seus dados estarão carregados em um arquivo Excel chamado "empresas.xlsx"

## Autor
Pedro Kurtz - APSA
