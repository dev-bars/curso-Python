import streamlit as st 
import math as mt 
# Problema retangulo
TITULO = "Problema Retangulo"
st.title("TITULO")

# Entrada de dados
base = st.number_input("Digite a base do retangulo: ", min_value=0.0, format="%.1f")
altura = st.number_input("Digite a altura do retangulo: ", min_value=0.0, format="%.1f")

# Processamento de dados
area = base * altura
perimentro = 2 * base + altura * 2
# diagonal = (base**2 + altura**2)**0,5
x = mt.pow(base,2) + mt.pow(altura,2)
diagonal = mt.sqrt(x)

# Saida de dados
st.write(f"A área do retangulo é: {area:.1f}")
st.write(f"O perimetro do retangulo é: {perimentro:.1f}")
st.write(f"A diagonal do retangulo é: {diagonal:.1f}") 