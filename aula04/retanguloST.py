import streamlit as st 
# Problema retangulo
st.title("Problema retangulo")

# Entrada de dados
base = st.number_input("Digite a base do retangulo: ")
altura = st.number_input("Digite a altura do retangulo: ")

# Processamento de dados
area = base * altura
perimentro = 2 * base + altura * 2
diagonal = (base**2 + altura**2)**0,5

# Saida de dados
st.write(f"A área do retangulo é: {area}")
st.write(f"O perimetro do retangulo é: {perimentro}")
st.write(f"A diagonal do retangulo é: {diagonal}")