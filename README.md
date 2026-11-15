# 📊 Análisis de Seguros: Visualización con Matplotlib, Seaborn y Streamlit

Este repositorio contiene un proyecto práctico de análisis de datos y visualización utilizando el dataset de costos médicos de seguros de salud (`insurance.csv`). 

El objetivo del proyecto es implementar **5 gráficos clave** utilizando de forma independiente **Matplotlib** y **Seaborn**, para posteriormente construir un **Dashboard interactivo con Streamlit** que permita filtrar y explorar estos mismos gráficos en tiempo real.

---

## 📈 Los 5 Gráficos Analizados

En el proyecto se desarrollan las siguientes representaciones visuales estructuradas tanto en modo estático como interactivo:

1. **Distribución de Edad**: Un histograma interactivo para entender la demografía del dataset.
2. **Edad vs. Cargos Médicos**: Gráfico de dispersión para analizar cómo influyen la edad y el hábito de fumar (`smoker`) en el costo final del seguro.
3. **Distribución de Cargos por Sexo**: Gráfico de caja (boxplot) para comparar la variabilidad de costos entre hombres y mujeres.
4. **Densidad de BMI por Región**: Diagrama de violín para observar la distribución del Índice de Masa Corporal (BMI) según la región geográfica.
5. **Mapa de Calor (Correlación)**: Matriz que calcula y muestra de forma limpia la correlación lineal de Pearson entre todas las variables numéricas.

---

## 📁 Estructura del Repositorio

*   `Visualización_con_Matplotlib,_Seaborn_y_Streamlit.ipynb`: Cuaderno de Jupyter (Google Colab) con todo el código estructurado paso a paso y las visualizaciones generadas estáticamente.
*   `app.py`: Archivo de código Python que implementa el cuadro de mando interactivo en Streamlit.
*   `insurance.csv`: El dataset original con la información del seguro médico.
*   `README.md`: Este archivo de documentación.

---

## 🛠️ Requisitos e Instalación

Para ejecutar el cuaderno y la aplicación localmente en tu computadora, asegúrate de tener instalado Python (versión 3.8 o superior) y corre el siguiente comando en tu terminal para instalar las dependencias necesarias:

```bash
pip install streamlit pandas numpy matplotlib seaborn
```

---

## 🚀 Instrucciones de Uso

### 1. Ejecutar el Dashboard de Streamlit
Para iniciar la aplicación interactiva de Streamlit, clona el repositorio, asegúrate de tener el archivo `insurance.csv` en la misma carpeta que `app.py`, abre la terminal (o PowerShell en Windows) y ejecuta:

```bash
python -m streamlit run app.py
```

### Características de la App de Streamlit:
*   **Filtros en tiempo real**: Ajusta dinámicamente el rango de edad con un *Slider*, selecciona una o varias regiones específicas mediante un *Multiselect*, o segmenta entre fumadores y no fumadores.
*   **Tarjetas de KPIs (Métricas)**: Indicadores de resumen (Promedio de costos, total de registros, BMI promedio) que se recalculan automáticamente conforme aplicas los filtros.
*   **Pestañas (Tabs)**: Navegación intuitiva organizada en:
    *   `Vista de Datos`: Explora el dataset filtrado y sus estadísticas descriptivas.
    *   `Gráficos Matplotlib`: Visualización limpia de los 5 gráficos utilizando Matplotlib nativo.
    *   `Gráficos Seaborn`: Los mismos 5 gráficos estilizados con la librería Seaborn.
