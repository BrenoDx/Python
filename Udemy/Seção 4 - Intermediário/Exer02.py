# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar

def par_impar(numero):
    if numero % 2 == 0:
        return f"{numero} é PAR"
    return f"{numero} é ÍMPAR"

print(par_impar(2))
print(par_impar(3))
print(par_impar(40))
print(par_impar(27))