import streamlit as st 
import math as mt 

#Problemas medidas
TITULO = "Cálculo de área de um quadrado, triangulo e trapezio"
st.markdown(f"<h1 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)

# Entrada de dados
medidaA = st.number_input("Inserir a medida A: ")
medidaB = st.number_input("Inserir a medida B: ")
medidaC = st.number_input("Inserir a medida C: ")

# Processamento de dados
areaQuadrado = mt.pow(medidaA,2)
areaTriangulo = (medidaA * medidaB) / 2
areaTrapezio = ((medidaA + medidaC)) *medidaB / 2

# Saida de dados
st.write(f"A área do quadrado é: {areaQuadrado:.4f}")
st.write(f"A área do triangulo é: {areaTriangulo:.4f}")
st.write(f"A área do trapezio é: {areaTrapezio:.4f}")