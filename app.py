import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------
# CONFIGURACIÓN GENERAL DE LA APP
# -------------------------------------------------

st.set_page_config(
    page_title="Bank Marketing EDA",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------
# ESTILOS PERSONALIZADOS
# -------------------------------------------------

st.markdown("""
<style>

.main-title {
    font-size:40px;
    font-weight:700;
    color:#1f4e79;
}

.section-title {
    font-size:24px;
    font-weight:600;
    color:#1f4e79;
}

.box-style {
    background-color:#2c3e50;
    padding:20px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# SIDEBAR - MENÚ PRINCIPAL
# -------------------------------------------------

st.sidebar.title("📊 Menú de Navegación")

menu = st.sidebar.selectbox(
    "Menú",
    [
        "Home",
        "Carga del Dataset",
        "Análisis Exploratorio (EDA)",
        "Conclusiones"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Aplicación desarrollada con Streamlit para análisis exploratorio de datos.")


# -------------------------------------------------
# MÓDULO 1 - HOME
# -------------------------------------------------

if menu == "Home":

    st.markdown('<p class="main-title">Análisis Exploratorio de Datos - Bank Marketing</p>', unsafe_allow_html=True)

    st.markdown("---")

    # Tabs para organizar información
    tab1, tab2, tab3 = st.tabs(["📌 Proyecto", "📂 Dataset", "⚙ Tecnologías"])

    # -------------------------------------------------
    # TAB 1 - PRESENTACIÓN DEL PROYECTO
    # -------------------------------------------------

    with tab1:

        st.markdown('<p class="section-title">Objetivo del Proyecto</p>', unsafe_allow_html=True)

        col1, col2 = st.columns([2,1])

        with col1:
            st.markdown("""
            <div class="box-style">
            Esta aplicación interactiva tiene como objetivo realizar un 
            <b>Análisis Exploratorio de Datos (EDA)</b> sobre el dataset 
            <b>Bank Marketing</b>.

            A través de diferentes herramientas de análisis y visualización,
            se busca comprender mejor la información disponible, identificar
            patrones relevantes y obtener una visión general de los datos.

            El enfoque del proyecto está orientado a explorar y comprender
            los datos, más que a construir modelos predictivos.
            </div>
            """, unsafe_allow_html=True)

    # -------------------------------------------------
    # TAB 2 - INFORMACIÓN DEL DATASET
    # -------------------------------------------------

    with tab2:

        st.markdown('<p class="section-title">Descripción del Dataset</p>', unsafe_allow_html=True)

        st.markdown("""
        <div class="box-style">
        El dataset <b>Bank Marketing</b> contiene información relacionada con
        campañas de marketing realizadas por una institución bancaria.

        Los datos incluyen características demográficas de los clientes,
        información sobre las interacciones durante campañas de contacto
        y el resultado obtenido respecto a la suscripción de un producto
        financiero ofrecido por el banco.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Variables generales del dataset")

        st.write("""
        - Información demográfica del cliente  
        - Información laboral y financiera  
        - Historial de contacto con campañas de marketing  
        - Resultado de la campaña (suscripción o no)
        """)

    # -------------------------------------------------
    # TAB 3 - TECNOLOGÍAS UTILIZADAS
    # -------------------------------------------------

    with tab3:

        st.markdown('<p class="section-title">Tecnologías Utilizadas</p>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.info("🐍 Python")
            st.write("Lenguaje principal para el análisis y desarrollo de la aplicación.")

        with col2:
            st.info("🐼 Pandas / NumPy")
            st.write("Manipulación de datos y cálculos numéricos.")

        with col3:
            st.info("📊 Matplotlib / Seaborn")
            st.write("Visualización de datos para el análisis exploratorio.")

        st.markdown("---")

        st.success("Framework de la aplicación: Streamlit")


    # -------------------------------------------------
    # INFORMACIÓN DEL AUTOR
    # -------------------------------------------------

    st.markdown("---")

    st.markdown('<p class="section-title">Autor del Proyecto</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([1,2])

    with col1:
        st.metric("Año", "2026")

    with col2:
        st.write("""
        **Nombre:** 👨‍💻 Omar Anthony Poma Vega  
        **Curso:** Especialización en Python for Analytics  
        """)

# -------------------------------------------------
# MÓDULO 2 - CARGA DEL DATASET
# -------------------------------------------------

elif menu == "Carga del Dataset":

    st.markdown('<p class="main-title">Carga del Dataset</p>', unsafe_allow_html=True)

    st.markdown("""
    En esta sección se carga el archivo **Bank Marketing dataset** que será utilizado
    para realizar el análisis exploratorio de datos en los siguientes módulos.
    """)

    st.markdown("---")

    # -------------------------------------------------
    # CARGA DEL ARCHIVO
    # -------------------------------------------------

    uploaded_file = st.file_uploader(
        "Cargar archivo CSV",
        type=["csv"]
    )

    # -------------------------------------------------
    # VALIDACIÓN DE CARGA
    # -------------------------------------------------

    if uploaded_file is not None:

        try:

            import pandas as pd

            df = pd.read_csv(uploaded_file, sep=";")

            # Guardar dataset para otros módulos
            st.session_state["dataset"] = df

            st.success("Archivo cargado correctamente")

            st.markdown("---")

            # -------------------------------------------------
            # INFORMACIÓN GENERAL DEL DATASET
            # -------------------------------------------------

            filas, columnas = df.shape

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Número de filas", filas)

            with col2:
                st.metric("Número de columnas", columnas)

            st.markdown("---")

            # -------------------------------------------------
            # VISTA PREVIA DEL DATASET
            # -------------------------------------------------

            st.subheader("Vista previa del dataset")

            st.dataframe(df.head())

            st.info("Se muestran las primeras 5 filas del dataset cargado.")

            st.markdown("---")

            # -------------------------------------------------
            # INFORMACIÓN DE COLUMNAS
            # -------------------------------------------------

            st.subheader("Columnas del dataset")

            columnas_df = df.columns.tolist()

            st.write(columnas_df)

        except Exception as e:

            st.error("Error al leer el archivo. Verifique que el formato sea correcto.")


    else:

        st.warning("Por favor cargue un archivo CSV para continuar.")

        st.stop()

# -------------------------------------------------
# MÓDULO 3 - ANALISIS DEL DATASET
# -------------------------------------------------
elif menu == "Análisis Exploratorio (EDA)":

    st.title("📊 Análisis Exploratorio de Datos (EDA)")

    # -----------------------------------------------------
    # VALIDACIÓN OBLIGATORIA
    # -----------------------------------------------------

    if "dataset" not in st.session_state:
        st.warning("⚠️ Primero debe cargar el dataset en el módulo 'Carga del Dataset'")
        st.stop()

    df = st.session_state["dataset"]

    # -----------------------------------------------------
    # CLASE DATA ANALYZER (POO)
    # -----------------------------------------------------

    class DataAnalyzer:

        def __init__(self, dataframe):
            self.df = dataframe

        def info_dataset(self):
            return self.df.dtypes

        def null_values(self):
            return self.df.isnull().sum()

        def classify_variables(self):
            numeric = self.df.select_dtypes(include=["int64","float64"]).columns.tolist()
            categorical = self.df.select_dtypes(include=["object"]).columns.tolist()
            return numeric, categorical

        def descriptive_stats(self):
            return self.df.describe()

        def mode_values(self):
            return self.df.mode().iloc[0]

    analyzer = DataAnalyzer(df)

    numeric_cols, categorical_cols = analyzer.classify_variables()

    # -----------------------------------------------------
    # SIDEBAR (Widget obligatorio)
    # -----------------------------------------------------

    st.sidebar.subheader("Filtros del análisis")

    age_filter = st.sidebar.slider(
        "Filtrar rango de edad",
        int(df["age"].min()),
        int(df["age"].max()),
        (int(df["age"].min()), int(df["age"].max()))
    )

    show_data = st.sidebar.checkbox("Mostrar dataset filtrado")

    df_filtered = df[(df["age"] >= age_filter[0]) & (df["age"] <= age_filter[1])]

    if show_data:
        st.dataframe(df_filtered)

    # -----------------------------------------------------
    # TABS (10 ÍTEMS)
    # -----------------------------------------------------

    tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10 = st.tabs([
        "Item 1",
        "Item 2",
        "Item 3",
        "Item 4",
        "Item 5",
        "Item 6",
        "Item 7",
        "Item 8",
        "Item 9",
        "Item 10"
    ])

    # -----------------------------------------------------
    # ITEM 1
    # -----------------------------------------------------

    with tab1:

        st.header("Ítem 1: Información general del dataset")

        col1,col2 = st.columns(2)

        with col1:
            st.subheader("Tipos de datos")
            st.dataframe(analyzer.info_dataset())

        with col2:
            st.subheader("Conteo de valores nulos")
            st.dataframe(analyzer.null_values())

        st.write("Dimensiones del dataset:", df.shape)

    # -----------------------------------------------------
    # ITEM 2
    # -----------------------------------------------------

    with tab2:

        st.header("Ítem 2: Clasificación de variables")

        col1,col2 = st.columns(2)

        with col1:
            st.subheader("Variables Numéricas")
            st.write(numeric_cols)
            st.write("Cantidad:", len(numeric_cols))

        with col2:
            st.subheader("Variables Categóricas")
            st.write(categorical_cols)
            st.write("Cantidad:", len(categorical_cols))

    # -----------------------------------------------------
    # ITEM 3
    # -----------------------------------------------------

    with tab3:

        st.header("Ítem 3: Estadísticas descriptivas")

        st.dataframe(analyzer.descriptive_stats())

        st.subheader("Medidas estadísticas")

        media = df[numeric_cols].mean()
        mediana = df[numeric_cols].median()
        moda = analyzer.mode_values()

        col1,col2,col3 = st.columns(3)

        with col1:
            st.write("Media")
            st.dataframe(media)

        with col2:
            st.write("Mediana")
            st.dataframe(mediana)

        with col3:
            st.write("Moda")
            st.dataframe(moda)

        st.info("Interpretación: estas medidas permiten entender el comportamiento central y la dispersión de los datos.")

    # -----------------------------------------------------
    # ITEM 4
    # -----------------------------------------------------

    with tab4:

        st.header("Ítem 4: Análisis de valores faltantes")

        missing = analyzer.null_values()

        st.subheader("Conteo de valores nulos por variable")

        st.dataframe(missing)

        st.divider()

        st.subheader("Visualización de valores faltantes")

        fig, ax = plt.subplots(figsize=(8,6))

        missing.sort_values().plot(
            kind="barh",
            color="#1976D2",
            ax=ax
        )

        ax.set_xlabel("Cantidad de valores nulos")
        ax.set_ylabel("Variables")
        ax.set_title("Valores faltantes por columna")

        st.pyplot(fig)

        st.info("Discusión: este análisis permite identificar si existen columnas con valores faltantes que puedan afectar los análisis posteriores.")

    # -----------------------------------------------------
    # ITEM 5
    # -----------------------------------------------------

    with tab5:

        st.header("Ítem 5: Distribución de variables numéricas")

        variable = st.selectbox("Seleccione una variable numérica", numeric_cols)

        fig,ax = plt.subplots()

        sns.histplot(df_filtered[variable], kde=True, ax=ax)

        ax.set_title(f"Distribución de {variable}")

        st.pyplot(fig)

        st.info("Interpretación visual: el histograma permite observar la forma de la distribución y detectar posibles sesgos o concentraciones.")

    # -----------------------------------------------------
    # ITEM 6
    # -----------------------------------------------------

    with tab6:

        st.header("Ítem 6: Análisis de variables categóricas")

        variable = st.selectbox("Seleccione variable categórica", categorical_cols)

        conteo = df_filtered[variable].value_counts()

        col1,col2 = st.columns(2)

        with col1:

            fig,ax = plt.subplots()

            sns.barplot(x=conteo.index, y=conteo.values, ax=ax)

            plt.xticks(rotation=45)

            st.pyplot(fig)

        with col2:

            st.subheader("Proporciones (%)")

            proporciones = (conteo/len(df_filtered))*100

            st.dataframe(proporciones)

    # -----------------------------------------------------
    # ITEM 7
    # -----------------------------------------------------

    with tab7:

        st.header("Ítem 7: Análisis bivariado (Numérico vs Categórico)")

        col1,col2 = st.columns(2)

        with col1:

            fig,ax = plt.subplots()

            sns.boxplot(x="y", y="age", data=df_filtered, ax=ax)

            ax.set_title("Age vs y")

            st.pyplot(fig)

        with col2:

            fig,ax = plt.subplots()

            sns.boxplot(x="y", y="duration", data=df_filtered, ax=ax)

            ax.set_title("Duration vs y")

            st.pyplot(fig)

        st.info("Comparación de grupos: permite observar diferencias entre clientes que aceptaron o no el depósito.")

    # -----------------------------------------------------
    # ITEM 8
    # -----------------------------------------------------

    with tab8:

        st.header("Ítem 8: Análisis bivariado (Categórico vs Categórico)")

        col1,col2 = st.columns(2)

        with col1:

            tabla = pd.crosstab(df_filtered["education"], df_filtered["y"])

            st.write("Education vs y")

            st.dataframe(tabla)

            fig,ax = plt.subplots()

            tabla.plot(kind="bar", ax=ax)

            st.pyplot(fig)

        with col2:

            tabla = pd.crosstab(df_filtered["contact"], df_filtered["y"])

            st.write("Contact vs y")

            st.dataframe(tabla)

            fig,ax = plt.subplots()

            tabla.plot(kind="bar", ax=ax)

            st.pyplot(fig)

    # -----------------------------------------------------
    # ITEM 9
    # -----------------------------------------------------

    with tab9:

        st.header("Ítem 9: Análisis dinámico basado en parámetros")

        variable_num = st.selectbox("Variable numérica", numeric_cols)

        variable_cat = st.multiselect("Variable categórica", categorical_cols)

        if variable_cat:

            fig,ax = plt.subplots()

            sns.boxplot(
                x=variable_cat[0],
                y=variable_num,
                data=df_filtered,
                ax=ax
            )

            plt.xticks(rotation=45)

            st.pyplot(fig)

    # -----------------------------------------------------
    # ITEM 10
    # -----------------------------------------------------

    with tab10:

        st.header("Ítem 10: Hallazgos clave del EDA")

        col1,col2 = st.columns(2)

        with col1:

            fig,ax = plt.subplots()

            sns.histplot(df_filtered["age"], kde=True, ax=ax)

            st.pyplot(fig)

        with col2:

            fig,ax = plt.subplots()

            sns.countplot(x="y", data=df_filtered, ax=ax)

            st.pyplot(fig)

        st.subheader("Insights principales")

        st.info("""
        - La mayoría de los clientes no acepta el depósito ofrecido por el banco.
        - La duración de la llamada presenta relación con la aceptación del producto.
        - La distribución de edades se concentra en personas económicamente activas.
        - Algunas variables categóricas como educación o tipo de contacto muestran diferencias en el comportamiento de los clientes.
        - Estos patrones pueden ayudar a mejorar futuras campañas de marketing mediante una mejor segmentación de clientes.
        """)

elif menu == "Conclusiones":

    st.title("📌 Conclusiones del análisis")

    # -----------------------------------------------------
    # VALIDACIÓN OBLIGATORIA
    # -----------------------------------------------------

    if "dataset" not in st.session_state:
        st.warning("⚠️ Primero debe cargar el dataset en el módulo 'Carga del Dataset'")
        st.stop()

    df = st.session_state["dataset"]

    st.write("""
    1. La mayoría de los clientes no acepta la oferta de depósito, lo que indica que las campañas podrían mejorar su segmentación.

    2. La duración de la llamada parece tener relación con la aceptación del producto, ya que las llamadas más largas suelen terminar en respuestas positivas.

    3. Algunas variables categóricas como el nivel educativo y el tipo de contacto muestran diferencias en el comportamiento de los clientes.

    4. La distribución de edades muestra que la mayoría de los clientes pertenece a grupos económicamente activos.

    5. Los patrones identificados en el análisis pueden ayudar al banco a diseñar campañas de marketing más enfocadas en los segmentos con mayor probabilidad de aceptación.
    """)