from api import buscar_taxa

# Mapeia variações de nomes de moedas para seus respectivos códigos ISO
MAPEAMENTO = {
    "dolar":"USD",
    "dólar":"USD",
    "euro":"EUR",
    "libra":"GBP"
}

def converter_para_real(moeda, valor):

    # Converte nomes informados pelo usuário para código oficial da moeda
    if moeda.lower() in MAPEAMENTO:
        moeda_origem = MAPEAMENTO[moeda.lower()]
    else:
        moeda_origem = moeda.lower()

    taxa = buscar_taxa(moeda_origem)
    
    if taxa is None:
        return 0
    else:
        return valor*taxa
