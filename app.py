import requests
import pandas as pd
import time

# 
def scrap_receita_api(cnae, limite_paginas, uf="RJ"):
    url = "https://minhareceita.org/"
    
    params = {
        "cnae": cnae,
        "uf": uf,
        "limit": 100
    }

    results = []
    cursor = None

    for i in range(limite_paginas):
        if cursor:
            params["cursor"] = cursor

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            companies = data.get("data", [])
            results.extend(companies)

            cursor = data.get("cursor")

            if not cursor:
                break

        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            break

        time.sleep(0.5)

    return results


def filter_companies(companies):
    results = []

    for data in companies:
        address = ", ".join(filter(None, [
            data.get('descricao_tipo_de_logradouro'),
            data.get('logradouro'),
            data.get('numero'),
            data.get('complemento')
        ]))

        scrap = {
            "CNPJ": data.get("cnpj"),
            "Nome": data.get("razao_social"),
            "Situação Cadastral": data.get("situacao_cadastral"),
            "Data Situação Cadastral": data.get("data_situacao_cadastral"),
            "Data de Início de Atividades": data.get("data_inicio_atividade"),
            "Endereço": address,
            "Bairro": data.get("bairro"),
            "Município": data.get("municipio"),
            "UF": data.get("uf"),
            "CEP": data.get("cep"),
            "Telefone 1": data.get("ddd_telefone_1"),
            "Telefone 2": data.get("ddd_telefone_2"),
            "Telefone Fax": data.get("ddd_fax"),
            "CNAE Principal": data.get("cnae_fiscal"),
            "CNAE Descrição": data.get("cnae_fiscal_descricao") or "",
        }

        results.append(scrap)

    return results


def scrap_companies(cnae, limite_paginas, uf="RJ"):
    companies = scrap_receita_api(cnae, limite_paginas, uf)

    if not companies:
        print("Nenhum dado encontrado.")
        return None

    scrap_list = filter_companies(companies)

    return scrap_list

# modifique aqui para 
cnae = "8112500"
data = scrap_companies(cnae, limite_paginas=1, uf="RJ")

if data:
    df = pd.DataFrame(data)

    # salvar arquivo
    df.to_csv("empresas.csv", index=False, sep=";", encoding="latin1")
    print("Arquivo salvo com sucesso!")
    print(f"Linhas salvas: {len(df)}")
