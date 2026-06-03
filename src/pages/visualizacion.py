"""
Módulo de Visualización de Datos
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.utils import plot_kde, plot_bar_chart, get_churn_analysis
from src.config import COLORS, PLOT_CONFIG


def show_visualizacion():
    """Muestra la sección de visualización de datos"""
    
    st.markdown("## 📊 Análisis Visual")
    st.write("Visualización de relaciones e insights en los datos")
    st.divider()
    
    df = st.session_state.get("df")
    
    if df is None:
        st.warning("⚠️ Por favor, cargue un dataset primero")
        return
    
    # Opciones de visualización
    opciones = [
        "Clientes Activos vs Abandonados",
        "Permanencia Laboral vs Churn",
        "Número de Productos vs Churn",
        "Género vs Churn",
        "Edad Promedio por Estado",
        "Tarjeta de Crédito vs Churn",
        "Distribución de Edades",
        "Distribución de Balance",
    ]
    
    visualizacion = st.selectbox("Seleccione un análisis visual:", opciones)
    
    st.divider()
    
    # ==========================================
    # 3.1. CLIENTES ACTIVOS VS ABANDONADOS
    # ==========================================
    if visualizacion == "Clientes Activos vs Abandonados":
        st.subheader("👥 Relación: Clientes Activos vs Abandonados")
        
        resultado = get_churn_analysis(df, "IsActiveMember")
        
        st.dataframe(resultado, use_container_width=True)
        
        # Gráfico
        fig, ax = plt.subplots(figsize=PLOT_CONFIG["figsize"])
        resultado_plot = (
            df.groupby("IsActiveMember")["Exited"]
            .mean()
            .mul(100)
            .round(2)
        )
        resultado_plot.index = ["Inactivo", "Activo"]
        resultado_plot.plot(kind="bar", ax=ax, color=COLORS['secondary'])
        ax.set_title("Tasa de Abandono por Estado de Actividad", fontsize=14, fontweight='bold', color=COLORS['primary'])
        ax.set_ylabel("Tasa de Abandono (%)")
        ax.set_xlabel("Estado")
        ax.grid(True, alpha=0.3, axis='y')
        st.pyplot(fig)
    
    # ==========================================
    # 3.2. PERMANENCIA LABORAL VS CHURN
    # ==========================================
    elif visualizacion == "Permanencia Laboral vs Churn":
        st.subheader("📅 Relación: Permanencia Laboral vs Churn")
        
        resultado = get_churn_analysis(df, "Tenure")
        st.dataframe(resultado, use_container_width=True)
        
        # Gráfico
        fig, ax = plt.subplots(figsize=PLOT_CONFIG["figsize"])
        resultado_plot = (
            df.groupby("Tenure")["Exited"]
            .mean()
            .mul(100)
            .round(2)
        )
        ax.plot(resultado_plot.index, resultado_plot.values, marker='o', color=COLORS['secondary'], linewidth=2, markersize=6)
        ax.fill_between(resultado_plot.index, resultado_plot.values, alpha=0.3, color=COLORS['secondary'])
        ax.set_title("Tasa de Abandono por Años de Permanencia", fontsize=14, fontweight='bold', color=COLORS['primary'])
        ax.set_ylabel("Tasa de Abandono (%)")
        ax.set_xlabel("Años de Permanencia")
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
    
    # ==========================================
    # 3.3. NÚMERO DE PRODUCTOS VS CHURN
    # ==========================================
    elif visualizacion == "Número de Productos vs Churn":
        st.subheader("🛍️ Relación: Número de Productos vs Churn")
        
        resultado = get_churn_analysis(df, "NumOfProducts")
        st.dataframe(resultado, use_container_width=True)
        
        # Gráfico
        fig, ax = plt.subplots(figsize=PLOT_CONFIG["figsize"])
        resultado_plot = (
            df.groupby("NumOfProducts")["Exited"]
            .mean()
            .mul(100)
            .round(2)
        )
        resultado_plot.plot(kind="bar", ax=ax, color=COLORS['secondary'])
        ax.set_title("Tasa de Abandono por Número de Productos", fontsize=14, fontweight='bold', color=COLORS['primary'])
        ax.set_ylabel("Tasa de Abandono (%)")
        ax.set_xlabel("Número de Productos")
        ax.grid(True, alpha=0.3, axis='y')
        st.pyplot(fig)
    
    # ==========================================
    # 3.4. GÉNERO VS CHURN
    # ==========================================
    elif visualizacion == "Género vs Churn":
        st.subheader("👫 Relación: Género vs Churn")
        
        resultado = get_churn_analysis(df, "Gender")
        st.dataframe(resultado, use_container_width=True)
        
        # Gráfico
        fig, ax = plt.subplots(figsize=PLOT_CONFIG["figsize"])
        resultado_plot = (
            df.groupby("Gender")["Exited"]
            .mean()
            .mul(100)
            .round(2)
        )
        resultado_plot.plot(kind="bar", ax=ax, color=COLORS['secondary'])
        ax.set_title("Tasa de Abandono por Género", fontsize=14, fontweight='bold', color=COLORS['primary'])
        ax.set_ylabel("Tasa de Abandono (%)")
        ax.set_xlabel("Género")
        ax.grid(True, alpha=0.3, axis='y')
        st.pyplot(fig)
    
    # ==========================================
    # 3.5. EDAD PROMEDIO POR ESTADO
    # ==========================================
    elif visualizacion == "Edad Promedio por Estado":
        st.subheader("🎂 Edad Promedio según Estado de Abandono")
        
        resultado = (
            df.groupby("Exited")["Age"]
            .agg(['mean', 'min', 'max', 'std'])
            .round(2)
        )
        resultado.index = ["No Abandonó", "Abandonó"]
        
        st.dataframe(resultado, use_container_width=True)
        
        # Métricas
        col1, col2 = st.columns(2)
        edad_no_exit = df[df["Exited"] == 0]["Age"].mean()
        edad_exit = df[df["Exited"] == 1]["Age"].mean()
        
        with col1:
            st.metric("Edad Promedio (No Abandonó)", f"{edad_no_exit:.2f} años")
        with col2:
            st.metric("Edad Promedio (Abandonó)", f"{edad_exit:.2f} años")
    
    # ==========================================
    # 3.6. TARJETA DE CRÉDITO VS CHURN
    # ==========================================
    elif visualizacion == "Tarjeta de Crédito vs Churn":
        st.subheader("💳 Tasa de Abandono según Tenencia de Tarjeta de Crédito")
        
        resultado = (
            pd.crosstab(
                df["HasCrCard"],
                df["Exited"],
                normalize="index"
            ) * 100
        ).round(2)
        
        resultado.index = ["Sin Tarjeta", "Con Tarjeta"]
        resultado.columns = ["No Abandonó (%)", "Abandonó (%)"]
        
        st.dataframe(resultado, use_container_width=True)
        
        # Gráfico
        fig, ax = plt.subplots(figsize=PLOT_CONFIG["figsize"])
        resultado.plot(kind="bar", ax=ax, color=[COLORS['success'], COLORS['danger']])
        ax.set_title("Tasa de Abandono según Tarjeta de Crédito", fontsize=14, fontweight='bold', color=COLORS['primary'])
        ax.set_ylabel("Porcentaje (%)")
        ax.set_xlabel("Estado de Tarjeta")
        ax.grid(True, alpha=0.3, axis='y')
        plt.xticks(rotation=0)
        st.pyplot(fig)
    
    # ==========================================
    # 3.7. DISTRIBUCIÓN DE EDADES
    # ==========================================
    elif visualizacion == "Distribución de Edades":
        st.subheader("📊 Distribución de Edades según Estado de Abandono")
        
        fig = plot_kde(
            df,
            x_col="Age",
            hue_col="Exited",
            title="Distribución de Edades por Estado de Abandono"
        )
        st.pyplot(fig)
        
        # Estadísticas
        col1, col2 = st.columns(2)
        with col1:
            st.write("**No Abandonó (0):**")
            st.write(f"- Media: {df[df['Exited']==0]['Age'].mean():.2f}")
            st.write(f"- Mediana: {df[df['Exited']==0]['Age'].median():.2f}")
            st.write(f"- Rango: {df[df['Exited']==0]['Age'].min()}-{df[df['Exited']==0]['Age'].max()}")
        
        with col2:
            st.write("**Abandonó (1):**")
            st.write(f"- Media: {df[df['Exited']==1]['Age'].mean():.2f}")
            st.write(f"- Mediana: {df[df['Exited']==1]['Age'].median():.2f}")
            st.write(f"- Rango: {df[df['Exited']==1]['Age'].min()}-{df[df['Exited']==1]['Age'].max()}")
    
    # ==========================================
    # 3.8. DISTRIBUCIÓN DE BALANCE
    # ==========================================
    elif visualizacion == "Distribución de Balance":
        st.subheader("💰 Distribución de Balance según Estado de Abandono")
        
        fig = plot_kde(
            df,
            x_col="Balance",
            hue_col="Exited",
            title="Distribución de Balance por Estado de Abandono"
        )
        st.pyplot(fig)
        
        # Estadísticas
        col1, col2 = st.columns(2)
        with col1:
            st.write("**No Abandonó (0):**")
            st.write(f"- Media: ${df[df['Exited']==0]['Balance'].mean():.2f}")
            st.write(f"- Mediana: ${df[df['Exited']==0]['Balance'].median():.2f}")
            st.write(f"- Máximo: ${df[df['Exited']==0]['Balance'].max():.2f}")
        
        with col2:
            st.write("**Abandonó (1):**")
            st.write(f"- Media: ${df[df['Exited']==1]['Balance'].mean():.2f}")
            st.write(f"- Mediana: ${df[df['Exited']==1]['Balance'].median():.2f}")
            st.write(f"- Máximo: ${df[df['Exited']==1]['Balance'].max():.2f}")
