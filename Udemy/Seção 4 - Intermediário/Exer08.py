# Exercício - unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem
# Use todos os valores da menor lista.
# EX:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado 
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest

cidades = ['Salvador', 'Ubatuba', 'Belo Horizontes']
uf = ['BA', 'SP', 'MG', 'RJ']
lista = [()]

def zipper(list, list2):
    intervalo_maximo = min(len(list), len(list2))
    return [(list2[i], list[i]) for i in range(intervalo_maximo)]
    

print(zipper(uf, cidades))
print(list(zip(cidades, uf)))
print(list(zip_longest(cidades, uf, fillvalue='SEM CIDADE')))
