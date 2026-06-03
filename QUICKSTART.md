# 🚀 GUÍA RÁPIDA DE INICIO

## ⚡ Comenzar en 5 Minutos

### 1. **Instalar Dependencias**
```bash
pip install -r requirements.txt
```

### 2. **Ejecutar la App**
```bash
streamlit run app.py
```

### 3. **Abrir en el Navegador**
```
http://localhost:8501
```

---

## 🎯 Primeros Pasos

### Opción A: Usar Dataset Incluido ⭐ (Recomendado)
1. Abre la app
2. Haz clic en **"📊 Cargar Dataset Predeterminado"** en la barra lateral
3. ¡Listo! Comienza a explorar

### Opción B: Cargar Tu Propio Dataset
1. Abre la app
2. Usa el **file uploader** de la barra lateral
3. Sube un CSV con tus datos
4. ¡Analiza!

---

## 🗺️ Navegar por la App

| Sección | Qué Hace |
|---------|----------|
| **Inicio** | Bienvenida e instrucciones |
| **🔍 Exploración** | Analiza estructura de datos |
| **📊 Visualización** | Ve gráficos e insights |

---

## 🔍 Qué Puedo Hacer en Exploración

✅ Ver dimensiones del dataset
✅ Encontrar valores nulos
✅ Detectar datos duplicados
✅ Identificar valores atípicos
✅ Analizar balance de clases
✅ Ver tipos de datos

---

## 📊 Qué Puedo Hacer en Visualización

✅ Relación de clientes activos vs abandonados
✅ Permanencia laboral vs churn
✅ Productos vs abandono
✅ Género vs churn
✅ Edad promedio
✅ Tarjeta de crédito vs churn
✅ Distribuciones (edad, balance)

---

## 📋 Requisitos del Dataset

Tu CSV debe tener idealmente:
- `Exited` (variable objetivo: 0/1)
- `Age` (edad)
- `Tenure` (permanencia)
- `Balance` (saldo)
- `IsActiveMember` (activo/inactivo)
- `Gender` (género)
- Y otras columnas de datos...

**⚠️ Nota**: La app es flexible, funcionará con otros CSVs también

---

## 🎨 Características Principales

✨ **Interfaz Moderna**
- Colores profesionales (Azul + Naranja)
- Diseño responsive
- Componentes personalizados

📊 **Análisis Completo**
- 8+ visualizaciones
- Estadísticas detalladas
- Detección automática de problemas

⚡ **Rendimiento**
- Caché de datos
- Carga rápida
- Interfaz fluida

---

## 🤔 Preguntas Frecuentes

### P: ¿Qué versión de Python necesito?
R: Python 3.8 o superior

### P: ¿Puedo usar mis propios datos?
R: Sí, sube un CSV en la barra lateral

### P: ¿Cómo cambio los colores?
R: Edita `src/config.py`

### P: ¿Cómo agrego más análisis?
R: Crea módulos en `src/pages/`

### P: ¿Puedo desplegarlo en Streamlit Cloud?
R: Sí, push a GitHub y conecta en share.streamlit.io

---

## 🔗 Enlaces Útiles

- 📖 [Documentación Streamlit](https://docs.streamlit.io)
- 📊 [Documentación Pandas](https://pandas.pydata.org)
- 📈 [Documentación Matplotlib](https://matplotlib.org)
- 🐍 [Documentación Python](https://docs.python.org/3/)

---

## 💡 Tips y Trucos

1. **Caché**: Los datos se cargan en caché automáticamente
2. **Session**: Usa la barra lateral para navegación suave
3. **Búsqueda**: Prueba diferentes análisis para encontrar insights
4. **Exportación**: Puedes hacer screenshot de los gráficos
5. **Filtros**: Los análisis se adaptan a tus datos

---

## 🚀 Próximos Pasos Avanzados

1. **Modelos Predictivos**: Agrega Random Forest o XGBoost
2. **Dashboard**: Crea un resumen ejecutivo
3. **Exportación**: Genera reportes PDF
4. **Base de Datos**: Integra con SQL/MongoDB
5. **API**: Expone resultados como API REST

---

## 📞 ¿Necesitas Ayuda?

- 📧 Consulta la documentación en README.md
- 🐛 Reporta bugs en GitHub Issues
- 💬 Pregunta en comunidades de Streamlit
- 📚 Revisa ejemplos en Streamlit Gallery

---

**¡Listo para empezar! 🎉**

Abre la terminal y ejecuta:
```bash
streamlit run app.py
```

**¡Que disfrutes analizando datos! 📊✨**
