loop = True

print("======Calculadora======")
while loop:
    try:
        opcao = int(input("1 - Somar; 2 - Subtrair; 3 - divide; 4 - Multiplicar; 5 - Sair\n"))

        if opcao == 5:
            print("Finalizando o programa")
            break

    except:
        print("Opção Inválida!")