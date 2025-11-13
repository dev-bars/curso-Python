import PySimpleGUI as sg 
import numpy as np

def main():
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

    numeros = []#Outra lista

    for i in range(n):
        layout = [
            [sg.Text(f"Digite o {i+1}º numero")],
            [sg.Input(key="Campeao")],
            [sg.Button("ok"), sg.Button("cancelar")]
        ]

        janela = sg.Window("Entrada de numeros", layout)

        while True:
            eventos, valores = janela.read()
            if eventos == sg.WIN_CLOSED or eventos == "cancelar":
                janela.close()
                break 
            if eventos == "ok":
                try:
                    num = float(valores["Campeao"])
                    numeros.append(num)
                    break
                except:
                    sg.popup("Insira valores válidos")
    janela.close()

    #Utilização do numpy
    vetor = np.array(numeros)
    soma = np.sum(vetor)
    media = np.mean(vetor)


    #Resultados
    resultado_layout = [
        [sg.Text("Elementos do vetor")],
        [sg.Text(",".join(map(str, vetor)))],
        [sg.Text(f"Soma dos elementos = {soma}")],
        [sg.Text(f"Media dos elementos = {media}")],
        [sg.Button("Fechar")]
    ]

    resultado_janela = sg.Window("Resultado", resultado_layout)

    while True:
        eventoResultado = resultado_janela.read()
        if evento == sg.WIN_CLOSED or "Fechar" in eventoResultado:
            resultado_janela.close()
            break
    resultado_janela.close()

if __name__ == "__main__":
    main()