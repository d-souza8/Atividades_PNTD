# Importa a biblioteca Tkinter
import tkinter as tk

# Cria janela principal
janela = tk.Tk()

# Cria o título da janela principal
janela.title("Interface gráfica com Tkinter")

# Define o tamanho da janela
janela.geometry("500x200")

# Cria o rótulo (texto)
rotulo = tk.Label(janela, text="Bem-vindo a sua primeira interface gráfica!")

# Exibe o rótulo na janela
rotulo.pack()

# Exibe e mantém a janela ativa até o usuário fechar
janela.mainloop()