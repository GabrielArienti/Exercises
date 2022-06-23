from ast import Break
import random
import PySimpleGUI as sg
import os


class PassGen:
    def _init_(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
             sg.Input(key='Site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(10, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
                range(30)), key='total_chars', default_value=1, size=(3, 1))]
            [sg.Output(size=(32, 5))]
            [sg.Button('Gerar Senha')]
        ]
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break

    def salvar_senha(self):
        pass


gen = PassGen()
gen.Iniciar()
