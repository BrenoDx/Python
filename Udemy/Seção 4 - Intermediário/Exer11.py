'''
Exercício - lista de tarefas com desfazer e refazer
todo = [] -> lista de tarefas
todo = ['Fazer café'] -> Adicionar fazer café
todo = ['fazer café', 'caminhar'] -> adicionar caminhar
desfazer = ['fazer café'] -> refazer ['caminhar']
desfazer = [] -> refazer ['fazer café','caminhar']
refazer = todo ['Fazer café']
refazer = todo ['fazer café', 'caminhar']
'''
import os
import json


def listar(list):
    print('\nTAREFAS:')
    if list is not None:
        for tarefa in list:
            print(tarefa)
    print()

def adicionar(tarefa, list):
    
    list.append(tarefa)
    listar(list)

def desfazer(list, list2):
    if list is not None:
        list2.append(list[-1])
        list.pop()
        listar(list)

def refazer(list, list2):
    if list2 is not None:
        list.append(list2[-1])
        list2.pop()
        listar(list)

def ler_tarefas(tarefas,caminho):
    dados = []
    try:
        with open(caminho, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
            salvar_tarefas(tarefas, caminho)
            return dados
    except FileNotFoundError:
        print('Arquivo não encontrado')
        salvar_tarefas(tarefas, caminho)
        return dados

def salvar_tarefas(tarefas, caminho):
    dados = tarefas
    with open(caminho, 'w', encoding='utf8') as arquivo:
            dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
            return dados

CAMINHO = 'arquivo.json'
lista_tarefas = ler_tarefas([], CAMINHO)
lista_excluidos = []

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(lista_tarefas),
        'desfazer': lambda: desfazer(lista_tarefas, lista_excluidos),
        'refazer': lambda: refazer(lista_tarefas, lista_excluidos),
        'clear': os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, lista_tarefas),
    }
   
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()
    salvar_tarefas(lista_tarefas, CAMINHO)