import streamlit as st 
#Problema duração de tempo
TITULO = ("Calculadora de duração de tempo")
st.title(TITULO)

st.set_page_config(page_title="tempo")
st.set_page_config(page_icon="b")

# Entrada de dados
tempo = st.number_input("Digite o tempo em segundos: ", min_value=0, step=1, help="Insira a duração em segundos para converter em horas, minutos e segundos")

# Processamento de dados
horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60

# Saida de dados
st.write(f"{horas:.2f} horas, {minutos:.2f} minutos {segundos:.2f} e segundos")
