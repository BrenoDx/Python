from service import converter_para_real

print("============================================")
print("Olá, seja bem-vindo ao Conversor de Moedas!")
print("Escolha moeda que deseja fazer converter:")
print("Moedas disponíveis 'USD' Dólar, 'EUR' Euro, 'GBP' libra")
print("============================================")

moeda = input("Selecione a moeda desejada(Ex: USD, EUR, GBP): ").upper()
valor = float(input("Informe o valor que deseja converter: "))

resultado = converter_para_real(moeda, valor)
print(f"Resultado: R$ {resultado:.2f}")