# 🚀 GUÍA DE DEPLOYMENT

## 📤 Desplegar en GitHub

### Paso 1: Inicializar Repositorio Git (si no existe)

```bash
cd ProyectoFinalUCG
git init
git add .
git commit -m "Versión inicial: Aplicación profesional de análisis de churn"
```

### Paso 2: Crear Repositorio en GitHub

1. Ve a [github.com](https://github.com)
2. Click en "New repository"
3. Nombre: `ProyectoFinalUCG`
4. Descripción: `Sistema de análisis de abandono bancario (Churn) con Streamlit`
5. Visibilidad: **Public** (para que todos lo vean)
6. **No** inicialices con README (ya tienes uno)
7. Click "Create repository"

### Paso 3: Agregar Remote y Push

```bash
git remote add origin https://github.com/tu-usuario/ProyectoFinalUCG.git
git branch -M main
git push -u origin main
```

### Resultado
✅ Tu proyecto está en GitHub

**URL**: `https://github.com/tu-usuario/ProyectoFinalUCG`

---

## 🌐 Desplegar en Streamlit Cloud

### Requisitos
- ✅ Proyecto en GitHub
- ✅ Archivo `requirements.txt`
- ✅ Archivo `app.py`
- ✅ `.streamlit/config.toml` (opcional)

### Paso 1: Ir a Streamlit Cloud

Navega a [share.streamlit.io](https://share.streamlit.io)

### Paso 2: Crear Nueva App

1. Click en **"New app"**
2. Selecciona tu repositorio GitHub
   - Repositorio: `ProyectoFinalUCG`
   - Branch: `main`
   - Main file path: `app.py`
3. Click **"Deploy"**

### Paso 3: Esperar a que Desplegue

- Streamlit construirá la app automáticamente
- Mostrará logs en tiempo real
- En ~2 minutos tendrás tu app en vivo

### Resultado
✅ App disponible en: `https://tu-usuario-proyectofinalucg.streamlit.app`

---

## 🔧 Solucionar Problemas

### Error: "Module not found"
**Causa**: Falta una dependencia en `requirements.txt`
**Solución**: Agrega la dependencia y haz push

```bash
echo "nueva-libreria>=version" >> requirements.txt
git add requirements.txt
git commit -m "Agregar nueva dependencia"
git push
```

### Error: "CSV not found"
**Causa**: El archivo `data/Churn_Modelling.csv` no está en el repo
**Solución**: Verifica que esté en la carpeta `data/`

```bash
ls data/  # Ver archivos en data/
```

### Error de Importación en `app.py`
**Causa**: Ruta relativa incorrecta
**Solución**: Revisa que las importaciones usen rutas relativas:

```python
from src.config import APP_CONFIG  # ✅ Correcto
# NO hagas: from /src/config import APP_CONFIG  # ❌ Incorrecto
```

### App lenta
**Causa**: El caché no está funcionando
**Solución**: Revisa que `@st.cache_data` esté en `load_data()`

---

## 📝 Archivo de Configuración Avanzada

Si necesitas personalizar más, edita `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#1E3A8A"
backgroundColor = "#F9FAFB"
secondaryBackgroundColor = "#FFFFFF"
textColor = "#1F2937"
font = "sans serif"

[client]
showErrorDetails = true
toolbarMode = "minimal"

[server]
headless = true
port = 8501
runOnSave = true
maxUploadSize = 200
```

---

## 🔐 Variables de Entorno y Secretos

Si necesitas guardar claves secretas (API keys, contraseñas):

### Local (`.streamlit/secrets.toml`)
```toml
[database]
password = "tu-contraseña"
api_key = "tu-clave"
```

**⚠️ NUNCA** subas este archivo a GitHub.

### En Streamlit Cloud
1. Ve a tu app en share.streamlit.io
2. Click en "⋮ (menú)" → "Settings"
3. Ve a "Secrets"
4. Pega el contenido de `secrets.toml`
5. Save

Luego en tu código:
```python
import streamlit as st
password = st.secrets["database"]["password"]
```

---

## 📊 Monitorear tu App

### En Streamlit Cloud
- Panel de control con estadísticas
- Logs en tiempo real
- Métricas de tráfico
- Status de la app

### Localmente
```bash
# Ver logs
streamlit run app.py --logger.level=debug

# Ver argumentos disponibles
streamlit run --help
```

---

## 🔄 Actualizar después del Deployment

Cualquier cambio que hagas y subas a GitHub se desplegará automáticamente en Streamlit Cloud:

```bash
# Hacer cambios locales
# Editar archivos...

# Subir cambios
git add .
git commit -m "Descripción del cambio"
git push origin main

# ¡Listo! Streamlit actualizará automáticamente
```

**Tiempo**: Generalmente 30-60 segundos

---

## 📚 Mejores Prácticas

### 1. **Versionado**
```bash
# Hacer commits descriptivos
git commit -m "Fix: Corregir cálculo de promedio en exploracion.py"
```

### 2. **Branches**
```bash
# Para cambios importantes, usa ramas
git checkout -b feature/nuevas-visualizaciones
# ... hacer cambios ...
git push origin feature/nuevas-visualizaciones
# En GitHub, abre Pull Request
```

### 3. **Documentación**
- Actualiza README cuando agregas features
- Documenta cambios importantes
- Mantén CHANGELOG.md (opcional)

### 4. **Testing**
```bash
# Antes de push, prueba localmente
streamlit run app.py
```

---

## 🎯 Checklist de Deployment

### Antes de Hacer Push

- [ ] ¿Funciona localmente? (`streamlit run app.py`)
- [ ] ¿Están todos los archivos en el repo?
- [ ] ¿`requirements.txt` tiene todas las dependencias?
- [ ] ¿`data/Churn_Modelling.csv` está incluido?
- [ ] ¿Las importaciones son relativas?
- [ ] ¿No hay `.streamlit/secrets.toml` en el repo?
- [ ] ¿`.gitignore` excluye archivos sensibles?
- [ ] ¿README está actualizado?

### Después del Deployment

- [ ] ¿La app aparece en Streamlit Cloud?
- [ ] ¿Puedo acceder a la URL?
- [ ] ¿Carga el dataset correctamente?
- [ ] ¿Funcionan todas las páginas?
- [ ] ¿Se ven los estilos correctamente?
- [ ] ¿No hay errores en la consola?

---

## 🎉 Resultado Final

**Tu app está en línea:**
- 🌐 GitHub: `https://github.com/tu-usuario/ProyectoFinalUCG`
- 🚀 Streamlit Cloud: `https://tu-usuario-proyectofinalucg.streamlit.app`

**Comparte el enlace:**
```
¡Mira mi análisis de churn bancario!
https://tu-usuario-proyectofinalucg.streamlit.app
```

---

## 📞 Soporte

### Documentación Oficial
- [Streamlit Deployment Docs](https://docs.streamlit.io/streamlit-community-cloud)
- [GitHub Docs](https://docs.github.com)

### Comunidades
- [Streamlit Community Forum](https://discuss.streamlit.io)
- [Stack Overflow - Streamlit](https://stackoverflow.com/questions/tagged/streamlit)

### Contacto
- 📧 Universidad CASA GRANDE: info@casagrange.edu

---

**¡Tu aplicación está lista para el mundo! 🌍✨**
