"""
Estilos personalizados HTML/CSS para Streamlit
"""

from src.config import COLORS

def get_custom_css():
    """Retorna CSS personalizado para la aplicación"""
    
    css = f"""
    <style>
        /* Variables CSS */
        :root {{
            --primary: {COLORS['primary']};
            --secondary: {COLORS['secondary']};
            --success: {COLORS['success']};
            --warning: {COLORS['warning']};
            --danger: {COLORS['danger']};
            --light: {COLORS['light']};
            --dark: {COLORS['dark']};
            --border: {COLORS['border']};
        }}
        
        /* Estilos generales */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #F9FAFB;
            color: {COLORS['dark']};
        }}
        
        /* Encabezados */
        h1, h2, h3, h4, h5, h6 {{
            color: {COLORS['primary']};
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }}
        
        h1 {{
            font-size: 2.5rem;
            border-bottom: 3px solid {COLORS['secondary']};
            padding-bottom: 0.75rem;
        }}
        
        h2 {{
            font-size: 1.875rem;
            border-left: 4px solid {COLORS['secondary']};
            padding-left: 1rem;
        }}
        
        /* Separadores */
        hr {{
            border: none;
            height: 2px;
            background: linear-gradient(to right, {COLORS['primary']}, {COLORS['secondary']}, transparent);
            margin: 2rem 0;
        }}
        
        /* Tarjetas informativas */
        .metric-card {{
            background: white;
            border-left: 4px solid {COLORS['secondary']};
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        
        .metric-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }}
        
        /* Botones */
        button {{
            background-color: {COLORS['primary']};
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 6px;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 500;
        }}
        
        button:hover {{
            background-color: {COLORS['secondary']};
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba({int(COLORS['primary'][1:3], 16)}, {int(COLORS['primary'][3:5], 16)}, {int(COLORS['primary'][5:7], 16)}, 0.3);
        }}
        
        /* DataFrames */
        table {{
            background: white;
            border-collapse: collapse;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }}
        
        th {{
            background-color: {COLORS['primary']};
            color: white;
            padding: 1rem;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 0.875rem 1rem;
            border-bottom: 1px solid {COLORS['border']};
        }}
        
        tr:hover {{
            background-color: {COLORS['light']};
        }}
        
        /* Mensajes */
        .stSuccess {{
            background-color: #D1FAE5 !important;
            border-left: 4px solid {COLORS['success']} !important;
            color: #065F46 !important;
        }}
        
        .stError {{
            background-color: #FEE2E2 !important;
            border-left: 4px solid {COLORS['danger']} !important;
            color: #7F1D1D !important;
        }}
        
        .stWarning {{
            background-color: #FEF3C7 !important;
            border-left: 4px solid {COLORS['warning']} !important;
            color: #78350F !important;
        }}
        
        .stInfo {{
            background-color: #DBEAFE !important;
            border-left: 4px solid {COLORS['primary']} !important;
            color: #1E3A8A !important;
        }}
        
        /* Barra lateral */
        .sidebar .sidebar-content {{
            background-color: {COLORS['light']};
        }}
        
        .sidebar-header {{
            background: linear-gradient(135deg, {COLORS['primary']}, {COLORS['secondary']});
            color: white;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            font-weight: 600;
        }}
        
        /* Selectbox y inputs mejorados */
        .stSelectbox, .stMultiSelect, .stTextInput {{
            border-radius: 6px;
        }}
        
        .stSelectbox > div > div {{
            border-color: {COLORS['border']} !important;
        }}
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 2px;
        }}
        
        .stTabs [data-baseweb="tab"] {{
            background-color: {COLORS['light']};
            border-radius: 6px 6px 0 0;
        }}
        
        .stTabs [aria-selected="true"] {{
            background-color: {COLORS['primary']} !important;
            color: white !important;
        }}
        
        /* Gráficos */
        .stPlotlyContainer {{
            background: white;
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }}
        
        /* Contenedor principal */
        .main {{
            background-color: #F9FAFB;
        }}
        
        /* Columnas */
        .row-widget {{
            padding: 1rem;
        }}
        
        /* Cuadro de opciones */
        .option-box {{
            background: white;
            border: 2px solid {COLORS['border']};
            border-radius: 8px;
            padding: 1.5rem;
            margin: 1rem 0;
            transition: all 0.3s ease;
        }}
        
        .option-box:hover {{
            border-color: {COLORS['secondary']};
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }}
        
        .option-box.active {{
            border-color: {COLORS['secondary']};
            background-color: rgba({int(COLORS['secondary'][1:3], 16)}, {int(COLORS['secondary'][3:5], 16)}, {int(COLORS['secondary'][5:7], 16)}, 0.05);
        }}
        
        /* Títulos de secciones */
        .section-title {{
            color: {COLORS['primary']};
            font-size: 1.5rem;
            font-weight: 600;
            margin: 2rem 0 1rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid {COLORS['secondary']};
        }}
        
        /* Footer */
        .footer {{
            text-align: center;
            padding: 2rem;
            color: #999;
            border-top: 1px solid {COLORS['border']};
            margin-top: 3rem;
            font-size: 0.875rem;
        }}
        
    </style>
    """
    return css


def apply_custom_style():
    """Aplica estilos personalizados a la aplicación"""
    import streamlit as st
    st.markdown(get_custom_css(), unsafe_allow_html=True)


def get_header_html(title: str, icon: str = "🏦", subtitle: str = None):
    """Retorna HTML para un encabezado personalizado"""
    
    subtitle_html = f'<p style="font-size: 1.1rem; margin-top: 0.5rem; opacity: 0.9;">{subtitle}</p>' if subtitle else ""
    
    html = f"""<div style="background: linear-gradient(135deg, {COLORS['primary']}, {COLORS['secondary']}); padding: 2rem; border-radius: 8px; margin-bottom: 2rem; color: white;">
    <h1 style="color: white; border: none; margin: 0; padding: 0; font-size: 2.2rem;">{icon} {title}</h1>
    {subtitle_html}
</div>"""
    
    return html


def get_info_box(title: str, content: str, color: str = "info"):
    """Retorna HTML para una caja de información"""
    
    color_map = {
        "info": COLORS['primary'],
        "success": COLORS['success'],
        "warning": COLORS['warning'],
        "danger": COLORS['danger'],
    }
    
    icon_map = {
        "info": "ℹ️",
        "success": "✅",
        "warning": "⚠️",
        "danger": "❌",
    }
    
    border_color = color_map.get(color, COLORS['primary'])
    icon = icon_map.get(color, "ℹ️")
    
    html = f"""
    <div style="background: white; border-left: 4px solid {border_color}; 
                padding: 1.5rem; border-radius: 8px; margin: 1rem 0;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);">
        <strong style="color: {border_color}; font-size: 1.1rem;">{icon} {title}</strong>
        <p style="margin-top: 0.5rem; color: {COLORS['dark']};">{content}</p>
    </div>
    """
    return html
