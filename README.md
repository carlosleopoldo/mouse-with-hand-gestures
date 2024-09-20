# Detección de Gestos con Mediapipe para Control de Mouse

Este proyecto utiliza la biblioteca de `Mediapipe` de Google para detectar gestos de la mano a través de la cámara web y mapear esos gestos a diferentes acciones del mouse, como clics, doble clic y captura de pantalla.

## Gestos Soportados

El sistema puede detectar los siguientes gestos y realizar las correspondientes acciones:

1. **Movimiento del mouse**:  
   - **Gesto**: La punta del dedo índice se mueve por la pantalla.  
   - **Acción**: El cursor del mouse sigue el movimiento de la punta del dedo índice.

2. **Clic izquierdo**:  
   - **Gesto**: El dedo índice se dobla, mientras que el pulgar permanece extendido y separado.  
   - **Acción**: Se simula un clic izquierdo.

3. **Clic derecho**:  
   - **Gesto**: El dedo medio se dobla, mientras que el índice permanece extendido.  
   - **Acción**: Se simula un clic derecho.

4. **Doble clic**:  
   - **Gesto**: Tanto el dedo índice como el dedo medio están doblados.  
   - **Acción**: Se simula un doble clic.

5. **Captura de pantalla**:  
   - **Gesto**: Ambos dedos, el índice y el medio, están doblados y el pulgar está cerca del índice.  
   - **Acción**: Se toma una captura de pantalla y se guarda en la carpeta del proyecto con un nombre aleatorio.

## Requisitos del Sistema

- **Sistema Operativo**: 
  - Windows 10 o superior
  - macOS Catalina o superior
  - Linux (Ubuntu recomendado)
  
- **Python 3.7 o superior**

- **Bibliotecas necesarias**:
  - `opencv-python` para captura y procesamiento de video.
  - `mediapipe` para detección de manos.
  - `pyautogui` para controlar el mouse y tomar capturas de pantalla.
  - `pynput` para simular clics del mouse.
  - `random` (librería estándar de Python) para generar nombres de archivos de captura de pantalla aleatorios.
  - `util.py` (asegúrate de que esta librería esté presente o implementada para cálculo de ángulos y distancias entre puntos clave de los dedos).

## Instalación

1. **Instalar Python**: Si aún no tienes Python instalado, descárgalo desde [python.org](https://www.python.org/downloads/) e instálalo según tu sistema operativo.

2. **Instalar dependencias**:
   
   Navega a la carpeta del proyecto en la terminal o línea de comandos y ejecuta:

   ```bash
   pip install -r requirements.txt
