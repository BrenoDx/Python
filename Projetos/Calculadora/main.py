from calculadora import calculadora
loop = True

print("======Calculadora======")
while loop:
    try:
        n1 = float(input("Informe o primeiro número:\n"))
        opcao = int(input("1 - Somar; 2 - Subtrair; 3 - divide; 4 - Multiplicar; 5 - Sair\n"))
        n2 = float(input("Informe o segundo número:\n"))

        if opcao == 1:
            print(f"Resultado é: {calculadora.somar(n1,n2)}")
        elif opcao == 2:
            print(f"Resultado é: {calculadora.subtrair(n1,n2)}")
        elif opcao == 3:
            print(f"Resultado é: {calculadora.divide(n1,n2)}")
          
        if opcao == 5:
            print("Finalizando o programa")
            break

    except:
        print("Entrada Inválida!")