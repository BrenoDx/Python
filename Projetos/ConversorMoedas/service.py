from api import buscar_taxa

MAPEAMENTO = {
    "dolar":"USD",
    "dólar":"USD",
    "euro":"EUR",
    "libra":"GBP"
}

def converter_para_real(moeda, valor):
    if moeda.lower() in MAPEAMENTO:
        moeda_origem = MAPEAMENTO[moeda.lower()]
    else:
        moeda_origem = moeda.lower()

    taxa = buscar_taxa(moeda_origem)
    
    if taxa is None:
        return 0
    else:
        return valor*taxa
