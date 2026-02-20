from service import converter_para_real
import tkinter as tk
from tkinter import ttk

def converter():
    # Função executada ao clicar no botão "Converter"
    moeda = entrada_moeda.get()
    valor = float(entrada_valor.get())
    resultado = converter_para_real(moeda, valor)

    valor_convertido.config(text=f"Valor convertido: R${resultado:.2f}")

def centralizar_janela(janela, largura, altura):
    # Obtém dimensões da tela para centralizar
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)

    janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Criação da janela principal da aplicação
janela = tk.Tk()
janela.title("Conversor de Moedas")
largura = 500
altura = 400
centralizar_janela(janela, largura, altura)

# Frame principal que agrupa os widgets da interface
frame = ttk.Frame(janela, padding=20)
frame.pack()


ttk.Label(frame, text="Olá, seja bem-vindo ao Conversor de Moedas!", font=("Segoe UI", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

# Campos de entrada de dados
ttk.Label(frame, text="Moeda:").grid(row=1, column=0, sticky="w", pady=5)
entrada_moeda = ttk.Entry(frame)
entrada_moeda.grid(row=1, column=1, pady=5)
ttk.Label(frame, text="Valor:").grid(row=2, column=0, sticky="w", pady=5)
entrada_valor = ttk.Entry(frame)
entrada_valor.grid(row=2, column=1, pady=5)

botao = ttk.Button(frame, text="Converter", command=converter)
botao.grid(row=3, column=0, columnspan=2, pady=15)

valor_convertido = ttk.Label(frame, text="")
valor_convertido.grid(row=4, column=0, columnspan=2, pady=10)


janela.mainloop()



