import streamlit as st
import pandas as pd
from queries import artilheiro,time_pais
from db_connection import get_connection
import plotly.express as px

st.set_page_config(layout="wide") #because wide is better than stretch

conn = get_connection()

st.title("Estatísticas da Conmebol Libertadores 2025 - Eliminatórias")
st.divider()

col1,_,col2 = st.columns([2,0.5,2]) #setting a gap

with col1:
    st.subheader("Artilharia")
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

    st.dataframe(artilheiro(conn))

with col2:
    color_pais = {
        "Argentina":"#09b2b8",
        "Brasil": "#048a0b",
        "Colômbia": "#4CC952",
        "Equador": "#18048a",
        "Paraguai": "#8a0404",
        "Peru": "#464646",
        "Uruguai": "#fffb00",
    }
    traducao = { #Translation because the data is in portuguese
        "Brasil": "Brazil",
        "Argentina": "Argentina",
        "Uruguai": "Uruguay",
        "Chile": "Chile",
        "Paraguai": "Paraguay",
        "Colômbia": "Colombia",
        "Equador": "Ecuador",
        "Peru": "Peru",
        "Bolívia": "Bolivia",
        "Venezuela": "Venezuela"
    }
    st.header("Times por país")
    df_pais = time_pais(conn)
    df_pais["pais_en"] = df_pais["pais"].map(traducao)
    plot = px.choropleth(
        df_pais,locations="pais_en", 
        locationmode="country names", 
        scope="south america",
        hover_data={"clubes":True,"pais_en":False,"pais":False},
        hover_name="pais",
        color="pais",
        color_discrete_map=color_pais,
        labels={"pais_en":"País"}
    )
    st.plotly_chart(plot, width='stretch') #use_container_width will be deprecated

    st.dataframe(time_pais(conn))
    