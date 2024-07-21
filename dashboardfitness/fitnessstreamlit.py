# Conceptos básicos de Python para datos de fitness
pasos_diarios = 10000
distancia_recorrida = 7.5
calorias_quemadas = 2500

print(f"Hoy has dado {pasos_diarios} pasos, recorrido {distancia_recorrida} km y quemado {calorias_quemadas} calorías.")

#Clase 2
# Listas y diccionarios para datos de fitness
pasos_semana = [8000, 10000, 9500, 11000, 9000, 12000, 7500]
actividades = {
    "Correr": 30,
    "Caminar": 60,
    "Ciclismo": 45
}

print("Pasos esta semana:", pasos_semana)
print("Minutos por actividad:", actividades)

#clase 3 
import pandas as pd

# Cargar datos
df = pd.read_csv('C:/Users/admin/OneDrive/Documentos/aprende_programando/dataAnalitycsConPython/dailyActivity_merged.csv')
print(df.head())
print(df.info())

#clase 4
import pandas as pd

# Cargar y preparar datos
df = pd.read_csv('C:/Users/admin/OneDrive/Documentos/aprende_programando/dataAnalitycsConPython/dailyActivity_merged.csv')
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])
df['DayOfWeek'] = df['ActivityDate'].dt.day_name()

# Asegurar tipos de datos correctos
df['TotalSteps'] = pd.to_numeric(df['TotalSteps'], errors='coerce')
df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')

print(df.dtypes)
print(df.isnull().sum())

#clase 5

import pandas as pd

df = pd.read_csv('C:/Users/admin/OneDrive/Documentos/aprende_programando/dataAnalitycsConPython/dailyActivity_merged.csv')
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])

# Estadísticas básicas
print("Promedio de pasos diarios:", df['TotalSteps'].mean())
print("Calorías promedio quemadas:", df['Calories'].mean())
print("Distancia total promedio:", df['TotalDistance'].mean())

# Actividad por tipo
actividad_promedio = df[['VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes']].mean()
print("\nPromedio de minutos por tipo de actividad:")
print(actividad_promedio)

#clase 6
import streamlit as st
import pandas as pd

st.title('Mi Primera App de Fitness con Streamlit')

df = pd.read_csv('C:/Users/admin/OneDrive/Documentos/aprende_programando/dataAnalitycsConPython/dailyActivity_merged.csv')
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])

st.write("Datos de actividad diaria:")
st.dataframe(df.head())

st.write(f"Total de registros: {len(df)}")

#clase 7
import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Visualizaciones de Datos de Fitness')

df = pd.read_csv('C:/Users/admin/OneDrive/Documentos/aprende_programando/dataAnalitycsConPython/dailyActivity_merged.csv')
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])

# Gráfico de línea para pasos totales
fig_steps = px.line(df, x='ActivityDate', y='TotalSteps', title='Pasos Diarios')
st.plotly_chart(fig_steps)

# Gráfico de barras para calorías
fig_calories = px.bar(df, x='ActivityDate', y='Calories', title='Calorías Quemadas por Día')
st.plotly_chart(fig_calories)

#clase 8
import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Dashboard Interactivo de Fitness')

df = pd.read_csv('C:/Users/admin/OneDrive/Documentos/aprende_programando/dataAnalitycsConPython/dailyActivity_merged.csv')
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])

metric = st.selectbox('Elige una métrica', ['TotalSteps', 'TotalDistance', 'Calories'])

fig = px.line(df, x='ActivityDate', y=metric, title=f'{metric} a lo largo del tiempo')
st.plotly_chart(fig)

date_range = st.date_input('Selecciona un rango de fechas', [df['ActivityDate'].min(), df['ActivityDate'].max()])

#clase 9
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title('Dashboard Avanzado de Fitness')

df = pd.read_csv('C:/Users/admin/OneDrive/Documentos/aprende_programando/dataAnalitycsConPython/dailyActivity_merged.csv')
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])

col1, col2 = st.columns(2)

with col1:
    st.subheader('Métricas Diarias')
    metric = st.selectbox('Elige una métrica', ['TotalSteps', 'TotalDistance', 'Calories'])
    fig = px.line(df, x='ActivityDate', y=metric)
    st.plotly_chart(fig)

with col2:
    st.subheader('Distribución de Actividad')
    activity_data = df[['VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes']].sum()
    fig_pie = px.pie(values=activity_data.values, names=activity_data.index)
    st.plotly_chart(fig_pie)

st.subheader('Estadísticas Resumidas')
st.write(df.describe())