# Exercício - Adiando execucão de funções
def soma(x,y):
    return x + y

def multiplicar(x,y):
    return x * y

def criar_funcao(funcao, x):
    def interno(y):
        return funcao(x,y)
    return interno

soma_com_cinco = criar_funcao(soma, 5)
multiplicar_por_dez =  criar_funcao(multiplicar, 10)

print(soma_com_cinco(25))
print(multiplicar_por_dez(2))

