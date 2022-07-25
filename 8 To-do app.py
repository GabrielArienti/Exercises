from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu


# Cores
cor_branco = "#fafafa"
cor_preto = "#0d0d0d"
cor_amarelo = "#f2e200"
cor_vermelho = "#d10902"
cor_azul = "#010963"

# Janela principal
janela = Tk()
janela.geometry("500x225")
janela.title("To-do App")
janela.configure(bg=cor_branco)
janela.resizable(width=FALSE, height=FALSE)

# Frames

frame_esquerda = Frame(janela, width=300, height=225,
                       relief=FLAT, bg=cor_branco)
frame_esquerda.grid(row=0, column=0, sticky=NSEW)

frame_direita = Frame(janela, width=200, height=250,
                      relief=FLAT, bg=cor_branco)
frame_direita.grid(row=0, column=1, sticky=NSEW)


# Frame esquerda

frame_esq_cima = Frame(frame_esquerda, width=300, height=50,
                       relief=FLAT, bg=cor_branco)
frame_esq_cima.grid(row=0, column=0, sticky=NSEW)

frame_esq_baixo = Frame(frame_esquerda, width=300, height=175,
                        relief=FLAT, bg=cor_branco)
frame_esq_baixo.grid(row=1, column=0, sticky=NSEW)


janela.mainloop()
