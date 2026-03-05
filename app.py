import streamlit as st
from urllib.parse import quote

# 1. Configuración de la página
st.set_page_config(
    page_title="EcoClean Assist - Presupuestador",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
<style>
    .stApp { background-color: #f9fbf9; color: #2c3e50; }
    h1, h2, h3 { color: #1e8449 !important; font-family: 'Helvetica Neue', sans-serif; font-weight: 700; }
    .stForm { background-color: #ffffff; padding: 2rem; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #e0e0e0; }
    div.stButton > button:first-child { background-color: #27ae60; color: white; border-radius: 8px; border: none; padding: 12px 24px; font-weight: bold; width: 100%; transition: all 0.3s ease; }
    div.stButton > button:first-child:hover { background-color: #2ecc71; transform: translateY(-2px); }
    .stAlert { border-radius: 10px; border: 2px solid #27ae60; background-color: #e8f8f5; }
</style>
""", unsafe_allow_html=True)

# --- 3. CABECERA ---
st.markdown("<h1 style='text-align: center;'>🌱 EcoClean</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #7f8c8d; font-weight: normal; margin-top: -15px;'>Tu presupuesto rápido y fácil</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- 4. LÓGICA DE NEGOCIO ---
PRECIO_M2_CESPED = 600
PRECIO_HORA_LIMPIEZA = 4000
MI_TELEFONO_WHATSAPP = "5493407405533" 

# --- 5. EL FORMULARIO ---
with st.form("presupuestador_estetico"):
    st.markdown("#### 🛠️ 1. Elegí tu Servicio")
    servicio = st.multiselect("", ["Corte de Césped", "Limpieza de Hogar"])
    
    m2 = 0
    horas = 0
    estado_pasto = "Normal"
    
    if servicio:
        st.markdown("#### 📏 2. Detalles del Trabajo")
        c1, c2 = st.columns(2)
        if "Corte de Césped" in servicio:
            with c1:
                m2 = st.number_input("Metros cuadrados ($m^2$):", min_value=0, step=10)
                estado_pasto = st.selectbox("Estado actual:", ["Normal", "Maleza Alta (+20%)"])
        if "Limpieza de Hogar" in servicio:
            with c2:
                horas = st.number_input("Horas estimadas:", min_value=0, step=1)

    st.markdown("#### 📍 3. ¿Dónde y Cuándo?")
    ciudad = st.text_input("Ciudad")
    direccion = st.text_input("Dirección Exacta")
    col_f, col_h = st.columns(2)
    with col_f: fecha = st.date_input("Día")
    with col_h: horario = st.time_input("Horario")

    enviado = st.form_submit_button("💰 CALCULAR PRESUPUESTO")

# --- 6. RESULTADOS ---
if enviado:
    if not servicio or not ciudad or not direccion:
        st.warning("⚠️ Completá todos los campos.")
    else:
        total_cesped = m2 * PRECIO_M2_CESPED
        if "Maleza Alta" in estado_pasto: total_cesped *= 1.2
        total_limpieza = horas * PRECIO_HORA_LIMPIEZA
        total_final = total_cesped + total_limpieza
        
        st.success(f"### ✅ Total Estimado: ${total_final:,.2f}")
        
        mensaje_wa = quote(f"¡Hola! Quiero agendar: {', '.join(servicio)}. Ubicación: {direccion}, {ciudad}. Fecha: {fecha} a las {horario}. Total: ${total_final:,.2f}")
        link_whatsapp = f"https://wa.me/{MI_TELEFONO_WHATSAPP}?text={mensaje_wa}"
        
        st.markdown(f'<a href="{link_whatsapp}" target="_blank"><button style="background-color: #25D366; color: white; border-radius: 10px; border: none; padding: 15px; width: 100%; font-weight: bold; cursor: pointer;">📲 SOLICITAR POR WHATSAPP</button></a>', unsafe_allow_html=True)
        st.balloons()
