import PySimpleGUI as sg 
import numpy as np

#Lista para guardar o layout da janela
layout = [
    [sg.Text("Digite a quantidade de numeros:")],
    #Entrada de dados
    [sg.Input(key="N")],
    [sg.Button("ok"), sg.Button("cancelar")]
]

#Variáveis
janela = sg.Window("Calculadora", layout)

while True:
    evento, valores = janela.read() #Variáveis usadas no While
    if evento == sg.WIN_CLOSED or evento == "cancelar":
        janela.close()
        break
    elif evento == "ok":
        try:
            n = int(valores["N"])
            if n <= 0:
                sg.popup("Digite um valor positivo")
                continue
            break
        except:
            sg.popup("Insira um valor válido")

janela.close()

            