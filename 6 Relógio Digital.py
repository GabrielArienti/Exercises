from tkinter import *
from tkinter import ttk
from datetime import datetime
import pyglet

# pyglet.font.add_file("digital-7.ttf")

# Cores
branco = "#fcfffd"
preto = "#141414"
amarelo = "#f7dc0a"

janela = Tk()
janela.title("Timer")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=branco)
janela.attributes("-alpha", 0.96)


def relógio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")
    ano = tempo.strftime("%Y")

    label_mostrador.config(text=hora)
    label_mostrador.after(200, relógio)
    label_data.config(text=dia_semana + "  " + str(dia) +
                      " " + str(mes) + " " + str(ano))


# Mostrador da hora
label_mostrador = Label(janela, text="", width=0, height=0, anchor="center",
                        font="Digital-7 80", bg=branco, fg=preto, )
label_mostrador.grid(row=1, column=0, padx=5, sticky=NE)

label_data = Label(janela, text="", width=0, height=0,
                   font="Digital-7 15 ", bg=branco, fg=preto)
label_data.grid(row=0, column=0, padx=5, sticky=NW)

relógio()


janela.mainloop()
