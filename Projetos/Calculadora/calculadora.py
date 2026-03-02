class calculadora:
    def somar(n1,n2):
        return n1+n2

    def subtrair(n1,n2):
        return n1-n2

    def divide(n1,n2):
        if n1 or n2 < 0:
            print("Divisão por 0 resulta numa Indeterminação!")
        
        return n1/n2

    def multiplicar(n1, n2):
        return n2*n2