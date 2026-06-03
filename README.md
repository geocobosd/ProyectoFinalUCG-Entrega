# 🏦 Análisis de Abandono Bancario (Churn Analysis)

[![Streamlit App](https://img.shields.io/badge/Streamlit-v1.0-FF4B4B?style=for-the-badge&logo=Streamlit)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=Python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

Sistema inteligente de análisis y predicción de abandono de clientes en instituciones bancarias, desarrollado con Streamlit y Python.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Tecnologías](#tecnologías)
- [Dataset](#dataset)
- [Análisis Disponibles](#análisis-disponibles)
- [Mejoras Futuras](#mejoras-futuras)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Autor](#autor)

---

## ✨ Características

✅ **Exploración Interactiva de Datos**
- Análisis de dimensiones y estructura del dataset
- Detección automática de valores nulos
- Identificación de datos duplicados
- Detección de valores atípicos (outliers) con métodos IQR y Z-Score
- Análisis de balance de variables objetivo

✅ **Visualizaciones Profesionales**
- Gráficos interactivos con matplotlib y seaborn
- Análisis de relaciones entre variables
- Distribuciones de edades y balance
- Tasas de abandono por diferentes segmentos

✅ **Interfaz Moderna**
- Tema profesional con colores corporativos (Azul + Naranja)
- Responsive design
- Navegación intuitiva
- Componentes visuales mejorados

✅ **Gestión de Datos**
- Carga de archivos CSV personalizados
- Dataset predeterminado incluido
- Caché de datos para mejor rendimiento
- Session state para persistencia de datos

---

## 📋 Requisitos

- **Python 3.8+**
- **pip** o **conda** (gestor de paquetes)
- **Git** (opcional, para clonación)

---

## 🚀 Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/ProyectoFinalUCG.git
cd ProyectoFinalUCG
```

### 2. Crear un Entorno Virtual (Recomendado)

**Con venv (Python):**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

**Con conda:**
```bash
conda create -n churn-analysis python=3.9
conda activate churn-analysis
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

**Contenido de requirements.txt:**
```
pandas>=1.3.0
numpy>=1.21.0
streamlit>=1.20.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=0.24.0
xgboost>=1.5.0
```

### 4. Ejecutar la Aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá en `http://localhost:8501`

---

## 💡 Uso

### Página de Inicio
- **Descripción** general de la aplicación
- Instrucciones de uso
- Información sobre características
- Columnas típicas del dataset

### Sección de Exploración 🔍
Analiza la estructura de tus datos:

1. **Resumen General**: Estadísticas básicas del dataset
2. **Dimensiones**: Número de filas y columnas
3. **Tipos de Datos**: Información sobre tipos de variables
4. **Valores Nulos**: Detección de datos faltantes
5. **Datos Duplicados**: Identificación de registros repetidos
6. **Valores Atípicos**: Detección de outliers
7. **Balance de Variables**: Distribución de clases objetivo

### Sección de Visualización 📊
Explora relaciones y patrones:

1. **Clientes Activos vs Abandonados**: Tasa de churn por actividad
2. **Permanencia Laboral vs Churn**: Relación con años en banco
3. **Número de Productos vs Churn**: Impacto de cantidad de productos
4. **Género vs Churn**: Análisis por género
5. **Edad Promedio**: Edad según estado de abandono
6. **Tarjeta de Crédito vs Churn**: Lealtad de clientes con tarjeta
7. **Distribución de Edades**: Gráficos de densidad
8. **Distribución de Balance**: Análisis de saldos

### Carga de Datos

**Opción 1: Dataset Predeterminado**
```
Click en "📊 Cargar Dataset Predeterminado" en la barra lateral
```

**Opción 2: Archivo Personalizado**
```
Usa el uploader de CSV en la barra lateral
```

---

## 📁 Estructura del Proyecto

```
ProyectoFinalUCG/
├── app.py                          # Aplicación principal
├── src/
│   ├── __init__.py
│   ├── config.py                  # Configuración centralizada
│   ├── utils.py                   # Funciones auxiliares
│   ├── styles/
│   │   └── custom_style.py        # Estilos HTML/CSS personalizados
│   └── pages/
│       ├── exploracion.py         # Módulo de exploración de datos
│       └── visualizacion.py       # Módulo de visualizaciones
├── data/
│   └── Churn_Modelling.csv        # Dataset incluido
├── .streamlit/
│   └── config.toml                # Configuración de Streamlit
├── requirements.txt               # Dependencias del proyecto
├── README.md                       # Este archivo
├── .gitignore                      # Archivos a ignorar en Git
└── LICENSE                         # Licencia MIT
```

### Descripción de Archivos Principales

| Archivo | Descripción |
|---------|------------|
| `app.py` | Punto de entrada principal de la aplicación |
| `src/config.py` | Configuración centralizada (colores, rutas, mensajes) |
| `src/utils.py` | Funciones reutilizables para carga y análisis de datos |
| `src/styles/custom_style.py` | Estilos personalizados y componentes HTML/CSS |
| `src/pages/exploracion.py` | Lógica de la sección de exploración |
| `src/pages/visualizacion.py` | Lógica de la sección de visualización |

---

## 🛠️ Tecnologías

| Tecnología | Uso |
|-----------|-----|
| **Streamlit** | Framework web para aplicaciones de datos |
| **Pandas** | Manipulación y análisis de datos |
| **NumPy** | Cálculos numéricos |
| **Matplotlib** | Visualización de gráficos |
| **Seaborn** | Gráficos estadísticos avanzados |
| **Scikit-learn** | Machine Learning (opcional para futuros modelos) |
| **XGBoost** | Modelos de predicción (opcional) |
| **Python 3.8+** | Lenguaje de programación |

---

## 📊 Dataset

### Información General

- **Nombre**: Churn_Modelling.csv
- **Filas**: 10,000 registros
- **Columnas**: 12 variables
- **Variable Objetivo**: `Exited` (Abandono: 0/1)

### Columnas del Dataset

| Columna | Descripción | Tipo |
|---------|------------|------|
| `CustomerId` | ID único del cliente | Integer |
| `Surname` | Apellido del cliente | String |
| `CreditScore` | Puntuación crediticia | Integer |
| `Geography` | País del cliente | String |
| `Gender` | Género del cliente | String |
| `Age` | Edad del cliente | Integer |
| `Tenure` | Años como cliente del banco | Integer |
| `Balance` | Saldo de la cuenta | Float |
| `NumOfProducts` | Cantidad de productos contratados | Integer |
| `HasCrCard` | Posee tarjeta de crédito (0/1) | Integer |
| `IsActiveMember` | Es miembro activo (0/1) | Integer |
| `EstimatedSalary` | Salario estimado | Float |
| **`Exited`** | **Abandonó el banco (0/1)** | **Integer** |

### Distribución de Clases

- **No Abandonaron (0)**: ~79.6%
- **Abandonaron (1)**: ~20.4%

---

## 📈 Análisis Disponibles

### 1. Exploración de Datos
- Revisión de estructura y calidad
- Detección de valores faltantes
- Identificación de duplicados
- Análisis de valores atípicos

### 2. Análisis Descriptivo
- Estadísticas por segmentos
- Comparación de tasas de churn
- Distribuciones de variables clave

### 3. Visualizaciones
- Gráficos de barras
- Gráficos de densidad (KDE)
- Box plots
- Análisis de relaciones

### 4. Insights Principales (Potenciales)
- Clientes de mayor edad tienen mayor probabilidad de abandonar
- La permanencia en el banco está correlacionada con lealtad
- El número de productos influye en la retención
- Diferencias de churn entre géneros

---

## 🚀 Despliegue en Streamlit Cloud

### 1. Preparar el Repositorio

```bash
# Asegurarse de que todo está en Git
git add .
git commit -m "Versión lista para deployment"
git push origin main
```

### 2. Conectar con Streamlit Cloud

1. Ir a [share.streamlit.io](https://share.streamlit.io)
2. Hacer click en "New app"
3. Seleccionar tu repositorio GitHub
4. Elegir branch "main"
5. Configurar path a "app.py"
6. Click en "Deploy"

### 3. Configuración de Secretos (si es necesaria)

```bash
# En .streamlit/secrets.toml (local, no subir a GitHub)
[database]
api_key = "tu-clave-secreta"
```

---

## 🔄 Flujo de Trabajo de Desarrollo

```
1. Cargar datos
   ↓
2. Explorar estructura
   ↓
3. Analizar calidad
   ↓
4. Visualizar relaciones
   ↓
5. Extraer insights
   ↓
6. Tomar decisiones
```

---

## 💾 Mejoras Futuras

- [ ] Agregar sección de modelos predictivos
- [ ] Implementar Random Forest
- [ ] Implementar XGBoost
- [ ] Dashboard con métricas de rendimiento
- [ ] Exportación de reportes a PDF
- [ ] Análisis de correlaciones
- [ ] Heatmaps interactivos
- [ ] Predicciones en tiempo real
- [ ] API REST
- [ ] Autenticación de usuarios
- [ ] Base de datos para histórico
- [ ] Temas dark/light intercambiables

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. **Fork** el repositorio
2. Crear una rama (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Ver archivo [LICENSE](LICENSE) para más detalles.

---

## 👨‍💼 Autor

**Universidad CASA GRANDE**

- 📧 Email: info@casagrange.edu
- 🌐 Web: www.casagrange.edu
- 📚 Programa: Maestría en Inteligencia Artificial y Ciencia de Datos

---

## 🙏 Agradecimientos

- Dataset original de [Kaggle](https://www.kaggle.com/datasets/churndata)
- Comunidad de Streamlit
- Contribuidores y usuarios

---

## 📞 Soporte

¿Tienes preguntas o encuentras un bug? 

- Abre un **Issue** en GitHub
- Consulta la documentación de [Streamlit](https://docs.streamlit.io)
- Revisa ejemplos en [Streamlit Gallery](https://streamlit.io/gallery)

---

## 📊 Estadísticas del Proyecto

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red)
![License](https://img.shields.io/badge/License-MIT-green)

**Última actualización**: Junio 2024

---

**Hecho con ❤️ para análisis de datos bancarios**
