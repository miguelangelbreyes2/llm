import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(
    page_title="Asistente de Escritura Automática",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ Asistente de Escritura Automática con OpenAI")
st.write(
    "Este asistente utiliza la API de OpenAI para ayudarte a mejorar textos, "
    "corregir ortografía, sugerir continuaciones y generar textos desde cero."
)

st.sidebar.header("Configuración")

api_key_input = st.sidebar.text_input(
    "OpenAI API Key",
    type="password",
    help="Puedes escribir tu API Key aquí o guardarla en un archivo .env."
)

api_key = api_key_input or os.getenv("OPENAI_API_KEY")

modelo = st.sidebar.selectbox(
    "Modelo",
    ["gpt-5.4-mini", "gpt-5.5"],
    index=0
)

if not api_key:
    st.info("Ingresa tu OpenAI API Key en la barra lateral para comenzar.")
    st.stop()

client = OpenAI(api_key=api_key)


def generar_respuesta(instrucciones, entrada_usuario):
    response = client.responses.create(
        model=modelo,
        instructions=instrucciones,
        input=entrada_usuario
    )
    return response.output_text


tarea = st.selectbox(
    "¿Qué quieres hacer?",
    [
        "Mejorar redacción y ortografía",
        "Sugerir continuación",
        "Escribir un texto desde cero",
        "Resumir un texto",
        "Cambiar el tono de un texto"
    ]
)

if tarea == "Mejorar redacción y ortografía":
    texto = st.text_area("Pega aquí tu texto:", height=180)

    if st.button("Mejorar texto"):
        if texto.strip():
            with st.spinner("Mejorando tu texto..."):
                instrucciones = """
                Eres un asistente experto en escritura.
                Corrige ortografía, gramática, puntuación y mejora la claridad del texto.
                Mantén la idea principal del usuario.
                Devuelve únicamente el texto corregido y mejorado.
                """
                respuesta = generar_respuesta(instrucciones, texto)
                st.subheader("Texto mejorado")
                st.write(respuesta)
        else:
            st.warning("Primero escribe un texto.")

elif tarea == "Sugerir continuación":
    texto = st.text_area("Escribe el inicio de tu texto:", height=180)

    if st.button("Sugerir continuación"):
        if texto.strip():
            with st.spinner("Generando continuación..."):
                instrucciones = """
                Eres un asistente creativo de escritura.
                Continúa el texto del usuario con un párrafo coherente.
                Respeta el estilo, el tema y el tono del texto original.
                """
                respuesta = generar_respuesta(instrucciones, texto)
                st.subheader("Continuación sugerida")
                st.write(respuesta)
        else:
            st.warning("Primero escribe el inicio del texto.")

elif tarea == "Escribir un texto desde cero":
    tema = st.text_input("¿Sobre qué tema quieres escribir?")
    tipo_texto = st.selectbox(
        "Tipo de texto",
        ["Correo electrónico", "Artículo", "Publicación para redes sociales", "Ensayo corto", "Historia creativa"]
    )
    tono = st.selectbox(
        "Tono",
        ["Profesional", "Casual", "Creativo", "Persuasivo", "Académico"]
    )

    if st.button("Generar texto"):
        if tema.strip():
            with st.spinner("Escribiendo texto..."):
                entrada = f"""
                Tema: {tema}
                Tipo de texto: {tipo_texto}
                Tono: {tono}
                """
                instrucciones = """
                Eres un asistente de escritura automática.
                Genera un texto completo, claro y útil según el tema, tipo de texto y tono solicitado.
                """
                respuesta = generar_respuesta(instrucciones, entrada)
                st.subheader("Texto generado")
                st.write(respuesta)
        else:
            st.warning("Primero escribe un tema.")

elif tarea == "Resumir un texto":
    texto = st.text_area("Pega el texto que quieres resumir:", height=220)

    if st.button("Resumir"):
        if texto.strip():
            with st.spinner("Resumiendo..."):
                instrucciones = """
                Eres un asistente experto en síntesis de información.
                Resume el texto del usuario de forma clara, breve y ordenada.
                Conserva las ideas principales.
                """
                respuesta = generar_respuesta(instrucciones, texto)
                st.subheader("Resumen")
                st.write(respuesta)
        else:
            st.warning("Primero pega un texto.")

elif tarea == "Cambiar el tono de un texto":
    texto = st.text_area("Pega el texto original:", height=180)
    nuevo_tono = st.selectbox(
        "Nuevo tono",
        ["Más profesional", "Más amable", "Más formal", "Más persuasivo", "Más sencillo"]
    )

    if st.button("Cambiar tono"):
        if texto.strip():
            with st.spinner("Reescribiendo texto..."):
                entrada = f"""
                Texto original:
                {texto}

                Nuevo tono:
                {nuevo_tono}
                """
                instrucciones = """
                Eres un asistente experto en estilo de escritura.
                Reescribe el texto con el nuevo tono solicitado.
                Mantén el significado original.
                Devuelve únicamente la nueva versión del texto.
                """
                respuesta = generar_respuesta(instrucciones, entrada)
                st.subheader("Texto reescrito")
                st.write(respuesta)
        else:
            st.warning("Primero pega un texto.")