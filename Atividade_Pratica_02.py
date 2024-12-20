# Importa a biblioteca do tkinter
import tkinter as tk

# Importa a função da caixa de mensagem do tkinter
from tkinter import messagebox

# Função a ser chamada quando o botão for clicado
def mostrar_mensagem():
    # Exibe uma caixa de mensagem informativa quando o botão é clicado
    messagebox.showinfo("Informação","Botão Clicado!")

# Cria janela principal
janela = tk.Tk()

# Define o título da janela
janela.title("Interface gráfica com Tkinter")

# Define o tamanho da janela 300px de largura por 200px de altura
janela.geometry("300x200")

# Cria um rótulo (label) que exibe uma mensagem na janela
rotulo = tk.Label(janela, text="Bem-vindo à sua primeira interface gráfica!")

# O método pack() posiciona o rótulo na janela, com padding (espaçamento) vertical de 20px
rotulo.pack(pady=20)

# Cria um botão e associa a função mostrar_mmensagem à ação de clique no botão
botao = tk.Button(janela, text="Clique aqui",command=mostrar_mensagem)

# O método pack() posiciona o rótulo na janela, com padding (espaçamento) vertical de 20px
botao.pack(pady=20)

# inicia o loop principal de interface gráfica, que mantém a janela aberta
# O método mainloop() escuta os eventos da interface, como cliques de botões
janela.mainloop()