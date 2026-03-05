import streamlit as st

# Configuración de la página
st.set_page_config(page_title="EcoClean Assist", page_icon="🌱")

# Títulos y Estética
st.title("🌱 EcoClean Assist")
st.subheader("Presupuestador de Limpieza y Césped")

# --- LÓGICA DE NEGOCIO ---
PRECIO_M2_CESPED = 600
PRECIO_HORA_LIMPIEZA = 4000

# --- INTERFAZ DE USUARIO ---
with st.form("presupuestador"):
    st.write("### 📝 Datos del Servicio")
    
    servicio = st.multiselect("¿Qué servicios necesitas?", ["Corte de Césped", "Limpieza de Hogar"])
    
    col1, col2 = st.columns(2)
    
    m2 = 0
    horas = 0
    
    if "Corte de Césped" in servicio:
        m2 = col1.number_input("Metros cuadrados ($m^2$):", min_value=0, step=10)
        estado_pasto = col1.selectbox("Estado del pasto:", ["Normal", "Maleza Alta (+20%)"])
        
    if "Limpieza de Hogar" in servicio:
        horas = col2.number_input("Horas estimadas:", min_value=0, step=1)

    st.write("### 📍 Datos de Contacto")
    ciudad = st.text_input("Ciudad")
    direccion = st.text_input("Dirección Exacta")
    fecha = st.date_input("Día para el servicio")
    horario = st.time_input("Horario preferido")

    enviado = st.form_submit_button("Calcular Presupuesto")

# --- CÁLCULOS ---
if enviado:
    total_cesped = m2 * PRECIO_M2_CESPED
    if "Maleza Alta" in locals() and estado_pasto == "Maleza Alta (+20%)":
        total_cesped *= 1.2
    
    total_limpieza = horas * PRECIO_HORA_LIMPIEZA
    total_final = total_cesped + total_limpieza
    
    if total_final > 0 and ciudad and direccion:
        st.success(f"### ✅ Presupuesto Estimado: ${total_final:,.2f}")
        st.info(f"**Resumen:** {m2}m² de césped y {horas}hs de limpieza en {ciudad}, {direccion} para el día {fecha} a las {horario}.")
        
        # Botón para enviar por WhatsApp (Opcional)
        mensaje_wa = f"Hola EcoClean! Quiero agendar: {m2}m2 de césped y {horas}hs de limpieza en {direccion}, {ciudad} para el {fecha} a las {horario}. Total: ${total_final}"
        st.link_button("📲 Enviar pedido por WhatsApp", f"https://wa.me/TU_TELEFONO_AQUI?text={mensaje_wa}")
    else:
        st.error("Por favor, completá todos los campos para generar el presupuesto.")
