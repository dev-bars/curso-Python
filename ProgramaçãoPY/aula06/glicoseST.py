import streamlit as st 

st.title("CLASSIFICAÇÃO DE NÍVEIS DE GLICOSE") #Titulo na página
st.markdown( ###Constuir uma tabela com markdown
        """
        | Nivel de glicose | Classificação |
        |------------------|---------------|
        | 0 - 70           |  Hipoglicenica|
        |71 - 100          |  Normal       |
        |101 - 140         |  Pré-diabético|
        |141 ou mais       |  Diabetes     |
"""
)

#Entrada de dados
glicose = st.number_input("Insira o nível de glicose no sangue (mg/dl)", min_value=0)
if st.button("Classificar"): #Botão para classificar o nível de glicose
        if glicose <= 70:
                st.write("Hipoglicemia")
        elif glicose <= 100:
                st.write("Normal")
        elif glicose <= 140:
                st.write("Pré-diabético")
        else:
                st.write("Diabetes")

#Processamento de dados

