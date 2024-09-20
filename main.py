import cv2
import mediapipe as mp
import pyautogui
import random
import util
from pynput.mouse import Button, Controller

# Controlador del mouse para realizar acciones de clic
mouse = Controller()

# Obtenemos las dimensiones de la pantalla
screen_width, screen_height = pyautogui.size()

# Inicializamos el modelo de detección de manos de MediaPipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,  # Modo dinámico para imágenes en movimiento
    model_complexity=1,       # Complejidad del modelo de detección
    min_detection_confidence=0.7,  # Confianza mínima de detección
    min_tracking_confidence=0.7,   # Confianza mínima para el seguimiento
    max_num_hands=1               # Detectar solo una mano
)

# Función para obtener la coordenada de la punta del dedo índice
def find_finger_tip(processed):
    if processed.multi_hand_landmarks:
        hand_landmarks = processed.multi_hand_landmarks[0]  # Asumimos que solo una mano es detectada
        index_finger_tip = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
        return index_finger_tip
    return None, None

# Función para mover el mouse según la posición de la punta del dedo índice
def move_mouse(index_finger_tip):
    if index_finger_tip is not None:
        x = int(index_finger_tip.x * screen_width)  # Mapeamos la coordenada 'x' a la pantalla
        y = int(index_finger_tip.y / 2 * screen_height)  # Mapeamos la coordenada 'y' a la pantalla
        pyautogui.moveTo(x, y)

# Función para detectar si el gesto actual corresponde a un clic izquierdo
def is_left_click(landmark_list, thumb_index_dist):
    return (
        util.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and  # Ángulo entre puntos clave de los dedos
        util.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) > 90 and
        thumb_index_dist > 50  # Distancia entre el pulgar y el índice
    )

# Función para detectar si el gesto actual corresponde a un clic derecho
def is_right_click(landmark_list, thumb_index_dist):
    return (
        util.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and
        util.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) > 90 and
        thumb_index_dist > 50
    )

# Función para detectar si el gesto actual corresponde a un doble clic
def is_double_click(landmark_list, thumb_index_dist):
    return (
        util.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and
        util.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and
        thumb_index_dist > 50
    )

# Función para detectar si el gesto actual corresponde a una captura de pantalla
def is_screenshot(landmark_list, thumb_index_dist):
    return (
        util.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and
        util.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and
        thumb_index_dist < 50
    )

# Función principal para detectar gestos y realizar acciones correspondientes
def detect_gesture(frame, landmark_list, processed):
    if len(landmark_list) >= 21:  # Verificamos que se hayan detectado suficientes puntos

        # Obtenemos la posición de la punta del índice y la distancia entre pulgar e índice
        index_finger_tip = find_finger_tip(processed)
        thumb_index_dist = util.get_distance([landmark_list[4], landmark_list[5]])

        # Detectamos el gesto y ejecutamos la acción correspondiente
        if util.get_distance([landmark_list[4], landmark_list[5]]) < 50 and util.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) > 90:
            move_mouse(index_finger_tip)  # Movimiento del mouse
        elif is_left_click(landmark_list, thumb_index_dist):
            mouse.press(Button.left)
            mouse.release(Button.left)  # Clic izquierdo
            cv2.putText(frame, "Click izquierdo", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        elif is_right_click(landmark_list, thumb_index_dist):
            mouse.press(Button.right)
            mouse.release(Button.right)  # Clic derecho
            cv2.putText(frame, "Click derecho", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif is_double_click(landmark_list, thumb_index_dist):
            pyautogui.doubleClick()  # Doble clic
            cv2.putText(frame, "Doble Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        elif is_screenshot(landmark_list, thumb_index_dist):
            im1 = pyautogui.screenshot()  # Toma una captura de pantalla
            label = random.randint(1, 1000)
            im1.save(f'screenshots/mi_captura_{label}.png')  # Guarda la captura
            cv2.putText(frame, "Captura de pantalla tomada", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

# Función principal del programa
def main():
    draw = mp.solutions.drawing_utils  # Utilidad para dibujar las conexiones de las manos
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Accedemos a la cámara

    # Verificamos si la cámara está disponible
    if not cap.isOpened():
        print("Error: No se pudo acceder a la cámara.")
    else:
        print("Cámara accesible.")
        
    try:
        while cap.isOpened():
            ret, frame = cap.read()  # Leemos el cuadro de video

            if not ret:
                print("Error al capturar el cuadro")
                break

            frame = cv2.flip(frame, 1)  # Invertimos la imagen horizontalmente
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertimos a RGB para MediaPipe
            processed = hands.process(frameRGB)  # Procesamos el cuadro con MediaPipe

            # Lista para almacenar los puntos de referencia de la mano
            landmark_list = []
            if processed.multi_hand_landmarks:
                hand_landmarks = processed.multi_hand_landmarks[0]  # Solo detectamos una mano
                draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)  # Dibujamos las conexiones de la mano
                for lm in hand_landmarks.landmark:
                    landmark_list.append((lm.x, lm.y))  # Almacenamos las coordenadas normalizadas

            # Detectamos gestos en función de los puntos detectados
            detect_gesture(frame, landmark_list, processed)

            # Mostramos el cuadro con las marcas dibujadas
            cv2.imshow('Deteccion de gestos', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break  # Salimos si se presiona 'q'

    finally:
        cap.release()  # Liberamos la cámara
        cv2.destroyAllWindows()  # Cerramos las ventanas de OpenCV

# Ejecutamos la función principal si este archivo es ejecutado directamente
if __name__ == '__main__':
    main()
