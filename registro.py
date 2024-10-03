import streamlit as st
import pandas as pd
from datetime import date

def grabar_datos(nombre,fecha_nac,tipo):
    if nombre and fecha_nac <= date.today():
        with open('clientes.csv','a', encoding='utf-8') as file:
            file.write(f'{nombre},{fecha_nac},{tipo}\n')
        st.session_state['exito'] = True
    else:
        st.session_state['exito'] = False    

st.set_page_config(
    page_title = 'registro de clientes',
    page_icon = '👨‍🏫')

st.title('registro de clientes')
st.divider()

nombre = st.text_input('Digite el nombre del Cliente',
                       key = 'nombre_cliente')

fecha_nac = st.date_input('fecha de nacimiento',format='DD/MM/YYYY')

tipo = st.selectbox('tipo de cliente',
                    ['persona juridica','persona fisica'])

btn_registro = st.button('registrar',
                         on_click=grabar_datos,
                         args=[nombre,fecha_nac,tipo])

if btn_registro:
    if st.session_state['exito']:
        st.success('Cliente cadastrado con exito!!',
                   icon ='👍')
    else:
        st.error('Hubo un problema en el registro!!',
                    icon='🤔')
            
        
                   
