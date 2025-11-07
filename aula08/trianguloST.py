import streamlit as st 

st.title("Verificação de triangulo e cálculo de perimetro ou área")

#Entrada de dados
valorA = st.number_input("Digite o valor de A: ", min_value=0)
valorB = st.number_input("Digite o valor de B: ", min_value=0)
valorC = st.number_input("Digite o valor de C: ", min_value=0)

perimetro = (valorA + valorB + valorC)
area = ((valorA + valorB) * valorC) / 2

#Processamento de dados
def calculo(valorA,valorB,valorC):
    if (valorA + valorB > valorC) and (valorA + valorC > valorB) and (valorB + valorC > valorA):
        resultado = st.write(f"É um triangulo! Perimetro = {perimetro}")
    else:
        resultado = st.write(f"Não é um triangulo! A área é = {area}")

#Saida de dados
if st.button("Calcular"):
    st.write(f"{calculo(valorA,valorB,valorC)}")