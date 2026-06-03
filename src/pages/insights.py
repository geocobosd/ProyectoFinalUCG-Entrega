"""
Módulo de Análisis e Insights con Modelos Predictivos
Contiene Random Forest y XGBoost para predicción de churn
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)
from xgboost import XGBClassifier
from src.config import COLORS, PLOT_CONFIG
import seaborn as sns


def prepare_data(df: pd.DataFrame) -> tuple:
    """
    Prepara los datos para modelado
    
    Args:
        df: DataFrame con los datos
        
    Returns:
        Tupla (X_train, X_test, y_train, y_test)
    """
    try:
        # Copiar datos
        data_model = df.copy()
        
        # Eliminar columnas innecesarias
        if 'Surname' in data_model.columns:
            data_model = data_model.drop('Surname', axis=1)
        if 'CustomerId' in data_model.columns:
            data_model = data_model.drop('CustomerId', axis=1)
        
        # Convertir variables categóricas
        data_model = pd.get_dummies(
            data_model,
            columns=['Geography', 'Gender'],
            drop_first=True
        )
        
        # Separar variable objetivo
        X = data_model.drop('Exited', axis=1)
        y = data_model['Exited']
        
        # Llenar valores nulos
        X = X.fillna(0)
        
        # Dividir datos
        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.3,
            random_state=42,
            stratify=y
        )
        
        return X_train, X_test, y_train, y_test, X.columns
        
    except Exception as e:
        st.error(f"Error al preparar datos: {str(e)}")
        return None, None, None, None, None


def plot_confusion_matrix(cm, title="Matriz de Confusión"):
    """Visualiza la matriz de confusión"""
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                cbar_kws={'label': 'Cantidad'},
                xticklabels=['No Abandonó', 'Abandonó'],
                yticklabels=['No Abandonó', 'Abandonó'])
    ax.set_title(title, fontsize=14, fontweight='bold', color=COLORS['primary'])
    ax.set_ylabel('Real')
    ax.set_xlabel('Predicción')
    return fig


def plot_feature_importance(importances, feature_names, title="Importancia de Variables", top_n=10):
    """Visualiza la importancia de características"""
    feat_importance = pd.Series(importances, index=feature_names).nlargest(top_n)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    feat_importance.plot(kind='barh', ax=ax, color=COLORS['secondary'])
    ax.set_title(title, fontsize=14, fontweight='bold', color=COLORS['primary'])
    ax.set_xlabel('Importancia')
    ax.invert_yaxis()
    ax.grid(True, alpha=0.3, axis='x')
    return fig


def show_model_metrics(y_test, y_pred, model_name="Modelo"):
    """Muestra métricas de evaluación del modelo"""
    
    col1, col2, col3, col4 = st.columns(4)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    with col1:
        st.metric("Precisión (Accuracy)", f"{accuracy:.4f}")
    with col2:
        st.metric("Precisión (Precision)", f"{precision:.4f}")
    with col3:
        st.metric("Sensibilidad (Recall)", f"{recall:.4f}")
    with col4:
        st.metric("F1-Score", f"{f1:.4f}")
    
    return accuracy, precision, recall, f1


def show_random_forest(X_train, X_test, y_train, y_test, feature_names):
    """Ejecuta y visualiza Random Forest"""
    
    st.subheader("🌲 Modelo Random Forest")
    st.write("Modelo de ensamble basado en árboles de decisión para clasificación de churn")
    
    st.divider()
    
    # Parámetros del modelo
    with st.expander("⚙️ Parámetros del Modelo", expanded=False):
        n_estimators = st.slider("Número de árboles", 50, 500, 100, 50)
        max_depth = st.slider("Profundidad máxima", 5, 50, 20)
        min_samples_split = st.slider("Mínimo de muestras para dividir", 2, 20, 5)
    
    # Entrenar modelo
    with st.spinner("⏳ Entrenando modelo Random Forest..."):
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            random_state=42,
            n_jobs=-1
        )
        
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
    
    st.success("✅ Modelo entrenado exitosamente")
    
    st.divider()
    
    # Métricas
    st.markdown("#### 📊 Métricas de Evaluación")
    accuracy, precision, recall, f1 = show_model_metrics(y_test, y_pred, "Random Forest")
    
    st.divider()
    
    # Matriz de confusión
    st.markdown("#### 🔲 Matriz de Confusión")
    cm = confusion_matrix(y_test, y_pred)
    fig = plot_confusion_matrix(cm, "Matriz de Confusión - Random Forest")
    st.pyplot(fig)
    
    st.divider()
    
    # Reporte de clasificación
    st.markdown("#### 📋 Reporte de Clasificación")
    report_text = classification_report(
        y_test, y_pred,
        target_names=['No Abandonó', 'Abandonó']
    )
    st.code(report_text, language="text")
    
    st.divider()
    
    # Importancia de características
    st.markdown("#### 🎯 Importancia de Características")
    fig = plot_feature_importance(
        model.feature_importances_,
        feature_names,
        "Top 10 Variables más Importantes - Random Forest",
        top_n=10
    )
    st.pyplot(fig)
    
    st.divider()
    
    # Predicciones detalladas
    st.markdown("#### 🔍 Predicciones Detalladas")
    
    resultado = pd.DataFrame({
        'Real': y_test.values,
        'Predicción': y_pred,
        'Probabilidad_No_Abandono': model.predict_proba(X_test)[:, 0],
        'Probabilidad_Abandono': model.predict_proba(X_test)[:, 1]
    }).round(4)
    
    st.dataframe(resultado.head(20), use_container_width=True)
    
    # Interpretación
    st.markdown("#### 💡 Interpretación de Resultados")
    
    if accuracy > 0.85:
        st.success(f"✅ Excelente desempeño con accuracy de {accuracy:.2%}")
    elif accuracy > 0.75:
        st.info(f"ℹ️ Buen desempeño con accuracy de {accuracy:.2%}")
    else:
        st.warning(f"⚠️ Desempeño moderado con accuracy de {accuracy:.2%}")
    
    st.info(f"""
    **Variables más influyentes en la predicción:**
    - {feature_names[np.argsort(model.feature_importances_)[-1]]}: {np.max(model.feature_importances_):.4f}
    - {feature_names[np.argsort(model.feature_importances_)[-2]]}: {np.sort(model.feature_importances_)[-2]:.4f}
    - {feature_names[np.argsort(model.feature_importances_)[-3]]}: {np.sort(model.feature_importances_)[-3]:.4f}
    """)


def show_xgboost(X_train, X_test, y_train, y_test, feature_names):
    """Ejecuta y visualiza XGBoost"""
    
    st.subheader("⚡ Modelo XGBoost")
    st.write("Gradient Boosting extremo para predicción de churn con alto rendimiento")
    
    st.divider()
    
    # Parámetros del modelo
    with st.expander("⚙️ Parámetros del Modelo", expanded=False):
        n_estimators = st.slider("Número de iteraciones", 50, 500, 200, 50)
        max_depth = st.slider("Profundidad máxima", 3, 10, 6)
        learning_rate = st.slider("Tasa de aprendizaje", 0.01, 0.5, 0.1, 0.01)
        scale_pos_weight = st.slider("Peso para clase positiva", 1.0, 10.0, 4.0, 0.5)
    
    # Entrenar modelo
    with st.spinner("⏳ Entrenando modelo XGBoost..."):
        model = XGBClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            learning_rate=learning_rate,
            scale_pos_weight=scale_pos_weight,
            random_state=42,
            use_label_encoder=False,
            eval_metric='logloss',
            verbosity=0
        )
        
        model.fit(X_train, y_train, verbose=False)
        y_pred = model.predict(X_test)
    
    st.success("✅ Modelo entrenado exitosamente")
    
    st.divider()
    
    # Métricas
    st.markdown("#### 📊 Métricas de Evaluación")
    accuracy, precision, recall, f1 = show_model_metrics(y_test, y_pred, "XGBoost")
    
    st.divider()
    
    # Matriz de confusión
    st.markdown("#### 🔲 Matriz de Confusión")
    cm = confusion_matrix(y_test, y_pred)
    fig = plot_confusion_matrix(cm, "Matriz de Confusión - XGBoost")
    st.pyplot(fig)
    
    st.divider()
    
    # Reporte de clasificación
    st.markdown("#### 📋 Reporte de Clasificación")
    report_text = classification_report(
        y_test, y_pred,
        target_names=['No Abandonó', 'Abandonó']
    )
    st.code(report_text, language="text")
    
    st.divider()
    
    # Importancia de características
    st.markdown("#### 🎯 Importancia de Características")
    fig = plot_feature_importance(
        model.feature_importances_,
        feature_names,
        "Top 10 Variables más Importantes - XGBoost",
        top_n=10
    )
    st.pyplot(fig)
    
    st.divider()
    
    # Predicciones detalladas
    st.markdown("#### 🔍 Predicciones Detalladas")
    
    resultado = pd.DataFrame({
        'Real': y_test.values,
        'Predicción': y_pred,
        'Probabilidad_No_Abandono': model.predict_proba(X_test)[:, 0],
        'Probabilidad_Abandono': model.predict_proba(X_test)[:, 1]
    }).round(4)
    
    st.dataframe(resultado.head(20), use_container_width=True)
    
    # Interpretación
    st.markdown("#### 💡 Interpretación de Resultados")
    
    if accuracy > 0.85:
        st.success(f"✅ Excelente desempeño con accuracy de {accuracy:.2%}")
    elif accuracy > 0.75:
        st.info(f"ℹ️ Buen desempeño con accuracy de {accuracy:.2%}")
    else:
        st.warning(f"⚠️ Desempeño moderado con accuracy de {accuracy:.2%}")
    
    st.info(f"""
    **Variables más influyentes en la predicción:**
    - {feature_names[np.argsort(model.feature_importances_)[-1]]}: {np.max(model.feature_importances_):.4f}
    - {feature_names[np.argsort(model.feature_importances_)[-2]]}: {np.sort(model.feature_importances_)[-2]:.4f}
    - {feature_names[np.argsort(model.feature_importances_)[-3]]}: {np.sort(model.feature_importances_)[-3]:.4f}
    """)


def show_insights():
    """Función principal para mostrar la sección de Insights"""
    
    st.markdown("## 📈 Análisis Predictivo con Machine Learning")
    st.write("Modelos de aprendizaje automático para predicción de churn bancario")
    st.divider()
    
    df = st.session_state.get("df")
    
    if df is None:
        st.warning("⚠️ Por favor, cargue un dataset primero")
        return
    
    # Preparar datos
    X_train, X_test, y_train, y_test, feature_names = prepare_data(df)
    
    if X_train is None:
        st.error("No se pudieron preparar los datos")
        return
    
    st.success(f"✅ Datos preparados: {len(X_train)} registros para entrenar, {len(X_test)} para prueba")
    
    st.divider()
    
    # Seleccionar modelo
    modelo = st.selectbox(
        "Selecciona un modelo predictivo:",
        ["Selecciona un modelo", "🌲 Random Forest", "⚡ XGBoost"]
    )
    
    st.divider()
    
    if modelo == "Selecciona un modelo":
        st.info("""
        **Elige un modelo para entrenar y evaluar:**
        
        - **Random Forest**: Ensamble de árboles de decisión, interpretable y robusto
        - **XGBoost**: Gradient Boosting extremo, mayor precisión pero menos interpretable
        """)
    
    elif modelo == "🌲 Random Forest":
        show_random_forest(X_train, X_test, y_train, y_test, feature_names)
    
    elif modelo == "⚡ XGBoost":
        show_xgboost(X_train, X_test, y_train, y_test, feature_names)
