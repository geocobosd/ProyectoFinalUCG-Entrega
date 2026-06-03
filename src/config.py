"""
Configuración centralizada de la aplicación Streamlit
"""

# Colores corporativos
COLORS = {
    "primary": "#1E3A8A",      # Azul oscuro profesional
    "secondary": "#FF8C42",     # Naranja cálido
    "success": "#10B981",       # Verde éxito
    "warning": "#F59E0B",       # Ámbar advertencia
    "danger": "#EF4444",        # Rojo peligro
    "light": "#F3F4F6",         # Gris claro
    "dark": "#1F2937",          # Gris oscuro
    "border": "#E5E7EB",        # Borde gris
}

# Configuración de la aplicación
APP_CONFIG = {
    "title": "Análisis de Abandono Bancario",
    "subtitle": "Sistema Inteligente de Predicción de Churn",
    "description": "Análisis y predicción de abandono de clientes en instituciones bancarias",
    "author": "Universidad CASA GRANDE",
    "version": "1.0.0",
    "page_icon": "🏦",
}

# Rutas de archivos
DATA_PATH = "data/Churn_Modelling.csv"

# Configuración de gráficos
PLOT_CONFIG = {
    "figsize": (12, 6),
    "style": "darkgrid",
    "dpi": 100,
}

# Mensajes
MESSAGES = {
    "success": "✅ Operación completada exitosamente",
    "error": "❌ Ocurrió un error",
    "loading": "⏳ Cargando...",
    "info": "ℹ️ Información",
}
