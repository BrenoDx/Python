"""
Iterando strings com while
"""
nome = 'Breno'
tamanho_nome = len(nome)
i = 0

nova_string = ''
while i < tamanho_nome:
    letra = nome[i]
    nova_string += '*' + letra
    i += 1

print(nova_string)