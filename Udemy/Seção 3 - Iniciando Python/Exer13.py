cpf_enviado = input("Informe seu CPF") \
    .replace('.', '') \
    .replace(' ', '') \
    .replace('-', '')

nove_digitos = cpf_enviado[:9]
contador_regressivo_1 = 10
contador_regressivo_2 = 11
dez_digitos = None

resultado_1 = 0
resultado_2 = 0

for digito in nove_digitos:
    resultado_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
primeiro_digito = (resultado_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
dez_digitos = nove_digitos + str(primeiro_digito)

for digito in dez_digitos:
    resultado_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
segundo_digito = (resultado_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9  else 0

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
if cpf_enviado == cpf_gerado:
    print(f"CPF {cpf_enviado} Válido!")
else:
    print("CPF Inválido")


