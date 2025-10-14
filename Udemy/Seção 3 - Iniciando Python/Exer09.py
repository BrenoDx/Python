""" Calculadora com While"""
opcao = True

while opcao:
    primeiro_numero = input('Digite o primeiro número!')
    segundo_numero = input('Digite o segundo número!')
    operador = input('Digite o operador (+-/*)')

    numeros_validos = None

    try:
        num_1_float = float(primeiro_numero)
        num_2_float = float(segundo_numero)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um dos números são inválidos!')
        continue
        
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos or len(operador) > 1:
        print('operador inválido')
        continue
    print('Realizando sua conta...')
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float-num_2_float)
    elif operador == '*':
        print(num_1_float*num_2_float)
    elif operador == '/':
        print(num_1_float/num_2_float)
    opcao = input('Quer sair?').lower().startswith('n')
