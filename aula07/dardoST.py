import streamlit as st
st.title("Simulacao de lancamento de dardo 🎯")
'''O objetivo do aplicativo é mostrar o dado com maior distancia'''

# Entrada de dados
st.header("Inserir as tres distancias lançados pelo jogador.")
coluna1, coluna2, coluna3 = st.columns(3)
with coluna1:
    dardo1 = st.number_input("Distancia do 1 dardo: ", min_value=0)
with coluna2:
    dardo2 = st.number_input("Distancia do 2 dardo: ", min_value=0)
with coluna3:
    dardo3 = st.number_input("Distancia do 3 dardo: ", min_value=0)

# Estrutura de controle de decisao
if (dardo1 > dardo2) and (dardo1 > dardo3):
    dardo_vencedor = "Dardo1"
elif (dardo2 > dardo1) and (dardo2 > dardo3):
    dardo_vencedor = "Dardo2"
else:
    dardo_vencedor = "Dardo3"

# Saida de dados
if st.button("Apresentar resultados dos lançamentos"):
    st.write(f"O dardo com maior distancia e {dardo_vencedor}")
