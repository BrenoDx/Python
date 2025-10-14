"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro
"""
numero_str = input("Digite um número inteiro")
try:
    numero_int = int(numero_str)
    if numero_int % 2 == 0:
        print(f"O número que você digitou {numero_int} é PAR")
    else:
        print(f"O número que você digitou {numero_int} é IMPAR")
except:
    print("Não é um numero inteiro")