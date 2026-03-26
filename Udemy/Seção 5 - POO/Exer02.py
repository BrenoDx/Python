'''
Exercício com classes
1 - Crie uma classe Carro (nome)
2 - Crie uma classe Motor (nome)
3 - Crie uma classe Fabricante (nome)
4 - Faça a ligação entre Carro tem Motor
Obs: Um motor pode ser de vários carros
5 - Faça a ligação entre Carro e Fabricante
Obs: Um fabricante pode fabricar vários carros
Exiba o nome do carro, motor e fabricantes na tela
'''

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
        
    @motor.setter
    def motor(self, nome):
        self._motor = nome

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante = nome

class Motor:
    def __init__(self, nome):
        self.nome= nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fiat_uno = Carro('Uno')
motor_1_0 = Motor('1.0')
fiat = Fabricante('Fiat')
fiat_uno.motor = motor_1_0
fiat_uno.fabricante = fiat

honda_hrv = Carro('Hr-v')
motor_2_0 = Motor('2.0')
honda = Fabricante('Honda')
honda_hrv.motor = motor_2_0
honda_hrv.fabricante = honda

ford_fiesta = Carro('Fiesta')
motor_1_6 = Motor('1.6')
ford = Fabricante('Ford')
ford_fiesta.motor = motor_1_6
ford_fiesta.fabricante = ford

print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)
print(honda_hrv.nome, honda_hrv.fabricante.nome, honda_hrv.motor.nome)
print(ford_fiesta.nome, ford_fiesta.fabricante.nome, ford_fiesta.motor.nome)