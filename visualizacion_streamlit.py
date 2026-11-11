import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Configuración de la página de Streamlit
st.set_page_config(page_title="Dashboard Comparativo: Matplotlib vs Seaborn vs Streamlit", layout="wide")

st.title("📊 Dashboard Comparativo: Mismo Gráfico en las 3 Tecnologías")
st.markdown("Comparativa exacta de las 5 visualizaciones implementadas con **Matplotlib**, **Seaborn** y **Streamlit (vía Plotly interactivo)**.")

# 1. Cargar el dataset
@st.cache_data
def load_data():
    return pd.read_csv('insurance.csv')

try:
    df = load_data()
    st.success("¡Dataset cargado correctamente!")
except Exception as e:
    st.error(f"No se pudo cargar el archivo 'insurance.csv'. Asegúrate de que esté en la misma carpeta. Error: {e}")
    st.stop()

if st.checkbox("Mostrar las primeras filas del dataset"):
    st.dataframe(df.head())

st.markdown("---")

# =====================================================================
# ANÁLISIS 1: DISTRIBUCIÓN DE EDAD (Histograma)
# =====================================================================
st.header("1️⃣ Distribución de Edad (Histograma)")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Matplotlib")
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.hist(df['age'], bins=20, color='royalblue', edgecolor='black', alpha=0.7)
    ax.set_xlabel('Edad')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)

with col2:
    st.subheader("Seaborn")
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.histplot(df['age'], bins=20, kde=False, color='purple', ax=ax)
    ax.set_xlabel('Edad')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)

with col3:
    st.subheader("Streamlit")
    edades_agrupadas = pd.cut(df['age'], bins=20).value_counts().sort_index()
    edades_agrupadas.index = [str(int(interval.left)) for interval in edades_agrupadas.index]
    st.bar_chart(edades_agrupadas, x_label="Edad", y_label="Frecuencia")

st.markdown("---")

# =====================================================================
# ANÁLISIS 2: EDAD VS CARGOS MÉDICOS (Dispersión)
# =====================================================================
st.header("2️⃣ Edad vs Cargos Médicos (Dispersión)")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Matplotlib")
    fig, ax = plt.subplots(figsize=(4, 3))
    colores = df['smoker'].map({'yes': 'red', 'no': 'blue'})
    ax.scatter(df['age'], df['charges'], c=colores, alpha=0.5, s=20)
    ax.set_xlabel('Edad')
    ax.set_ylabel('Cargos')
    st.pyplot(fig)

with col2:
    st.subheader("Seaborn")
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.scatterplot(data=df, x='age', y='charges', hue='smoker', palette='Set1', alpha=0.6, ax=ax)
    ax.set_xlabel('Edad')
    ax.set_ylabel('Cargos')
    st.pyplot(fig)

with col3:
    st.subheader("Streamlit")
    fig = px.scatter(df, x='age', y='charges', color='smoker')
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =====================================================================
# ANÁLISIS 3: CARGOS POR SEXO (Boxplot)
# =====================================================================
st.header("3️⃣ Cargos por Sexo (Boxplot)")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Matplotlib")
    fig, ax = plt.subplots(figsize=(4, 3))
    cargos_fem = df[df['sex'] == 'female']['charges']
    cargos_masc = df[df['sex'] == 'male']['charges']
    ax.boxplot([cargos_fem, cargos_masc], tick_labels=['Female', 'Male'], patch_artist=True,
                boxprops=dict(facecolor='lightblue', color='blue'))
    ax.set_ylabel('Cargos')
    st.pyplot(fig)

with col2:
    st.subheader("Seaborn")
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.boxplot(data=df, x='sex', y='charges', palette='Pastel1', ax=ax)
    ax.set_xlabel('Sexo')
    ax.set_ylabel('Cargos')
    st.pyplot(fig)

with col3:
    st.subheader("Streamlit")
    fig = px.box(df, x='sex', y='charges', color='sex')
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =====================================================================
# ANÁLISIS 4: BMI POR REGIÓN (Violin Plot)
# =====================================================================
st.header("4️⃣ BMI por Región (Violin Plot)")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Matplotlib")
    fig, ax = plt.subplots(figsize=(4, 3))
    regiones = df['region'].unique()
    datos_bmi = [df[df['region'] == r]['bmi'] for r in regiones]
    ax.violinplot(datos_bmi, showmedians=True)
    ax.set_xticks(range(1, len(regiones) + 1), regiones)
    ax.set_ylabel('BMI')
    st.pyplot(fig)

with col2:
    st.subheader("Seaborn")
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.violinplot(data=df, x='region', y='bmi', palette='Set2', ax=ax)
    st.pyplot(fig)

with col3:
    st.subheader("Streamlit")
    fig = px.violin(df, x='region', y='bmi', color='region')
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =====================================================================
# ANÁLISIS 5: MATRIZ DE CORRELACIÓN (Heatmap)
# =====================================================================
st.header("5️⃣ Matriz de Correlación (Heatmap)")
num_df = df.select_dtypes(include=[np.number])
corr_matrix = num_df.corr()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Matplotlib")
    fig, ax = plt.subplots(figsize=(4, 3))
    corr_vals = corr_matrix.values
    cols = corr_matrix.columns
    im = ax.imshow(corr_vals, cmap='coolwarm', vmin=-1, vmax=1)
    fig.colorbar(im, ax=ax, shrink=0.8)
    ax.set_xticks(range(len(cols)), labels=cols, rotation=45, fontsize=7)
    ax.set_yticks(range(len(cols)), labels=cols, fontsize=7)
    
    for i in range(len(cols)):
        for j in range(len(cols)):
            ax.text(j, i, f"{corr_vals[i, j]:.2f}", ha="center", va="center", 
                     color="black" if abs(corr_vals[i, j]) < 0.5 else "white", fontsize=7)    
    st.pyplot(fig)

with col2:
    st.subheader("Seaborn")
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax, annot_kws={"size": 7})
    ax.tick_params(axis='both', which='major', labelsize=7)
    st.pyplot(fig)

with col3:
    st.subheader("Streamlit")
    fig = px.imshow(
        corr_matrix, 
        text_auto=True, 
        color_continuous_scale='RdBu',
        zmin=-1, 
        zmax=1,
    )
    fig.update_layout(xaxis_title="", yaxis_title="")
    st.plotly_chart(fig, use_container_width=True)