"""
Módulo de Exploración de Datos
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.utils import (
    get_basic_stats, display_metric_row, get_data_types_info,
    get_null_values_info, detect_outliers, plot_boxplot, plot_bar_chart
)
from src.config import COLORS


def show_exploracion():
    """Muestra la sección de exploración de datos"""
    
    st.markdown("## 🔍 Exploración de Datos")
    st.write("Análisis inicial y validación del dataset")
    st.divider()
    
    df = st.session_state.get("df")
    
    if df is None:
        st.warning("⚠️ Por favor, cargue un dataset primero")
        return
    
    # Opciones de exploración
    exploracion = st.radio(
        "Seleccione un tipo de análisis:",
        [
            "Resumen General",
            "Dimensiones del Dataset",
            "Tipos de Datos",
            "Valores Nulos",
            "Datos Duplicados",
            "Valores Atípicos (Outliers)",
            "Balance de Variables",
        ],
        horizontal=True
    )
    
    st.divider()
    
    # ==========================================
    # RESUMEN GENERAL
    # ==========================================
    if exploracion == "Resumen General":
        st.subheader("📊 Resumen General del Dataset")
        
        stats = get_basic_stats(df)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📈 Filas", f"{stats['rows']:,}")
        with col2:
            st.metric("📊 Columnas", stats['columns'])
        with col3:
            st.metric("⚠️ Valores Nulos", stats['null_values'])
        with col4:
            st.metric("🔄 Duplicados", stats['duplicate_rows'])
        
        st.write("**Primeras 5 filas del dataset:**")
        st.dataframe(df.head(), use_container_width=True)
    
    # ==========================================
    # DIMENSIONES
    # ==========================================
    elif exploracion == "Dimensiones del Dataset":
        st.subheader("📐 Dimensiones del Dataset")
        
        filas, columnas = df.shape
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Número de Filas", f"{filas:,}")
        with col2:
            st.metric("Número de Columnas", columnas)
        
        st.write("**Columnas disponibles:**")
        cols_df = pd.DataFrame({
            "Nombre": df.columns,
            "Tipo": df.dtypes.values
        })
        st.dataframe(cols_df, use_container_width=True)
        
        st.write("**Primeras filas:**")
        st.dataframe(df.head(10), use_container_width=True)
    
    # ==========================================
    # TIPOS DE DATOS
    # ==========================================
    elif exploracion == "Tipos de Datos":
        st.subheader("🔤 Tipos de Datos")
        
        tipos_info = get_data_types_info(df)
        st.dataframe(tipos_info, use_container_width=True)
        
        # Resumen
        st.write("**Resumen de Tipos:**")
        type_counts = df.dtypes.value_counts()
        
        col1, col2 = st.columns(2)
        for dtype, count in type_counts.items():
            with col1 if list(type_counts.index).index(dtype) % 2 == 0 else col2:
                st.write(f"• **{dtype}**: {count} columnas")
    
    # ==========================================
    # VALORES NULOS
    # ==========================================
    elif exploracion == "Valores Nulos":
        st.subheader("🕳️ Análisis de Valores Nulos")
        
        nulos_info = get_null_values_info(df)
        
        total_nulos = df.isnull().sum().sum()
        st.metric("Total de Valores Nulos", total_nulos)
        
        if total_nulos > 0:
            st.write("**Detalles por columna:**")
            st.dataframe(nulos_info, use_container_width=True)
            
            # Gráfico
            fig = plot_bar_chart(
                df.isnull().sum()[df.isnull().sum() > 0],
                title="Valores Nulos por Variable",
                ylabel="Cantidad"
            )
            st.pyplot(fig)
        else:
            st.success("✅ No hay valores nulos en el dataset")
    
    # ==========================================
    # DATOS DUPLICADOS
    # ==========================================
    elif exploracion == "Datos Duplicados":
        st.subheader("🔄 Análisis de Datos Duplicados")
        
        duplicados_count = df.duplicated().sum()
        st.metric("Registros Duplicados", duplicados_count)
        
        if duplicados_count > 0:
            st.write("**Primeros registros duplicados:**")
            st.dataframe(df[df.duplicated(keep=False)].head(10), use_container_width=True)
        else:
            st.success("✅ No hay registros duplicados")
    
    # ==========================================
    # OUTLIERS
    # ==========================================
    elif exploracion == "Valores Atípicos (Outliers)":
        st.subheader("📈 Detección de Valores Atípicos")
        
        columnas_numericas = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
        
        if not columnas_numericas:
            st.warning("No hay columnas numéricas para analizar outliers")
            return
        
        variable = st.selectbox("Seleccione una variable numérica:", columnas_numericas)
        metodo = st.radio("Método de detección:", ["IQR", "Z-Score"], horizontal=True)
        
        outliers, lower, upper = detect_outliers(df, variable, "iqr" if metodo == "IQR" else "zscore")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Outliers Detectados", len(outliers))
        with col2:
            st.metric("Límite Inferior", f"{lower:.2f}")
        with col3:
            st.metric("Límite Superior", f"{upper:.2f}")
        with col4:
            st.metric("% del Dataset", f"{(len(outliers)/len(df)*100):.2f}%")
        
        # Boxplot
        fig = plot_boxplot(df, variable, f"Boxplot de {variable}")
        st.pyplot(fig)
        
        if len(outliers) > 0:
            st.write("**Primeros registros con outliers:**")
            st.dataframe(outliers.head(10), use_container_width=True)
    
    # ==========================================
    # BALANCE DE VARIABLES
    # ==========================================
    elif exploracion == "Balance de Variables":
        st.subheader("⚖️ Balance de Variables Objetivo")
        
        if "Exited" in df.columns:
            conteo = df["Exited"].value_counts()
            porcentaje = (df["Exited"].value_counts(normalize=True) * 100).round(2)
            
            resumen = pd.DataFrame({
                "Clase": conteo.index,
                "Cantidad": conteo.values,
                "Porcentaje (%)": porcentaje.values
            })
            
            st.dataframe(resumen, use_container_width=True)
            
            # Gráfico
            fig = plot_bar_chart(
                conteo,
                title="Distribución de la Variable Exited",
                xlabel="Exited",
                ylabel="Cantidad",
                color=COLORS['secondary']
            )
            st.pyplot(fig)
            
            st.info("""
            **Interpretación:**
            - **Exited = 0** → Cliente permanece en el banco (No abandonó)
            - **Exited = 1** → Cliente abandona el banco (Sí abandonó)
            """)
        else:
            st.error("La columna 'Exited' no existe en el dataset")
