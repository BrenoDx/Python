import os
import random

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

print('==========Seja bem-vindo ao jogo de Advinhação==========')
tentativas = 10
numero_secreto = random.randint(1,20)


for i in range(9, -1, -1):
    print(f'Você tem {tentativas} tentativas\nEscolha um número entre 0 a 20')
    
    escolha = input()
    tentativas -= 1

    if escolha.isdigit():
        
        if int(escolha) == numero_secreto:
            limpar_tela()
            print(f'Parabéns vc acertou o número secreto: {numero_secreto}')
            print(f'Faltando {tentativas} tentativas!')
            break
        elif int(escolha) > numero_secreto:
            print(f'Errou, número secreto é menor que {escolha}')
        else:
             print(f'Errou, número secreto é maior que {escolha}')
    else:
        print('Informe um número correto')

if tentativas == 0:
            limpar_tela()
            print(f'Acabaram as tentativas que pena!\nO número era: {numero_secreto}')


