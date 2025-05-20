import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título
st.title("Análise Financeira - Despesas e Orçamentos")

# Carregar os dados
df = pd.read_excel("financeiro.xlsx", sheet_name="Despesas")
df_orcamentos = pd.read_excel("financeiro.xlsx", sheet_name="Orcamentos")

# Converter colunas de valor para número, se necessário
df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
df['Trimestre'] = df['Data'].dt.to_period('Q')

# Seletor de setor
setores = df['Setor'].dropna().unique()
setor_selecionado = st.selectbox("Selecione o setor", setores)

# Filtrar os dados
df_setor = df[df['Setor'] == setor_selecionado]

# Gráfico de gastos ao longo do tempo
st.subheader("Gastos Mensais")
df_setor['Mês'] = df_setor['Data'].dt.to_period('M')
gastos_mensais = df_setor.groupby('Mês')['Valor'].sum().reset_index()

st.line_chart(gastos_mensais.rename(columns={'Mês': 'index'}).set_index('index'))

# Gráfico de setores mais caros
st.subheader("Setores com Maior Gasto")
gastos_setores = df.groupby('Setor')['Valor'].sum().sort_values(ascending=False).head(10)
st.bar_chart(gastos_setores)

# Comparar orçamento vs realizado
st.subheader("Orçamento vs Realizado por Mês")
df_orcamentos['Valor_previsto'] = pd.to_numeric(df_orcamentos['Valor_previsto'], errors='coerce')
df_orcamentos['Valor_realizado'] = pd.to_numeric(df_orcamentos['Valor_realizado'], errors='coerce')
df_orcamentos['Mes'] = df_orcamentos['Mes'].astype(int)

comparacao = df_orcamentos.groupby('Mes')[['Valor_previsto', 'Valor_realizado']].sum()
st.line_chart(comparacao)

# Detectar fornecedores com variação anormal
st.subheader("Fornecedores com Variações Anormais")

df_fornecedores = df.groupby('Fornecedor')['Valor'].agg(['mean', 'std'])
df_despesas = df.join(df_fornecedores, on='Fornecedor')
df_despesas['Desvio'] = abs(df_despesas['Valor'] - df_despesas['mean']) > df_despesas['std']

fornecedores_anormais = df_despesas[df_despesas['Desvio'] == True]['Fornecedor'].unique()

if len(fornecedores_anormais) > 0:
    st.write("Fornecedores com variações anormais de custo:")
    st.write(fornecedores_anormais)
else:
    st.write("Nenhuma variação anormal detectada.")
