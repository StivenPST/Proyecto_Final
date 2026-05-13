# Proyecto Final - Chatbot + Carro Seguidor de Linea
## Autores
* **Nombres:** Edwin Stiven Pasto Arévalo / Julian Felipe Romero Bocanegra / Yessika Vanessa Casas Casas
* **Carrera:** Ingeniería de Sistemas / Sistemas Digitales
* **Docente:** Diego Alejandro Barragan Vargas

## ♦ Objetivo 

## ♦ Materiales Necesarios

## ♦ Codigo ChatBot - Streamlit
### Concideraciones Previas
Este chatbot usa la API de Gemini. Para ejecutarlo se necesita una clave propia:
1. Ingresa a [Google AI Studio](https://aistudio.google.com/).
2. Genera una API Key.
3. Abre el archivo `chatbot_arduino.py`.
4. Reemplaza el texto `"API_KEY_GEMINI"` en la variable `API_KEY` por tu clave.

### Configuración Puerto Serial - Bluetooth
Se establece conexion entre la maquina y un dispositivo **Arduino** mediante el puerto serial `COM4` (*El puerto varia dependiendo del sistema operativo y del conector USB que se utilice en la maquina*)
Esto permite que el ChatBot envie señales al modulo Bluetooth configurado en el Arduino.

### Configuración Conexion IA - Gemini
En esta parte del codigo se establece la conexion con la API Gemini haciendo uso de las variables:
- `API_KEY`: Esta clave autentica las solicitudes.
-  `MODEL`: Especifica la version de lenguaje que usara Gemini.
-  `URL`: Define el enlace donde se enviaran las solicitudes.

### Segmentacion Especializada
Se define el comportamiento del ChatBot, indicando como debe responder a las solicitudes del usuario, asi como los comandos definidos para el control del carro segudir de linea mediante envio de señales Bluetooth hacia el Arduino.
Esta definicion se logra mediante la variable `SYSTEM_PROMPT`.

### Funcion De Pregunta IA
Envia las preguntas del usuario generando un `payload` que junta el `SYSTEM_PROMPT` con la `pregunta` del usuario. Adicionalmente al resivir los comandos de control predefinidos para el carro, hace el envio de dichos comandos. Ademas si ocurre algun error en este proceso el ChatBot lo informa al usuario. 

### Funcion Leer Color
### Funcion Control Carro 

### Interfaz Streamlit

#### Control Carro - Arduino --- Editar ---
El ChatBot interactua con el Arduino segun las ordenes que envie el usuario:
- **encender verde:** Envia comando  `ON_VERDE` al Arduino.
- **encender rojo:** Envia comando  `ON_ROJO` al Arduino.
- **apagar verde:** Envia comando  `OFF_VERDE` al Arduino.
- **apagar rojo:** Envia comando  `OFF_ROJO` al Arduino.
- **Temperatura:** Envia el comando  `TEMP` para pedir la temperatura al Arduino y muestrarla al usuario.



