import copy
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy

produtos = [
        {'nome': 'Produto 5', 'preco':10.00},
        {'nome': 'Produto 1', 'preco':22.32},
        {'nome': 'Produto 3', 'preco':10.11},
        {'nome': 'Produto 2', 'preco':105.87},
        {'nome': 'Produto 4', 'preco':69.90}
]

novos_produtos = [ {**p, 'preco': round(p['preco']*1.1, 2)} for p in copy.deepcopy(produtos) ]
print(novos_produtos)

# Ordene os produtos por nome descrescente (do maior para o menor)
# Gere Produtos_ordenados_por_nome por deep copy 

produtos_por_nome = sorted(copy.deepcopy(produtos), key=lambda p: p['nome'], reverse=True)
print(produtos_por_nome)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere Produtos_ordenados_por_preco por deep copy

produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=lambda p: p['preco'])
print(produtos_ordenados_por_preco)