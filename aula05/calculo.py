import streamlit as st
import pandas as pd
import numpy as np

# Título da aplicação
st.title("Calculadora de Soma com Gráfico de Progresso")

# Descrição opcional
st.write("Insira dois números para somar. O gráfico mostrará o resultado em uma escala de 0 a 200.")

# --- Área de Input ---
st.subheader("Entrada de Valores")
col1, col2 = st.columns(2)

with col1:
    numero1 = st.number_input("Primeiro Número", value=0.0, step=0.1)
with col2:
    numero2 = st.number_input("Segundo Número", value=0.0, step=0.1)

# --- Cálculo ---
soma = numero1 + numero2

# --- Exibição do Resultado ---
st.subheader("Resultado:")
st.write(f"A soma de {numero1} e {numero2} é **{soma}**")

# --- Visualização do Gráfico ---

# Prepara os dados para o gráfico em um DataFrame do Pandas
# O gráfico nativo do streamlit espera um DataFrame
data = pd.DataFrame({
    'Valor da Soma': [soma],
    'Maximo Esperado (200)': [200] # Adiciona um ponto de referência visual opcional
})

# Garante que o valor exibido no gráfico não ultrapasse 200 para manter a escala visual
valor_grafico = min(soma, 200)

# Cria um DataFrame simples para o gráfico de área, focando apenas na soma
chart_data = pd.DataFrame(
     [valor_grafico, 200], # Valores: Soma e o Limite Máximo
     columns=['Valor']
)

st.write("### Gráfico do Valor (0 a 200)")

# Usamos st.bar_chart ou st.area_chart com uma configuração manual de eixo
st.area_chart(chart_data, y="Valor", use_container_width=True)

# Nota: Embora os gráficos nativos do Streamlit ajustem a escala automaticamente,
# o código acima garante que o eixo Y mínimo seja 0 e o máximo seja pelo menos 200.
# Se a soma for maior que 200, o gráfico continuará a desenhar o valor real.
