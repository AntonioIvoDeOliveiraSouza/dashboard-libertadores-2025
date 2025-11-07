import streamlit as st
import pandas as pd
from queries import artilheiro,time_pais,jogador_time
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
    df_artilheiro.rename(columns={'jogador':'Artilheiro','gols_no_mata_mata':'Gols em Mata Mata','clube':'Clube'},inplace=True)
    df_artilheiro = df_artilheiro.style.set_properties(**{'color':'gold'})
    st.dataframe(df_artilheiro,hide_index=True)

    st.divider()
    #JOGADORES
    st.subheader("Goleadores")

    df_jogador = jogador_time(conn)
    df_jogador.rename(columns={'clube':'Clube','jogador':'Jogador','gols':'Gols marcados'},inplace=True)
    
    st.dataframe(df_jogador,hide_index=True)

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

    df_pais = df_pais.drop(columns=["pais_en"])
    st.dataframe(df_pais,hide_index=True)
    