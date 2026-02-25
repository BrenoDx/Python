from calculadora import somar,multiplicar,divide,subtrair
loop = True

print("======Calculadora======")
while loop:
    try:
        opcao = int(input("1 - Somar; 2 - Subtrair; 3 - divide; 4 - Multiplicar; 5 - Sair\n"))

        if opcao == 1:
            n1 = float(input("Informe o primeiro número:\n"))
            n2 = float(input("Informe o segundo número:\n"))

            print(f"Resultado é: {somar(n1,n2)}")

        if opcao == 5:
            print("Finalizando o programa")
            break

    except:
        print("Entrada Inválida!")