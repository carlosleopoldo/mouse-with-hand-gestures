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

## Instalación

1. **Instalar Python**: Si aún no tienes Python instalado, descárgalo desde [python.org](https://www.python.org/downloads/) e instálalo según tu sistema operativo.

2. **Instalar dependencias**:
   
   Navega a la carpeta del proyecto en la terminal o línea de comandos y ejecuta:

   ```bash
   pip install -r requirements.txt
   ```
   
3. **Verificar instalación**: Para asegurarte de que todas las bibliotecas se instalaron correctamente, puedes ejecutar el siguiente comando en la terminal:

   ```bash
   python -m pip show opencv-python mediapipe pyautogui pynput
   ```

## Ejecución del Código

1. **Iniciar la cámara**: Asegúrate de que tu cámara web esté conectada y funcionando.

2. **Ejecutar el programa**: En la terminal o línea de comandos, navega hasta la carpeta del proyecto y ejecuta:

   ```bash
   python main.py
   ```

   Donde `main.py` es el nombre del archivo donde tienes guardado el código principal.

3. **Interacción**: Al ejecutar el programa, la ventana mostrará la imagen de la cámara y los puntos clave de la mano detectada. Utiliza los gestos mencionados anteriormente para controlar el mouse. 

4. **Salir del programa**: Para salir del programa, cierra la ventana o presiona la tecla `q` en la ventana de OpenCV.

## Notas

- **Cámara**: El programa utiliza la cámara por defecto de tu sistema. Si tienes más de una cámara conectada, ajusta el índice del dispositivo en la línea `cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)` para seleccionar otra cámara.
  
- **Plataforma**: Este código ha sido probado en Windows y macOS. En Linux puede requerir ajustes para la captura de video y control del mouse.

## Contribuciones

Si tienes sugerencias o mejoras para el proyecto, siéntete libre de enviar un `pull request` o abrir un `issue`.

## Licencia

Este proyecto está bajo la Licencia MIT. Puedes consultar el archivo `LICENSE` para más detalles.
```

### Resumen:
- **Gestos explicados**: Detallo cada gesto que puede detectar el código y la acción correspondiente.
- **Requisitos**: Incluyo una lista clara de los requerimientos del sistema y las bibliotecas necesarias.
- **Instalación**: Instrucciones sobre cómo instalar Python y las dependencias necesarias.
- **Ejecución**: Explico cómo correr el programa y cómo interactuar con él.
- **Notas adicionales**: Información sobre la cámara y compatibilidad en distintos sistemas operativos.