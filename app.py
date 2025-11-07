import streamlit as st
import pandas as pd
from queries import artilheiro,time_pais,jogador_time,gol_mandante,gol_visitante
from db_connection import get_connection
import plotly.express as px

#Setting dataframes
conn = get_connection()
df_artilheiro = artilheiro(conn) #Create dataframe
df_jogador = jogador_time(conn)
df_pais = time_pais(conn)
df_mandante = gol_mandante(conn)
df_visitante = gol_visitante(conn)

st.set_page_config(layout="wide") #because wide is better than stretch

st.title("Estatísticas da Conmebol Libertadores 2025 - Eliminatórias")
st.divider()

col1,col2,col3 = st.columns(3)
with col1:
    st.metric("Total de Gols",df_artilheiro['gols_no_mata_mata'].sum())
with col2:
    st.metric("Média por jogador",df_artilheiro['gols_no_mata_mata'].mean())
with col3:
    st.metric("Artilheiro Líder",df_artilheiro.iloc[0]['jogador'])

tab1,tab2,tab3,tab4 = st.tabs(["Artilharia","Goleadores","Clubes","Gols-Casa/Visitante"],default="Clubes")

with tab1:
    st.subheader("Artilharia")
    #Artilheiro ploty_bar
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

with tab2:
    #JOGADORES
    st.subheader("Goleadores")

    df_jogador.rename(columns={'clube':'Clube','jogador':'Jogador','gols':'Gols marcados'},inplace=True)
    
    st.dataframe(df_jogador,hide_index=True)

with tab3:
    st.header("Times por país")
    col1,col2 = st.columns(2)
    with col1:
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
    with col2:
        df_pais = df_pais.drop(columns=["pais_en"])
        st.dataframe(df_pais,hide_index=True)

with tab4:
    #COMPARISON VISITOR-HOME
    st.subheader("Gols como Mandantes/Visitantes")

    color_gols={
        "gols_como_mandante":"#65b440",
        "gols_como_visitante": "#b92c2c"
    }
    merge_df = pd.merge(df_mandante,df_visitante, on='clube', how='outer') #merging both tables
    merge_df = merge_df.fillna(value=0) #treating null cells
    fig = px.bar(
        merge_df,
        x='clube',
        y=['gols_como_mandante','gols_como_visitante'],
        barmode='group',
        color_discrete_map=color_gols,
        labels={'clube':'Clubes','value':'Gols'}
    )
    st.plotly_chart(fig)