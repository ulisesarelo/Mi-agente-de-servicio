import streamlit as st
from urllib.parse import quote

# 1. Configuración de la página (¡Importante para celular!)
st.set_page_config(
    page_title="EcoClean Assist - Presupuestador",
    page_icon="🌱",
    layout="centered", # Centrado para que se vea mejor en PC y Mobile
    initial_sidebar_state="collapsed"
)

# --- 2. ESTILOS CSS PERSONALIZADOS (El "Maquillaje") ---
# Esto cambia colores, bordes y espaciados para que no parezca un formulario estándar.
st.markdown("""
<style>
    /* Fondo de la app y color de texto base */
    .stApp {
        background-color: #f9fbf9;
        color: #2c3e50;
    }
    
    /* Estilo para los títulos principales */
    h1, h2, h3 {
        color: #1e8449 !important; /* Un verde oscuro profesional */
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
    }
    
    /* Contenedor del formulario (Sombra y bordes redondeados) */
    .stForm {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #e0e0e0;
    }
    
    /* Estilo para las etiquetas de los campos */
    .stMarkdown p {
        font-size: 1.05rem;
        color: #34495e;
    }

    /* Estilo del botón de enviar (VERDE) */
    div.stButton > button:first-child {
        background-color: #27ae60;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 12px 24px;
        font-weight: bold;
        width: 100%; /* Botón ancho total en celular */
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #2ecc71;
        transform: translateY(-2px);
    }
    
    /* Estilo del resultado final (El cuadro de éxito) */
    .stAlert {
        border-radius: 10px;
        border: 2px solid #27ae60;
        background-color: #e8f8f5;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. CABECERA (Logo y Título Visual) ---
col1, col2, col3 = st.columns([1,2,1]) # Columnas para centrar el logo
with col2:
    # URL de un logo de ejemplo (Podés cambiar esta URL por la de tu logo real)
    logo_url = "https://raw.githubusercontent.com/ulisesarelo/Mi-agente-de-servicio/main/logo_ecoclean.png" # Si subís tu logo a GitHub, usá esa URL raw.
    try:
        st.image(logo_url, width=150) # Intenta cargar el logo
    except:
        st.markdown("<h1 style='text-align: center;'>🌱 EcoClean</h1>", unsafe_allow_html=True) # Fallback si no hay logo

st.markdown("<h3 style='text-align: center; color: #7f8c8d; font-weight: normal; margin-top: -15px;'>Tu presupuesto rápido y fácil</h3>", unsafe_allow_html=True)
st.markdown("---") # Línea divisoria


# --- 4. LÓGICA DE NEGOCIO (Los precios siguen igual) ---
PRECIO_M2_CESPED = 600
PRECIO_HORA_LIMPIEZA = 4000
# Reemplazá este número con tu celular REAL (con código de país, sin el +)
MI_TELEFONO_WHATSAPP = "3407405533" 

# --- 5. EL FORMULARIO (
