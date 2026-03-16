import csv
import difflib
import requests


url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
ibge_respos = requests.get(url).json()
municipios = {}
total_ok = 0
total_nao_encontrado = 0
total_erro_api = 0
pop_total_ok = 0

pop_por_regiao = {}
contagem_por_regiao = {}


for dados in ibge_respos:
    try:
        nome = dados["nome"]
        uf = dados["microrregiao"]["mesorregiao"]["UF"]["sigla"]
        regiao = dados["microrregiao"]["mesorregiao"]["UF"]["regiao"]["nome"]
        id_ibge = dados["id"]

        municipios[nome.lower()] = {
            "uf": uf,
            "regiao": regiao,
            "id": id_ibge
        }
    except (KeyError, TypeError):
        continue
nomes_ibge = list(municipios.keys())

resultado = []

with open("input.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:

        municipio = row["municipio"]
        populacao = int(row["populacao"])

        match = difflib.get_close_matches(municipio, nomes_ibge, n=1, cutoff=0.6)

        if match:

            nome_ibge = match[0]
            dados = municipios[nome_ibge]

            resultado.append({
                "municipio_input": municipio,
                "populacao_input": populacao,
                "municipio_ibge": nome_ibge,
                "uf": dados["uf"],
                "regiao": dados["regiao"],
                "id_ibge": dados["id"],
                "status": "OK"
            })

        else:

            resultado.append({
                "municipio_input": municipio,
                "populacao_input": populacao,
                "municipio_ibge": "",
                "uf": "",
                "regiao": "",
                "id_ibge": "",
                "status": "NAO_ENCONTRADO"
            })

with open("resultado.csv", "w", newline="", encoding="utf-8") as f:

    campos = [
        "municipio_input",
        "populacao_input",
        "municipio_ibge",
        "uf",
        "regiao",
        "id_ibge",
        "status"
    ]

    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()

    for r in resultado:
        writer.writerow(r)

print("resultado.csv gerado")

total_municipios = len(resultado)
for r in resultado:

    status = r["status"]

    if status == "OK":
        total_ok += 1
        pop_total_ok += r["populacao_input"]

        regiao = r["regiao"]

        if regiao not in pop_por_regiao:
            pop_por_regiao[regiao] = 0
            contagem_por_regiao[regiao] = 0

        pop_por_regiao[regiao] += r["populacao_input"]
        contagem_por_regiao[regiao] += 1

    elif status == "NAO_ENCONTRADO":
        total_nao_encontrado += 1

    elif status == "ERRO_API":
        total_erro_api += 1

medias_por_regiao = {}

for regiao in pop_por_regiao:

    soma = pop_por_regiao[regiao]
    quantidade = contagem_por_regiao[regiao]

    medias_por_regiao[regiao] = soma / quantidade

stats = {
    "total_municipios": total_municipios,
    "total_ok": total_ok,
    "total_nao_encontrado": total_nao_encontrado,
    "total_erro_api": total_erro_api,
    "pop_total_ok": pop_total_ok,
    "medias_por_regiao": medias_por_regiao
}

print(stats)

url_submit = "https://mynxlubykylncinttggu.functions.supabase.co/ibge-submit"

access_token = "eyJhbGciOiJIUzI1NiIsImtpZCI6ImR0TG03UVh1SkZPVDJwZEciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL215bnhsdWJ5a3lsbmNpbnR0Z2d1LnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiI4Yjk3NTUxYS04MTg5LTQ4YTgtYjQ4MS0xMGIwYjMwOTRiYWIiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzczNjk4NzM2LCJpYXQiOjE3NzM2OTUxMzYsImVtYWlsIjoiYnJlbm8uYWx2ZXMyMDAyQGhvdG1haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJlbWFpbCIsInByb3ZpZGVycyI6WyJlbWFpbCJdfSwidXNlcl9tZXRhZGF0YSI6eyJlbWFpbCI6ImJyZW5vLmFsdmVzMjAwMkBob3RtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJub21lIjoiQnJlbm8gQWx2ZXMgZGUgQXJh77-9am8iLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInN1YiI6IjhiOTc1NTFhLTgxODktNDhhOC1iNDgxLTEwYjBiMzA5NGJhYiJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6InBhc3N3b3JkIiwidGltZXN0YW1wIjoxNzczNjk1MTM2fV0sInNlc3Npb25faWQiOiI1ODI3MjQ5YS02YTE2LTQ5ZTYtYmJiOC0zZjU0OTMxM2U3YzkiLCJpc19hbm9ueW1vdXMiOmZhbHNlfQ.5JHynVDV9kw4shYiOsQEA09vUZPT3lyFJ4wM_-wsc58"

payload = {
    "stats": stats
}

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

response = requests.post(
    url_submit,
    json=payload,
    headers=headers
)

print("Resposta da API:")
print(response.json())