import streamlit as st 

def Celsius_Fahrenhet(t):
    return(temp * 1.8) + 32

def Celsius_Kelvin(t):
    return(temp + 273.15)

def Fahrenhet_Celsius(t):
    return(temp - 32) * 5/9

def Fahrenhet_Kelvin(t):
    return Fahrenhet_Celsius(t) + 273.15

def Kelvin_Celsius(t):
    return temp - 273.15

def Kelvin_Fahrenhet(t):
    return Celsius_Fahrenhet(Kelvin_Celsius(t))


#Problema temperatura
st.sidebar.title("Conversor de temperatura")
st.title("Conversor de Temperatura")
st.sidebar.markdown("Converte a temperatura entre Celsius, Fahrenheit e Kelvin")
celsius_selecionado = st.sidebar._checkbox("Celsius",key="temp_celsius")
fahrenheit_selecionado = st.sidebar._checkbox("Fahrenheit",key="temp_fahrenheit")
kelvin_selecionado = st.sidebar._checkbox("Kelvin",key="temp_kelvin")

#Entrada de dados
temp = st.number_input("Valor da temperatura",format="%.2f",step=1.0)



# Processamento de dados
if st.button("Converter",icon="🌡"):
    if celsius_selecionado:
        st.write(f"{temp}ºC em Fahrenheit: {Celsius_Fahrenhet(temp):.2f}ºF")
        st.write(f"{temp}ºC em Kelvin: {Celsius_Kelvin(temp):.2f}K")
    elif fahrenheit_selecionado:
        st.write(f"{temp}ºF em Celsius: {Fahrenhet_Celsius(temp):.2f}ºC")
        st.write(f"{temp}ºF em Kelvin: {Fahrenhet_Kelvin(temp):.2f}K")
    elif kelvin_selecionado:
        st.write(f"{temp}ºF em Celsius: {Kelvin_Celsius(temp):.2f}ºC")
        st.write(f"{temp}ºF em Fahrenheit: {Kelvin_Fahrenhet(temp):.2f}F")      