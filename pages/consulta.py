import streamlit as st
import pandas as pd

datos = pd.read_csv('clientes.csv')

st.title('Clientes Registrados')
st.divider()

st.dataframe(datos)
