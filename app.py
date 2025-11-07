import streamlit as st
import pandas as pd
from queries import artilheiro
from db_connection import get_connection
import plotly.express as px

conn = get_connection()

st.title("Estatísticas da Conmebol Libertadores 2025")
st.divider()

col1,col2 = st.columns(2)

with col1:
    st.subheader("Artilharia (Eliminatórias)")
    st.dataframe(artilheiro(conn))

    #Artilheiro ploty_bar
    df_artilheiro = artilheiro(conn) #Create dataframe
    color_artilharia = {
        "Palmeiras":"#0EA300",
        "Racing": "#09b2b8",
        "LDU":"#e40707",
        "Flamengo": "#850505",
        "São Paulo": "#f50035",
        "Botafogo": "#919090"
    }
    fig = px.bar(df_artilheiro,x="jogador",y="gols_no_mata_mata",color="clube",color_discrete_map=color_artilharia, labels={"jogador": "Artilheiros","gols_no_mata_mata":"Gols"})
    st.plotly_chart(fig)
