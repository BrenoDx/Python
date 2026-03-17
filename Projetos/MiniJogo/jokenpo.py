

import random


jogar = True
mao = [
    'pedra','papel', 'tesoura'
]

print('==========Seja bem-vindo ao Jokenpô ==========')
while jogar:

    escolha_usuario = input('Informe qual forma irá jogar: ').lower()
    escolha_oponente = random.choice(mao)

    print('JO KEN PÔ')
    if escolha_usuario not in mao:
        print('Essa forma não faz parte do jogo!')

    if escolha_usuario == escolha_oponente:
        print('Empate, ambos jogaram a mesma forma')
    else:
        if escolha_usuario == 'pedra' and escolha_oponente == 'tesoura':
            print(f'Parabéns você ganhou, oponente jogou {escolha_oponente}')
        elif escolha_usuario == 'papel' and escolha_oponente == 'pedra':
            print(f'Parabéns você ganhou, oponente jogou {escolha_oponente}')
        elif escolha_usuario == 'tesoura' and escolha_oponente == 'papel':
            print(f'Parabéns você ganhou, oponente jogou {escolha_oponente}')
        else:
            print(f'Você perdeu, oponente jogou {escolha_oponente}')