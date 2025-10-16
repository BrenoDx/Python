"""
Faça uma lista de comprar com listas
Ousuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
"""
import os
lista = []

while True:
    print("Selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]istar:")

    if opcao == "i":
        os.system("cls")
        lista.append(input("Produto: "))
    elif opcao == "a":
        try:
            os.system("cls")
            lista.pop(int(input("Escolha o índice para apagar: ")))

        except:
            print("Não foi possível apagar este índice ")

    elif opcao == "l":
        os.system("cls")
        if len(lista) == 0:
            print("Nada para listar")
            
        for item in enumerate(lista):
            print(item)
            
    else:
        print("Opcão errada")
        break