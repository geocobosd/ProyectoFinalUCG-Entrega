"""
ANÁLISIS DE ABANDONO BANCARIO
Sistema Inteligente de Predicción de Churn

Aplicación Streamlit para análisis y visualización de datos de abandono de clientes
en instituciones bancarias.

Autor: Universidad CASA GRANDE
Versión: 1.0.0
"""

import streamlit as st
import pandas as pd
from src.config import APP_CONFIG, COLORS, DATA_PATH
from src.styles.custom_style import apply_custom_style, get_header_html, get_info_box
from src.utils import load_data
from src.pages.exploracion import show_exploracion
from src.pages.visualizacion import show_visualizacion
from src.pages.insights import show_insights


# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title=APP_CONFIG["title"],
    page_icon=APP_CONFIG["page_icon"],
    layout="wide",
    initial_sidebar_state="expanded",
)

# Aplicar estilos personalizados
apply_custom_style()

# ==========================================
# ESTADO DE LA SESIÓN
# ==========================================
if "df" not in st.session_state:
    st.session_state.df = None
if "page" not in st.session_state:
    st.session_state.page = "Inicio"


# ==========================================
# ENCABEZADO PRINCIPAL
# ==========================================
st.markdown(get_header_html(
    APP_CONFIG["title"],
    APP_CONFIG["page_icon"],
    APP_CONFIG["subtitle"]
), unsafe_allow_html=True)


# ==========================================
# BARRA LATERAL - NAVEGACIÓN Y CARGA
# ==========================================
with st.sidebar:
    st.markdown("### ⚙️ Panel de Control")
    st.divider()
    
    # Sección de carga de datos
    st.markdown("#### 📁 Carga de Datos")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        archivo = st.file_uploader(
            "Sube un archivo CSV",
            type=["csv"],
            help="Carga un archivo CSV con datos de churn bancario"
        )
    
    if archivo:
        with st.spinner("⏳ Cargando archivo..."):
            try:
                df_custom = pd.read_csv(archivo)
                st.session_state.df = df_custom
                st.success("✅ Archivo cargado correctamente")
            except Exception as e:
                st.error(f"❌ Error al cargar: {str(e)}")
    
    # Opción de cargar datos por defecto
    if st.button(
        "📊 Cargar Dataset Predeterminado",
        help="Carga el dataset de ejemplo incluido",
        use_container_width=True
    ):
        with st.spinner("⏳ Cargando datos predeterminados..."):
            df = load_data(DATA_PATH)
            if df is not None:
                st.session_state.df = df
                st.success("✅ Dataset cargado correctamente")
    
    st.divider()
    
    # Navegación
    st.markdown("#### 🗺️ Navegación")
    page = st.radio(
        "Selecciona una sección:",
        ["Inicio", "🔍 Exploración", "📊 Visualización","📈 Insights"],
        label_visibility="collapsed"
    )
    st.session_state.page = page
    
    st.divider()
    
    # Información del dataset
    if st.session_state.df is not None:
        st.markdown("#### 📈 Información del Dataset")
        df = st.session_state.df
        st.metric("Filas", f"{df.shape[0]:,}")
        st.metric("Columnas", df.shape[1])
        
        st.write("**Variables disponibles:**")
        st.write(", ".join(df.columns.tolist()[:5]) + "...")


# ==========================================
# CONTENIDO PRINCIPAL
# ==========================================

if st.session_state.page == "Inicio":
    # ========== PÁGINA DE INICIO ==========
    
    st.markdown("""
    ### 👋 Bienvenido al Sistema de Análisis de Churn Bancario
    
    Esta aplicación te permite analizar y explorar datos de abandono de clientes
    en instituciones bancarias de forma interactiva.
    """)
    
    st.divider()
    
    # Características principales
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(get_info_box(
            "🔍 Exploración",
            "Análisis detallado de la estructura y calidad de los datos",
            "info"
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown(get_info_box(
            "📊 Visualización",
            "Gráficos interactivos y análisis de relaciones entre variables",
            "success"
        ), unsafe_allow_html=True)
    
    with col3:
        st.markdown(get_info_box(
            "📈 Insights",
            "Descubre patrones y tendencias en el comportamiento de churn",
            "warning"
        ), unsafe_allow_html=True)
    
    st.divider()
    
    # Instrucciones
    st.markdown("### 📋 Cómo usar esta aplicación:")
    
    instructions = """
    1. **Cargar datos**: Usa la barra lateral para subir un archivo CSV o carga el dataset predeterminado
    2. **Explorar**: Ve a la sección "Exploración" para analizar la estructura de los datos
    3. **Visualizar**: Consulta la sección "Visualización" para ver gráficos y relaciones
    4. **Analizar**: Interpreta los resultados para obtener insights sobre churn
    
    **Características de la aplicación:**
    - ✅ Carga de datos en tiempo real
    - ✅ Exploración interactiva del dataset
    - ✅ Detección de valores atípicos (outliers)
    - ✅ Análisis de balance de variables
    - ✅ Visualizaciones profesionales
    - ✅ Estadísticas detalladas
    - ✅ Interfaz moderna y responsiva
    """
    
    st.info(instructions)
    
    st.divider()
    
    # Columnas de información
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Próximos Pasos")
        st.markdown("""
        - Carga un dataset desde la barra lateral
        - Explora los datos en la sección correspondiente
        - Visualiza los análisis de churn
        - Exporta insights para tomar decisiones
        """)
    
    with col2:
        st.markdown("### 📊 Columnas Típicas del Dataset")
        st.markdown("""
        - **Exited**: Variable objetivo (0/1)
        - **Age**: Edad del cliente
        - **Tenure**: Años en el banco
        - **Balance**: Saldo de la cuenta
        - **NumOfProducts**: Cantidad de productos
        - **IsActiveMember**: Estado de actividad
        - **HasCrCard**: Tenencia de tarjeta crédito
        - **Gender**: Género
        """)
    
    # Mensaje de bienvenida
    st.divider()
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #666;">
        <p><strong>¿Necesitas ayuda?</strong></p>
        <p>Consulta la documentación o carga el dataset predeterminado para comenzar</p>
    </div>
    """, unsafe_allow_html=True)


elif st.session_state.page == "🔍 Exploración":
    # ========== PÁGINA DE EXPLORACIÓN ==========
    show_exploracion()


elif st.session_state.page == "📊 Visualización":
    # ========== PÁGINA DE VISUALIZACIÓN ==========
    show_visualizacion()


elif st.session_state.page == "📈 Insights":
    # ========== PÁGINA DE INSIGHTS ==========
    show_insights()


# ==========================================
# FOOTER
# ==========================================
st.divider()
st.markdown("""
<div style="text-align: center; padding: 1rem; color: #999; font-size: 0.85rem;">
    <p>
        <strong>Análisis de Abandono Bancario v1.0.0</strong> | 
        Desarrollado por Universidad CASA GRANDE - Ivette Rojas, Geo Cobos, René Lara
    </p>
    <p>
        📧 Email: info@casagrange.edu | 
        🌐 Web: www.casagrange.edu
    </p>
</div>
""", unsafe_allow_html=True)
 
