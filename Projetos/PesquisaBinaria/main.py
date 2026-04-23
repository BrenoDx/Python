def pesquisa_binaria(lista, chute):
    baixo = 0
    alto = len(lista) -1
    while baixo <= alto:
        meio = (baixo+alto) // 2
        item = lista[meio]

        if chute == item:
            return meio
        if item > chute:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1,3,5,7,9]
print('Índice: ', pesquisa_binaria(minha_lista, 3))