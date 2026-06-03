"""
Funciones auxiliares reutilizables
"""

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from src.config import PLOT_CONFIG, COLORS, DATA_PATH


@st.cache_data
def load_data(filepath: str = DATA_PATH) -> pd.DataFrame:
    """
    Carga el dataset desde archivo CSV
    
    Args:
        filepath: Ruta del archivo CSV
        
    Returns:
        DataFrame con los datos cargados
    """
    try:
        df = pd.read_csv(filepath, index_col=0)
        return df
    except FileNotFoundError:
        st.error(f"No se encontró el archivo: {filepath}")
        return None
    except Exception as e:
        st.error(f"Error al cargar los datos: {str(e)}")
        return None


def get_basic_stats(df: pd.DataFrame) -> dict:
    """
    Retorna estadísticas básicas del dataset
    
    Args:
        df: DataFrame
        
    Returns:
        Diccionario con estadísticas básicas
    """
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "null_values": df.isnull().sum().sum(),
        "duplicate_rows": df.duplicated().sum(),
    }


def display_metric_row(metrics: dict):
    """
    Muestra una fila de métricas
    
    Args:
        metrics: Diccionario con {nombre: valor}
    """
    cols = st.columns(len(metrics))
    for col, (name, value) in zip(cols, metrics.items()):
        with col:
            st.metric(name, value)


def get_data_types_info(df: pd.DataFrame) -> pd.DataFrame:
    """
    Retorna información sobre tipos de datos
    
    Args:
        df: DataFrame
        
    Returns:
        DataFrame con información de tipos de datos
    """
    return pd.DataFrame({
        "Variable": df.columns,
        "Tipo de Dato": df.dtypes.values,
        "No Nulos": df.notnull().sum().values,
        "Nulos": df.isnull().sum().values,
    })


def get_null_values_info(df: pd.DataFrame) -> pd.DataFrame:
    """
    Retorna información sobre valores nulos
    
    Args:
        df: DataFrame
        
    Returns:
        DataFrame con conteo de valores nulos
    """
    nulos = df.isnull().sum()
    return pd.DataFrame({
        "Variable": nulos.index,
        "Valores Nulos": nulos.values,
        "Porcentaje (%)": (nulos / len(df) * 100).round(2).values,
    })


def detect_outliers(df: pd.DataFrame, column: str, method: str = "iqr") -> tuple:
    """
    Detecta valores atípicos en una columna
    
    Args:
        df: DataFrame
        column: Nombre de la columna
        method: Método de detección ('iqr' o 'zscore')
        
    Returns:
        Tupla (DataFrame con outliers, límite inferior, límite superior)
    """
    if method == "iqr":
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
    else:  # zscore
        mean = df[column].mean()
        std = df[column].std()
        lower_bound = mean - 3 * std
        upper_bound = mean + 3 * std
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    
    return outliers, lower_bound, upper_bound


def plot_boxplot(df: pd.DataFrame, column: str, title: str = None, figsize: tuple = None):
    """
    Crea un boxplot
    
    Args:
        df: DataFrame
        column: Nombre de la columna
        title: Título del gráfico
        figsize: Tamaño de la figura
    """
    if figsize is None:
        figsize = PLOT_CONFIG["figsize"]
    
    if title is None:
        title = f"Boxplot de {column}"
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.boxplot(df[column])
    ax.set_title(title, fontsize=14, fontweight='bold', color=COLORS['primary'])
    ax.set_ylabel(column)
    ax.grid(True, alpha=0.3)
    
    return fig


def plot_bar_chart(data, title: str = None, xlabel: str = None, ylabel: str = None, 
                   figsize: tuple = None, color: str = None):
    """
    Crea un gráfico de barras
    
    Args:
        data: Serie de pandas o diccionario
        title: Título del gráfico
        xlabel: Etiqueta eje X
        ylabel: Etiqueta eje Y
        figsize: Tamaño de la figura
        color: Color de las barras
    """
    if figsize is None:
        figsize = PLOT_CONFIG["figsize"]
    
    if color is None:
        color = COLORS['secondary']
    
    fig, ax = plt.subplots(figsize=figsize)
    
    if isinstance(data, dict):
        data = pd.Series(data)
    
    data.plot(kind="bar", ax=ax, color=color)
    
    if title:
        ax.set_title(title, fontsize=14, fontweight='bold', color=COLORS['primary'])
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    
    ax.grid(True, alpha=0.3, axis='y')
    plt.xticks(rotation=45, ha='right')
    
    return fig


def plot_kde(df: pd.DataFrame, x_col: str, hue_col: str = None, title: str = None, figsize: tuple = None):
    """
    Crea un gráfico KDE (Kernel Density Estimation)
    
    Args:
        df: DataFrame
        x_col: Columna para eje X
        hue_col: Columna para colorear (opcional)
        title: Título del gráfico
        figsize: Tamaño de la figura
    """
    if figsize is None:
        figsize = PLOT_CONFIG["figsize"]
    
    if title is None:
        title = f"Distribución de {x_col}"
    
    fig, ax = plt.subplots(figsize=figsize)
    sns.kdeplot(data=df, x=x_col, hue=hue_col, fill=True, ax=ax)
    ax.set_title(title, fontsize=14, fontweight='bold', color=COLORS['primary'])
    ax.grid(True, alpha=0.3)
    
    return fig


def get_churn_analysis(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """
    Analiza la tasa de abandono por una columna de agrupación
    
    Args:
        df: DataFrame
        group_col: Columna para agrupar
        
    Returns:
        DataFrame con análisis de churn
    """
    resultado = (
        df.groupby(group_col)["Exited"]
        .agg(['count', 'sum', 'mean'])
        .rename(columns={'count': 'Total', 'sum': 'Abandonaron', 'mean': 'Tasa (%)'})
    )
    
    resultado['Tasa (%)'] = (resultado['Tasa (%)'] * 100).round(2)
    
    return resultado.reset_index()


def format_percentage(value: float) -> str:
    """
    Formatea un valor como porcentaje
    
    Args:
        value: Valor decimal
        
    Returns:
        String formateado como porcentaje
    """
    return f"{value * 100:.2f}%"
