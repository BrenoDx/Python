'''
Exercício - Salve sua classe em JSON
Salve os dados da sua classe em JSON
e depois crie novamente as instâncias
da classe com os dados salvos
faça em arquivos separados 
'''
import json
CAMINHO_ARQUIVO = 'exer01POO.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Breno', 23)
p2 = Pessoa('Gustavo', 36)
p3 = Pessoa('Julia', 31)

bd = [vars(p1), vars(p2), vars(p3)]
with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, indent=2, ensure_ascii=False)