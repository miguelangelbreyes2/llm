import streamlit as st

from config.settings import (
    APP_TITLE,
    APP_ICON,
    OPENAI_API_KEY,
    AVAILABLE_MODELS,
    DEFAULT_MODEL
)
from services.openai_provider import OpenAIProvider
from services.writing_assistant import WritingAssistant


st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="centered"
)

st.title(f"{APP_ICON} {APP_TITLE}")

st.write(
    "Esta aplicación utiliza la API de OpenAI para ayudar al usuario a mejorar textos, "
    "corregir redacción, generar contenido, resumir información y cambiar el tono de un escrito."
)

st.sidebar.header("Configuración")

api_key_input = st.sidebar.text_input(
    "OpenAI API Key",
    type="password",
    help="Puedes escribir tu API Key aquí o guardarla en un archivo .env."
)

api_key = api_key_input or OPENAI_API_KEY

modelo = st.sidebar.selectbox(
    "Modelo",
    AVAILABLE_MODELS,
    index=AVAILABLE_MODELS.index(DEFAULT_MODEL)
)

if not api_key:
    st.info("Ingresa tu OpenAI API Key en la barra lateral o configúrala en el archivo .env.")
    st.stop()

openai_provider = OpenAIProvider(
    api_key=api_key,
    model=modelo
)

assistant = WritingAssistant(openai_provider)

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
                respuesta = assistant.procesar("mejorar_texto", texto)
                st.subheader("Texto mejorado")
                st.write(respuesta)
        else:
            st.warning("Primero escribe un texto.")

elif tarea == "Sugerir continuación":
    texto = st.text_area("Escribe el inicio de tu texto:", height=180)

    if st.button("Sugerir continuación"):
        if texto.strip():
            with st.spinner("Generando continuación..."):
                respuesta = assistant.procesar("sugerir_continuacion", texto)
                st.subheader("Continuación sugerida")
                st.write(respuesta)
        else:
            st.warning("Primero escribe el inicio del texto.")

elif tarea == "Escribir un texto desde cero":
    tema = st.text_input("¿Sobre qué tema quieres escribir?")

    tipo_texto = st.selectbox(
        "Tipo de texto",
        [
            "Correo electrónico",
            "Artículo",
            "Publicación para redes sociales",
            "Ensayo corto",
            "Historia creativa"
        ]
    )

    tono = st.selectbox(
        "Tono",
        [
            "Profesional",
            "Casual",
            "Creativo",
            "Persuasivo",
            "Académico"
        ]
    )

    if st.button("Generar texto"):
        if tema.strip():
            entrada = f"""
            Tema: {tema}
            Tipo de texto: {tipo_texto}
            Tono: {tono}
            """

            with st.spinner("Escribiendo texto..."):
                respuesta = assistant.procesar("escribir_desde_cero", entrada)
                st.subheader("Texto generado")
                st.write(respuesta)
        else:
            st.warning("Primero escribe un tema.")

elif tarea == "Resumir un texto":
    texto = st.text_area("Pega el texto que quieres resumir:", height=220)

    if st.button("Resumir"):
        if texto.strip():
            with st.spinner("Resumiendo..."):
                respuesta = assistant.procesar("resumir_texto", texto)
                st.subheader("Resumen")
                st.write(respuesta)
        else:
            st.warning("Primero pega un texto.")

elif tarea == "Cambiar el tono de un texto":
    texto = st.text_area("Pega el texto original:", height=180)

    nuevo_tono = st.selectbox(
        "Nuevo tono",
        [
            "Más profesional",
            "Más amable",
            "Más formal",
            "Más persuasivo",
            "Más sencillo"
        ]
    )

    if st.button("Cambiar tono"):
        if texto.strip():
            entrada = f"""
            Texto original:
            {texto}

            Nuevo tono:
            {nuevo_tono}
            """

            with st.spinner("Reescribiendo texto..."):
                respuesta = assistant.procesar("cambiar_tono", entrada)
                st.subheader("Texto reescrito")
                st.write(respuesta)
        else:
            st.warning("Primero pega un texto.")