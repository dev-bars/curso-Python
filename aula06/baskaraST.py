import streamlit as st 
import math as mt
st.header("Calculadora de Bhaskara")
st.write("Calculadora de raízes \n de uma equação do segundo grau")
st.write("ax² + bx + c = 0")

# Entrada de dados
a = st.text_input("Insira o valor de A:")
b = st.text_input("Insira o valor de B:")
c = st.text_input("Insira o valor de C:")

# Processamento de dados
if st.button("Calcular raizes"):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        delta = b**2 -4*a*c
        if delta < 0:
            st.warning(f"A equação possui uma raiz real: {raiz}")
        elif delta == 0:
            raiz = (-b + mt.sqrt(delta)) / (2*a)
            st.success(f"As raízes da equação são \n Raiz 1: {raiz1} \n Raiz 2: {raiz2}")
        else:
            raiz1 = (-b + mt.sqrt(delta)) / (2*a)
            raiz2 = (-b + mt.sqrt(delta)) / (2*a)
            st.success(f"As raizes da equação são \n Raiz 1:{raiz1}, \n Raiz2: {raiz2}")
    except:
        st.error("Por favor insira valores válidos")
