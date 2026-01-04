import streamlit as st

# -----------------------------
# Configuración básica de la app
# -----------------------------
st.set_page_config(
    page_title="VirusTotal Human",
    layout="centered"
)

# -----------------------------
# Título y descripción
# -----------------------------
st.title("🛡️ VirusTotal Human")
st.write(
    "Interpreta análisis de VirusTotal en lenguaje claro, "
    "sin pánico y sin conocimientos técnicos."
)

# -----------------------------
# Entrada del usuario
# -----------------------------
hash_input = st.text_input(
    "Ingresá el hash del archivo (SHA256):",
    placeholder="Pegá el hash acá"
)

# -----------------------------
# Botón
# -----------------------------
if st.button("Analizar"):
    if hash_input:
        st.success("Interfaz funcionando correctamente ✅")
    else:
        st.warning("Ingresá un hash válido.")
