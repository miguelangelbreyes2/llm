\# Asistente de Escritura Automática con OpenAI



Este proyecto consiste en un asistente de escritura automática desarrollado con Python, Streamlit y la API de OpenAI.



La aplicación permite al usuario mejorar textos, corregir ortografía y gramática, generar textos desde cero, resumir contenido, sugerir continuaciones y cambiar el tono de un texto. Su objetivo es demostrar cómo un Modelo de Lenguaje de Gran Escala puede utilizarse para crear una herramienta práctica de apoyo a la escritura.



\## Funcionalidades



El asistente cuenta con las siguientes funciones principales:



\* Mejorar redacción y ortografía.

\* Sugerir la continuación de un texto.

\* Escribir textos desde cero a partir de un tema.

\* Resumir textos largos.

\* Cambiar el tono de un texto, por ejemplo, a profesional, amable, formal o persuasivo.



\## Tecnologías utilizadas



\* Python

\* Streamlit

\* OpenAI API

\* python-dotenv



\## Estructura del proyecto



```text

llm/

├── README.md

├── .gitignore

└── asistente\\\_escritura/

\&#x20;   ├── app.py

\&#x20;   ├── requirements.txt

\&#x20;   └── .env.example

```



\## Requisitos previos



Antes de ejecutar el proyecto, es necesario contar con:



\* Python 3.12 o superior instalado.

\* Una API Key válida de OpenAI.

\* Git instalado en el equipo.



\## Instalación



Primero, clona el repositorio:



```bash

git clone URL\\\_DE\\\_TU\\\_REPOSITORIO

```



Entra a la carpeta del proyecto:



```bash

cd llm

```



Crea un entorno virtual:



```bash

python -m venv .venv

```



En caso de usar Windows y que el comando anterior no funcione, puedes usar:



```bash

py -3.12 -m venv .venv

```



Activa el entorno virtual en Windows PowerShell:



```bash

.\\\\.venv\\\\Scripts\\\\activate

```



Después instala las dependencias:



```bash

pip install -r asistente\\\_escritura/requirements.txt

```



\## Configuración de la API Key



Dentro de la carpeta `asistente\\\_escritura`, crea un archivo llamado `.env`.



El archivo debe contener la siguiente variable:



```env

OPENAI\\\_API\\\_KEY=coloca\\\_tu\\\_api\\\_key\\\_aqui

```



Por seguridad, el archivo `.env` no debe subirse a GitHub. Para eso, el proyecto incluye un archivo `.gitignore`.



También se incluye un archivo `.env.example` como referencia para que otros usuarios sepan qué variable deben configurar.



\## Ejecución del proyecto



Desde la carpeta principal del proyecto, entra a la carpeta de la aplicación:



```bash

cd asistente\\\_escritura

```



Ejecuta la aplicación con Streamlit:



```bash

streamlit run app.py

```



Después de ejecutar el comando, Streamlit abrirá una ventana en el navegador. Si no se abre automáticamente, se puede ingresar manualmente a la dirección local que aparece en la terminal, normalmente:



```text

http://localhost:8501

```



\## Ejemplo de uso



Texto original:



```text

hola maestro le escribo para desirle que no pude entregar la tarea por que tube problemas con mi computadora

```



Respuesta generada por el asistente:



```text

Hola, maestro. Le escribo para decirle que no pude entregar la tarea porque tuve problemas con mi computadora.

```



\## Descripción del funcionamiento



La aplicación recibe una entrada del usuario desde una interfaz creada con Streamlit. Según la opción seleccionada, se construyen instrucciones específicas para el modelo de OpenAI.



Después, la aplicación envía la solicitud a la API de OpenAI y muestra la respuesta generada en pantalla.



Este flujo permite simular un producto funcional de usuario final basado en inteligencia artificial generativa.



\## Notas de seguridad



La API Key de OpenAI debe mantenerse privada. Por esta razón:



\* No se debe subir el archivo `.env` al repositorio.

\* El archivo `.env.example` solo sirve como guía.

\* Cada usuario debe configurar su propia API Key para ejecutar el proyecto.



\## Autor



Proyecto desarrollado por Miguel Angel Barragan Reyes como parte de una práctica de integración de Modelos de Lenguaje de Gran Escala mediante la API de OpenAI.

