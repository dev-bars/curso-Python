import streamlit as st

#Apresentaçao de gráfico exibindo lançamento
def grafico(datsu1,datsu2,datsu3):
    st.area_chart([0,1,2,3,4,5,6, datsu1], use_container_width=True,height=100,color="#e3e30a")
    st.area_chart([0,1,2,3,4,5,6, datsu2], use_container_width=True,height=100,color="#e30a0a")    
    st.area_chart([0,1,2,3,4,5,6, datsu3], use_container_width=True,height=100,color="#3d0ae3")


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
elif (dardo3 > dardo1) and (dardo3 > dardo2):
    dardo_vencedor = "Dardo3"
elif (dardo1 == dardo2) or (dardo1 == dardo3) or (dardo2==dardo3):
    dardo_vencedor = "Empate"

# Estrutura de dados com MAX (argumento que calcula maior valor)
maiorDiscancia = max(dardo1,dardo2,dardo3)

# Saida de dados
if st.button("Apresentar resultados dos lançamentos"):
    st.write(f"O dardo com maior distancia e {dardo_vencedor}")

if st.button("Apresentar resultados de valores dos lançamentos"):
    if dardo_vencedor == "Empate":
        st.write("Houve empate")
    else:
        st.write(f"O dardo com maior distancia é o {dardo_vencedor} com {maiorDiscancia} metros")
        grafico(dardo1,dardo2,dardo3)
