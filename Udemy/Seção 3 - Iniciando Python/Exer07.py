"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
nome = input("Digite seu nome: ")
qnt_nome = len(nome)
if qnt_nome > 1:
    if qnt_nome <= 4:
        print("Seu nome é curto")
    elif qnt_nome >= 5 and qnt_nome <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("Digite ao menos 2 letras.")