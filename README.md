# Dashboard Comparativo de Visualización de Datos: Matplotlib vs Seaborn vs Streamlit

## 📌 Descripción de la Tarea
Este proyecto consiste en el desarrollo de una aplicación web interactiva utilizando **Streamlit**, cuyo objetivo principal es realizar un Análisis Exploratorio de Datos (EDA) sobre un conjunto de datos de seguros médicos (`insurance.csv`). 

Para cada uno de los **5 análisis estadísticos** planteados, se comparan **tres formas diferentes de visualización**:
1. **Matplotlib**: Gráficos estáticos básicos y personalizados.
2. **Seaborn**: Gráficos estadísticos estilizados y avanzados.
3. **Streamlit / Plotly**: Componentes interactivos nativos integrados en la aplicación web.

Las visualizaciones incluidas son:
1. **Histograma de Distribución de Edad**
2. **Gráfico de Dispersión (Edad vs Cargos Médicos)**
3. **Diagrama de Cajas (Cargos Médicos por Sexo)**
4. **Gráfico de Violín (Distribución de BMI por Región)**
5. **Matriz de Correlación / Mapa de Calor (Heatmap con valores numéricos)**

---

## 🚀 Guía de Instalación y Ejecución

### Requisitos Previos
* Tener instalado **Python** (versión 3.8 o superior).

### Pasos a seguir en la Terminal de VS Code:

1. **Abrir la terminal integrada:**
   En Visual Studio Code, ve al menú superior y selecciona `Terminal` > `New Terminal` (o usa el atajo `` Ctrl + ` ``). Asegúrate de que la ruta actual de la terminal sea la carpeta raíz del proyecto clonado.

2. **Crear un entorno virtual (Recomendado):**
   Para mantener las dependencias aisladas y limpias, crea un entorno virtual ejecutando:
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual:**
   * **En Windows (Command Prompt / CMD):**
     ```bash
     venv\Scripts\activate.bat
     ```
   * **En Windows (PowerShell):**
     ```bash
     venv\Scripts\Activate.ps1
     ```
   * **En macOS / Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Instalar las dependencias necesarias:**
   Instala las librerías requeridas ejecutando el siguiente comando en la terminal:
   ```bash
   pip install streamlit pandas numpy matplotlib seaborn plotly
   ```

5. **Verificar los archivos del proyecto:**
   Asegúrate de que en la carpeta raíz del proyecto se encuentren los siguientes dos archivos indispensables:
   * `visualizacion_streamlit.py` (Script principal de la aplicación)
   * `insurance.csv` (Dataset de datos)

6. **Ejecutar la aplicación de Streamlit:**
   Lanza el servidor local con el siguiente comando:
   ```bash
   python -m streamlit run visualizacion_streamlit.py
   ```

7. **Visualizar el Dashboard:**
   Automáticamente se abrirá una pestaña en tu navegador web predeterminado con la dirección `http://localhost:8501` mostrando la aplicación interactiva completa.