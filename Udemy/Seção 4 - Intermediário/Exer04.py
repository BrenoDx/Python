# Exercício - Sistema de perguntas e respostas

perguntas = [
    {'Pergunta': 'Quanto que é 2+2?',
     'Opcoes':  ['1','2','3','4'],
     'Resposta': '4'
     },
     {'Pergunta': 'Quanto que é 5*5?',
     'Opcoes':  ['25','5','35','40'],
     'Resposta': '1'
     },
     {'Pergunta': 'Quanto que é 10/2?',
     'Opcoes':  ['10','2','5','1'],
     'Resposta': '3'
     },
     {'Pergunta': 'Quanto que é 50-20?',
     'Opcoes':  ['11','20','30','39'],
     'Resposta': '3'
     }
]
qtd_acerto = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    i= 1

    for opcao in pergunta['Opcoes']:
        print(i,')', opcao)
        i += 1

   
    print('\nEscolha uma opção:')
    entrada = input()
    
    if entrada == pergunta['Resposta']:
        print('Você Acertou\n')
        qtd_acerto += 1
    else:
        print('Você Errou!\n')

print('Você Acertou no total:', qtd_acerto, 'de', len(perguntas),'perguntas!')
        

    