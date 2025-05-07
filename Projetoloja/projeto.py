import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu





#config iniciais 
st.set_page_config(page_title='Dashboard de Vendas',page_icon='🛒',layout='wide')

#carregar dados
df=pd.read_excel("Vendas.xlsx")


#Filtros
#sideBar
st.sidebar.header("Selecione os filtros")

#filtro por loja
lojas=st.sidebar.multiselect(
        'Lojas',
        #opcoes do filtro
        options=df['ID Loja'].unique(),
        #opcao que vem por padrao
        default=df['ID Loja'].unique(),
        #chave unica
        key='loja'
)

#filtro de produto 
produtos=st.sidebar.multiselect(
    'produtos',
    options=df['Produto'].unique(),
    default=df['Produto'].unique(),
    key='produto'
)
#filtrar o dataframe de acordo com as opcoes selecionadas

df_selecao=df.query('`ID Loja` in @lojas and Produto in @produtos')

#Graficos e funcao

def home():
    st.title('Faturamento das lojas')

    total_vendas= df['Quantidade'].sum()
    media=df["Quantidade"].mean()
    mediana=df['Quantidade'].median()

    total1,total2,total3= st.columns(3)
    with total1:
        #exibir indicadores rapidos
        st.metric("Total Vendido",value=int(total_vendas))
    with total2:
        st.metric("Media por produto",value=f'{media:.1f}')
    with total3:
        st.metric("Mediana de produtos",value=int(mediana))
    st.markdown('---')
      

def graficos():
    #Criar um grafico de barras, mostrando a quantidade de produtos por loja
    fig_barras= px.bar(
        df,
        x='Produto',
        y='Quantidade',
        color='ID Loja',
        barmode='group',
        title="Quantidade de produtos vendidos por loja"

    )

  #grafico de linha,com total de vendas por loja    
    fig_linha= px.line(
        df.groupby(['ID Loja']).sum(numeric_only=True).reset_index(),
        x="ID Loja",
        y='Quantidade',
        title="Total de vendas por loja"
    )

    grafi1,grafi2=st.columns(2)
    with grafi1:
        st.plotly_chart(fig_barras,use_container_width=True)
    with grafi2:
        st.plotly_chart(fig_linha,use_container_width=True)

def sidebar():
    with st.sidebar:
        selecionado=option_menu(
            menu_title="Menu",
            options=['home','graficos'],
            icons=['house','bar-chart'],
            default_index=0
        )    
    if selecionado == 'home':
        home()
        graficos()
    elif selecionado == 'graficos':
        graficos()

sidebar()            