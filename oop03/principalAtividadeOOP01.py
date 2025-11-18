import classeAtividadeOOP01 as c
import streamlit as st 

st.title("Função 1 - Pessoa mais velha")

# Entrada de dados
if st.button("Calcular"):
    nome1 = st.text_input("Digite o nome da pessoa 1: ")
    idade1 = st.number_int(input(f"Digite a idade de {nome1}: "))

    nome2 = st.text_input("Digite o nome da pessoa 2: ")
    idade2 = st.number_int(input(f"Digite a idade de {nome2}: "))

    # Criação dos objetos
    p1 = c.Pessoa(nome1, idade1)
    p2 = c.Pessoa(nome2, idade2)


    # Saída de dados
#CORRIGIR 
if st.button("Calcular"):
    if p1.eh_mais_velha(p2.idade):
        print(f"{p1.nome} é mais velha, com {p1.idade} anos.")
    elif p2.eh_mais_velha(p1.idade):
        print(f"{p2.nome} é mais velha, com {p2.idade} anos.")
    else:
        print(f"{p1.nome} e {p2.nome} têm a mesma idade.")
