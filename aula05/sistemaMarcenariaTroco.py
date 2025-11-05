import streamlit as st 
#Problema troco Marcenaria

st.set_page_config(page_title="marcenaria")
st.set_page_config(page_icon="m")

TITULO = ("Sistema de troco - Marcenaria")
st.title(TITULO)

# Entrada de dados
precoUnitario = st.number_input("Digite o valor unitário do item: ", min_value=0, help="Insira o valor em reais")
quantidadeComprada = st.number_input("Digite a quantidade: ", min_value=0, step=1, help="Insira a quantidade da compra")
dinheiroRecebido = st.number_input("Valor dado pelo cliente: ", min_value=0, help="Insira o valor em reais")

# Processamento de dados
valorTotal = precoUnitario * quantidadeComprada
troco = dinheiroRecebido - valorTotal

# Saida de dados
st.write(f"O valor do troco é: R$ {troco:.2f}")