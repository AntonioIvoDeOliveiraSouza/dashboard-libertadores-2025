import streamlit as st
import pandas as pd
from queries import artilheiro
from db_connection import get_connection

conn = get_connection()

st.title("Estatísticas")
st.dataframe(artilheiro(conn))