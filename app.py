import streamlit as st
import re

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
# Función para extraer SHA256
# -----------------------------
def extraer_hash(texto):
    # Caso: URL de VirusTotal
    if "/file/" in texto:
        partes = texto.split("/file/")
        posible_hash = partes[-1].split("/")[0]
        return posible_hash

    # Caso: hash directo
    if re.fullmatch(r"[a-fA-F0-9]{64}", texto):
        return texto

    return None

# -----------------------------
# Entrada del usuario
# -----------------------------
entrada = st.text_input(
    "Ingresá el hash o el link de VirusTotal:",
    placeholder="Pegá el hash o la URL acá"
)

# -----------------------------
# Botón
# -----------------------------
if st.button("Analizar"):
    hash_archivo = extraer_hash(entrada)

    if hash_archivo:
        st.success("Hash detectado correctamente ✅")
        st.code(hash_archivo)
    else:
        st.error(
            "No se pudo detectar un hash válido.\n"
            "Pegá un SHA256 o un link de VirusTotal."
        )
