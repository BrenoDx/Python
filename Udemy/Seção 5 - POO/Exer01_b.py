from Exer01_a import Pessoa, CAMINHO_ARQUIVO
import json

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoa = json.load(arquivo)
    
    p1 = Pessoa(**pessoa[0])
    p2 = Pessoa(**pessoa[1])
    p3 = Pessoa(**pessoa[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)