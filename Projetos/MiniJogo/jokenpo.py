import random


vitoria = 0
derrota = 0
empate = 0
jogar = True
escolha = ''
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
        empate +=1
    else:
        if escolha_usuario == 'pedra' and escolha_oponente == 'tesoura':
            print(f'Parabéns você ganhou, oponente jogou {escolha_oponente}')
            vitoria +=1
        elif escolha_usuario == 'papel' and escolha_oponente == 'pedra':
            print(f'Parabéns você ganhou, oponente jogou {escolha_oponente}')
            vitoria +=1
        elif escolha_usuario == 'tesoura' and escolha_oponente == 'papel':
            print(f'Parabéns você ganhou, oponente jogou {escolha_oponente}')
            vitoria +=1
        else:
            print(f'Você perdeu, oponente jogou {escolha_oponente}')
            derrota +=1

    escolha = input('Deseja jogar novamente? [S/N]')
    if escolha.lower() == 'n':
        jogar = False

print('==========Resultado Final ==========')
print(f'Você teve {vitoria} vitória[s], {empate} empate[s] e {derrota} derrota[s] ')