from streamlit import header,write,text_input,button,warning,success,error
from math import sqrt,pow

# Função Python
def calculo(delta):
    valor = (sqrt(delta)) / (2*a)
    return valor

header("Calculadora de Bhaskara")
write("Calculadora de raízes \n de uma equação do segundo grau")
write("ax² + bx + c = 0")

# Entrada de dados
a = text_input("Insira o valor de A:")
b = text_input("Insira o valor de B:")
c = text_input("Insira o valor de C:")

# Processamento de dados
if button("Calcular raizes"):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        delta = pow(b,2) -4 * a * c
        if delta < 0:
            warning(f"A equação não possui raizes reais👍")
        elif delta == 0:
            raiz = (-b + calculo(delta)) / (2*a)
            success(f"A equção possui uma raiz real {raiz}")
        else:
            raiz1 = (-b + calculo(delta)) / (2*a)
            raiz2 = (-b + calculo(delta)) / (2*a)
            success(f"As raizes da equação são \n Raiz 1:{raiz1}, \n Raiz2: {raiz2}")
    except ValueError:
        error("Por favor insira valores válidos")
    except ZeroDivisionError:
        error(f"O valor de 'a' não pode ser zero em uma equação do segundo grau. ")
