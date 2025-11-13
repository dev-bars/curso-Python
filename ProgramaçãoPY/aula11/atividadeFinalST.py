import streamlit as st 

st.title("Atividade Final")

quantidade = st.number_input("Quantas pessoas serão digitadas: ", step=1)

#Lista
pessoas = []

for i in range(int(quantidade)):
    st.subheader(f"Pessoa {i+1}")
    nome = st.text_input(f"Insira o nome da pessoa: {i+1}")
    idade = st.number_input(f"Idade da pessoa: {i+1}", min_value=0, step=1)
    pessoas.append({"nome": nome, "idade": idade})
    lista = st.write(pessoas)

pessoa = st.write(f"Nome: {nome}, idade: {idade}")