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

botao_gerar_senha = tk.Button(janela, text="Gerar Senha", command=exibir_senha)
botao_gerar_senha.pack(pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

janela.mainloop()