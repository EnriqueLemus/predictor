import streamlit as st
import pandas as pd 
import pickle

st.header("Reto Predictor App")

st.write("""
## Predicción Ileso en Reto
""")

col16, col17, col18, col19 = st.columns(4)

col17.caption('Enrique Lemus')
col17.caption('Javier Morales')
col18.caption('Jessica Vazquez')
col18.caption('Sebastian Escobedo')


st.sidebar.header('Elige los valores para predecir')


def user_input():
    anio = st.sidebar.slider('Año', 2015, 2018, 2021)
    mes = st.sidebar.slider('mes', 0, 5, 11)
    dia = st.sidebar.slider('dia', 1, 15, 31)
    dia_sem = st.sidebar.slider('diasem', 0, 3, 5, 6)
    clave_mun = st.sidebar.slider('clave_num', 39, 60, 120)
    mun = st.sidebar.slider('mun', 0, 3, 15)
    herido = st.sidebar.selectbox('herido', [0, 1, 2])
    ibaen_atro = st.sidebar.slider('ibaen_atro', 0, 10, 20)
    num_mes = st.sidebar.slider('num_mes', 1, 5, 12)
    rango_hora = st.sidebar.slider('rango_hora', 0, 12, 24)
    tipo_accidente = st.sidebar.slider('tipo_accidente', 0, 7, 14)
    rango_edad = st.sidebar.slider('rango_edad', 0, 3, 6)
    tipo_usuario = st.sidebar.selectbox('tipo_usuario', [0, 1, 2])
    sexo = st.sidebar.selectbox('Sexo', [0, 1, 2])
    
    data = {'anio': anio,
            'mes': mes,
            'dia': dia, 
            'dia_sem': dia_sem, 
            'clave_mun': clave_mun, 
            'mun': mun,
            'herido': herido,
            'ibaen_atro': ibaen_atro,
            'num_mes': num_mes,
            'rango_hora': rango_hora, 
            'tipo_accidente': tipo_accidente,
            'rango_edad': rango_edad,
            'tipo_usuario': tipo_usuario,
            'sexo': sexo}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input()

st.subheader('User Input')
st.write(df)

# Load Trained Model
filename = 'model.sav'
model = pickle.load(open(filename, 'rb'))

prediction = model.predict(df)

st.subheader('Predicción: ')
st.write('0 = No ileso')
st.write('1 = Ileso')

target_names = ["1", "0"]
st.write('Resultado predicción: ' + target_names[prediction[0]])
