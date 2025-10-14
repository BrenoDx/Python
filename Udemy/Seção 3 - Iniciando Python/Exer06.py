"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. EX: Bom dia 0-11, Boa Tarde 12-17
e Boa Noite 18-23
"""
hora_str = input('Informe a hora em números inteiros: ')
if hora_str.isdigit():
    hora_int = int(hora_str)
    if hora_int >= 0 and hora_int <= 11:
        print("Bom dia!")
    elif hora_int >= 12 and hora_int <= 17:
        print("Boa Tarde!")
    elif hora_int >= 18 and hora_int <= 23:
        print("Boa Noite!")
    else:
        print("Não conheço essa hora!")
else:
    print('Digite apenas números inteiros!')