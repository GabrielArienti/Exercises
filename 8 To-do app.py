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

# Botão

botao_novo = Button(frame_esq_cima, text="Novo", width=10, height=1,
                    bg=cor_azul, fg=cor_branco, font="15", anchor=CENTER, relief=FLAT, overrelief=RAISED)
botao_novo.grid(row=0, column=0, sticky=NSEW, pady=1)

botao_remover = Button(frame_esq_cima, text="Remover", width=10, height=1,
                       bg=cor_vermelho, fg=cor_branco, font="15", anchor=CENTER, relief=FLAT, overrelief=RAISED)
botao_remover.grid(row=0, column=1, sticky=NSEW, pady=1)

botao_atualizar = Button(frame_esq_cima, text="Atualizar", width=10, height=1,
                         bg=cor_amarelo, fg=cor_preto, font="15", anchor=CENTER, relief=FLAT, overrelief=RAISED)
botao_atualizar.grid(row=0, column=2, sticky=NSEW, pady=1)

janela.mainloop()
