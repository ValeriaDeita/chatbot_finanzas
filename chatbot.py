import pdfplumber
from groq import Groq
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extraer_texto(pdf_file):
  texto = ""
  with pdfplumber.open("catalogo.pdf") as pdf:
    for page in pdf.pages:
      texto += page.extract_text() or ""
  return texto 
    
def preguntar(documento_texto, historial):
    mensajes = [
        {
            "role": "system",
            "content": f"""Eres un asesor financiero amigable de AutoFinancia MX.
Usa SOLO la información del siguiente catálogo para responder.
Si te preguntan por mensualidades, calcula usando la fórmula de amortización.
Responde siempre en español, de forma clara y breve.

CATÁLOGO:
{documento_texto}"""
        }
    ] + historial

    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=mensajes,
        max_tokens=500
    )
    return respuesta.choices[0].message.content

st.set_page_config(page_title="AutoFinancia MX", page_icon="🚗")
st.title("🚗 AutoFinancia MX")
st.caption("Hola, bienvenido al asistente virtual de Chatbot de AutoFinancia MX. " 
"En el podrás cotizar mensualidades, consultar el catálogo, conocer las tasas, los requisitos del crédito, etc.")
with st.expander("¿Cómo usar este chatbot?"):
    st.markdown("""

    **Ejemplos de preguntas que puedes hacer:**
    
    > *"¿Cuánto pagaría mensual por el Aveo a 24 meses con 20% de enganche?"*
                
    > *"¿Qué tasa de interés tienen para seminuevos?"*
                
    > *"¿Qué documentos necesito para solicitar el crédito?"*
    
    ---
    
    **Nota:** El chatbot responde únicamente con información del catálogo cargado.
    """)
texto_catalogo = extraer_texto("catalogo.pdf")

if "historial" not in st.session_state:
    st.session_state.historial = []

for msg in st.session_state.historial:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

pregunta = st.chat_input("¿Qué quieres saber?")

if pregunta:
    with st.chat_message("user"):
        st.write(pregunta)
    st.session_state.historial.append({"role": "user", "content": pregunta})

    with st.chat_message("assistant"):
        with st.spinner("Calculando..."):
            respuesta = preguntar(texto_catalogo, st.session_state.historial)
        st.write(respuesta)
    st.session_state.historial.append({"role": "assistant", "content": respuesta})