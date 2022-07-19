from ast import Num
from tkinter import *
from tkinter import ttk
from tkinter import dialog

from click import UsageError

# Cores usadas:
cor_branco = "#fcfcfc"
cor_preto = "#030303"
cor_amarelo = "#fadd00"
cor_brancocaixa = "#f2f2f2"

janela = Tk()
janela.title("")
janela.geometry("1000x550")
janela.config(bg=cor_branco)
janela.resizable(width=FALSE, height=FALSE)


# Frame esquerda (informações)

frame_esquerda = Frame(janela, width=500, height=550,
                       relief=FLAT, bg=cor_branco)
frame_esquerda.grid(row=0, column=0)

# Frame direita (mostrador)

frame_direita = Frame(janela, width=500, height=550,
                      relief=FLAT, bg=cor_branco)
frame_direita.grid(row=0, column=3)

# Frame esquerda

label_titulo = Label(frame_esquerda, text="Calculadora Kabalística", padx=3,
                     pady=3, relief=FLAT, font="Raleway 19 bold", bg=cor_branco, fg=cor_preto)
label_titulo.place(x=100, y=20)

label_nome = Label(frame_esquerda, text="Nome completo:", padx=3,
                   pady=3, relief=FLAT, font="Raleway 12 ", bg=cor_branco, fg=cor_preto)
label_nome.place(x=20, y=100)

entry_nome = Entry(frame_esquerda, relief=FLAT, width=30,
                   font="Raleway 12", bg=cor_brancocaixa, fg=cor_preto)
entry_nome.place(x=20, y=130)


# Data de nascimento
label_data = Label(frame_esquerda, text="Data de nascimento", padx=3,
                   pady=3, relief=FLAT, font="Raleway 12 ", bg=cor_branco, fg=cor_preto)
label_data.place(x=20, y=190)

entry_dia = Entry(frame_esquerda, relief=FLAT, width=7,
                  font="Raleway 12", bg=cor_brancocaixa, fg=cor_preto)
entry_dia.place(x=80, y=220)

entry_mes = Entry(frame_esquerda, relief=FLAT, width=7,
                  font="Raleway 12", bg=cor_brancocaixa, fg=cor_preto)
entry_mes.place(x=240, y=220)

entry_ano = Entry(frame_esquerda, relief=FLAT, width=7,
                  font="Raleway 12", bg=cor_brancocaixa, fg=cor_preto)
entry_ano.place(x=400, y=220)

label_dia = Label(frame_esquerda, text="27",
                  relief=FLAT, font="Raleway 10 italic ", bg=cor_branco, fg=cor_preto)
label_dia.place(x=50, y=221)

label_mes = Label(frame_esquerda, text="10",
                  relief=FLAT, font="Raleway 10 italic ", bg=cor_branco, fg=cor_preto)
label_mes.place(x=210, y=221)

label_ano = Label(frame_esquerda, text="1954",
                  relief=FLAT, font="Raleway 10 italic ", bg=cor_branco, fg=cor_preto)
label_ano.place(x=365, y=221)


# Função

def calcular():
    dia = int(entry_dia.get())
    mes = int(entry_mes.get())
    ano = int(entry_ano.get())
    nome = (entry_nome.get())

    # resutlado somado
    resultado_soma = int(dia + mes + ano)

    # Convertendo para lista:
    lista = [int(a) for a in str(resultado_soma)]

    # somando
    urgencia = sum(lista)
    print(urgencia)
    if urgencia > 9:
        lista2 = [int(a) for a in str(urgencia)]
        urgencia_final = sum(lista2)
        print(urgencia_final)
        if urgencia_final > 9:
            lista3 = [int(a) for a in str(urgencia_final)]
            urgencia_final2 = sum(lista3)
            print(urgencia_final2)

     # tonica fundamental = urgencia + soma da quantidade de letras no nome
    soma_nome = len(nome)
    listanome = [int(a) for a in str(soma_nome)]
    nome_final = sum(listanome)
    print(nome_final)
    if nome_final > 9:
        listanome2 = [int(a) for a in str(nome_final)]
        nome_final2 = sum(listanome2)
        print(nome_final2)
        if nome_final2 > 9:
            listanome3 = [int(a) for a in str(nome_final2)]
            nome_final3 = sum(listanome3)
            print(nome_final3)


# Labels explicativas
lab_urgencia = Label(frame_esquerda, text="Urgência Interior", relief=FLAT,
                     font="Raleway 14 bold", bg=cor_branco, fg=cor_amarelo)
lab_urgencia.place(x=20, y=280)

label_urgencia = Label(frame_esquerda, text="""
'Soma kabalística da data de nascimento,
o dia, mes e ano.'""", relief=FLAT, font="Raleway 10 italic ", bg=cor_branco, fg=cor_preto)
label_urgencia.place(x=200, y=270)


lab_tonica = Label(frame_esquerda, text="Tônica Fundamental", relief=FLAT,
                   font="Raleway 14 bold", bg=cor_branco, fg=cor_amarelo)
lab_tonica.place(x=20, y=345)

label_tonica = Label(frame_esquerda, text="""
'Urgencia Interior, mais a soma Kabalística
do número de letras do nome completo.'""", relief=FLAT, font="Raleway 10 italic ", bg=cor_branco, fg=cor_preto)
label_tonica.place(x=240, y=330)


lab_eventos = Label(frame_esquerda, text="Eventos Kabalisticos", relief=FLAT,
                    font="Raleway 14 bold", bg=cor_branco, fg=cor_amarelo)
lab_eventos.place(x=20, y=410)

label_eventos = Label(frame_esquerda, text="""
'A Lei do Karma se desenvolve com os números.'""", relief=FLAT, font="Raleway 10 italic ", bg=cor_branco, fg=cor_preto)
label_eventos.place(x=220, y=400)


# Calcular

botao_tonica = Button(frame_esquerda, command=calcular, text="Calcular", relief=RAISED, padx=130,
                      overrelief=FLAT, font="Raleway 17 bold", anchor="center", bg=cor_amarelo, fg=cor_branco)
botao_tonica.place(x=60, y=480)


janela.mainloop()

# Frames
