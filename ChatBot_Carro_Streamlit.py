import streamlit as st
import requests
import json
import os
import serial

# CONFIGURACION BLUETOOTH
# Se debe ajustar el puerto según el módulo Bluetooth: En Windows suele ser COM5, COM6...

try:
    bt = serial.Serial("COM5", 9600, timeout=1)  # Cambia COM5 por tu puerto real
except Exception as e:
    bt = None
    st.sidebar.error(f"No se pudo abrir el puerto Bluetooth: {e}")

# CONFIGURACION CONEXION IA - GEMINI
API_KEY = "API_KEY_GEMINI"  # Genera tu propia API KEY en https://aistudio.google.com/
MODELO = "models/gemini-2.5-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/{MODELO}:generateContent?key={API_KEY}"

# SEGMENTACION ESPECIALIZADA - PROMPT DEL CHATBOT
SYSTEM_PROMPT = """
Eres un asistente especializado en Sistemas Digitales.
Además de explicar conceptos, puedes recibir comandos para controlar un carro seguidor de líneas:
- 'avanzar' o 'W' → enviar comando 'F' por Bluetooth
- 'izquierda' o 'A' → enviar comando 'L'
- 'derecha' o 'D' → enviar comando 'R'
- 'detener' o 'S' → enviar comando 'S'
También puedes explicar la construcción del carro, los sensores de color y cómo se integra con Streamlit.
"""

# FUNCION DE PREGUNTA IA - GEMINI
def preguntar_gemini(mensaje_usuario):
    payload = {
        "contents": [{
            "parts": [
                {"text": SYSTEM_PROMPT},
                {"text": f"Pregunta: {mensaje_usuario}"}
            ]
        }]
    }
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(URL, headers=headers, data=json.dumps(payload))
        res_json = response.json()
        if response.status_code == 200:
            return res_json['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"❌ Error {response.status_code}: {res_json.get('error', {}).get('message', 'Error desconocido')}"
    except Exception as e:
        return f"❌ Error de conexión: {str(e)}"

# FUNCION LEER COLOR
def leer_color():
    if bt and bt.in_waiting > 0:
        return bt.readline().decode().strip()
    return None

# FUNCION CONTROL CARRO
def enviar_comando(comando):
    if bt:
        bt.write(comando.encode())

# INTERFAZ STREAMLIT
st.title("🚗 Carro Seguidor de Líneas con Chatbot")

# Panel lateral: color detectado
st.sidebar.subheader("🎨 Color detectado en tiempo real")
color_actual = leer_color()
if color_actual:
    st.sidebar.write(f"El carro está sobre: **{color_actual}**")
else:
    st.sidebar.write("Esperando datos del carro...")

# Historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for sender, text in st.session_state.messages:
    with st.chat_message(sender):
        st.markdown(text)

# Entrada estilo chat
user_input = st.chat_input("Escribe tu mensaje...")
if user_input:
    # Mostrar mensaje del usuario
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # CONTROL DEL CARRO
    if "avanzar" or "W" in user_input.lower():
        enviar_comando("F")
    elif "izquierda" or "A" in user_input.lower():
        enviar_comando("L")
    elif "derecha" or "D" in user_input.lower():
        enviar_comando("R")
    elif "detenter" or "S" in user_input.lower():
        enviar_comando("S")

    # RESPUESTA DEL BOT
    respuesta = preguntar_gemini(user_input)
    st.session_state.messages.append(("assistant", respuesta))
    with st.chat_message("assistant"):
        st.markdown(respuesta)
