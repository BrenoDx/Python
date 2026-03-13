'''
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]
============ Resultado
lista_soma = [2,4,6,8]
'''
def somar_lista(list,list2):
    tamanho = min(len(lista_a), len(lista_b))
    lista_soma = []
    for i in range(tamanho):
        lista_soma.append(list[i]+list2[i])
    
    return lista_soma



lista_a = [10,12,24,50,48,80,100]
lista_b = [20,24,48,100] 

print(somar_lista(lista_a, lista_b))


