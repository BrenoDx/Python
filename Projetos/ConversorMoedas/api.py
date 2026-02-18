import requests

def buscar_taxa(moeda_origem):
    url = f"https://api.frankfurter.app/latest?from={moeda_origem}&to=BRL"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        return dados["rates"]["BRL"]
    else:
        print(resposta)
        return None