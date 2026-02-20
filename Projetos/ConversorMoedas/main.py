from service import converter_para_real
import tkinter as tk

def converter():
    moeda = entrada_moeda.get()
    valor = float(entrada_valor.get())
    resultado = converter_para_real(moeda, valor)

    valor_convertido.config(text=f"Valor convertido: R${resultado:.2f}")

def centralizar_janela(janela, largura, altura):
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)

    janela.geometry(f"{largura}x{altura}+{x}+{y}")


janela = tk.Tk()
janela.title("Conversor de Moedas")
largura = 500
altura = 400
centralizar_janela(janela, largura, altura)


msg = tk.Label(janela, text="Olá, seja bem-vindo ao Conversor de Moedas!")
inicio = tk.Label(janela, text="Moedas disponíveis 'USD' Dólar, 'EUR' Euro, 'GBP' libra")
entrada_moeda = tk.Entry(janela)
entrada_valor = tk.Entry(janela)
botao = tk.Button(janela, text="Converter", command=converter)


valor_convertido = tk.Label(janela, text="")

msg.pack(pady=10)
inicio.pack(pady=15)
entrada_moeda.pack()
entrada_valor.pack(pady=5)
botao.pack(pady=30)
valor_convertido.pack(pady=5)
janela.mainloop()



