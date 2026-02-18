from api import buscar_taxa

def converter_para_real(moeda, valor):
    taxa = buscar_taxa(moeda)
    if taxa is None:
        print("Erro! verifique se digitou corretamente!")
        return 0
    else:
        return valor*taxa
