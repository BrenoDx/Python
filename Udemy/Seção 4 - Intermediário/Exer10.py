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

lista_tarefas = []
lista_excluidos = []

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa.lower() == 'listar':
        listar(lista_tarefas)
    elif tarefa.lower() == 'desfazer':
        desfazer(lista_tarefas, lista_excluidos)
    elif tarefa.lower() == 'refazer':
        refazer(lista_tarefas, lista_excluidos)
    elif tarefa.lower() == 'clear':
        os.system('cls')
    else:
        adicionar(tarefa, lista_tarefas)
