import datetime
import tkinter as tk

def gerar_senha():
    DataAtual = datetime.date.today()
    DataFormatada = DataAtual.strftime("%d/%m/%Y")

    Dia = int(DataFormatada[0:2])
    Mes = int(DataFormatada[3:5])
    Ano = int(DataFormatada[6:10])

    Senha = Dia * Mes *Ano
    return Senha

def exibir_senha(event=None):
    senha_gerada = gerar_senha()
    resultado_label.config(text=f'A senha gerada é {senha_gerada}')

janela = tk.Tk()
janela.title("Gerador de Senhas")

largura_janela = 200
altura_janela = 200

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2

janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

botao_gerar_senha = tk.Button(janela, text="Gerar Senha", command=exibir_senha)
botao_gerar_senha.pack(pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

janela.mainloop()