import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy


########################

wCam, hCam = 640, 480

########################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

while True:
    # 1. Buscar las marcas de la mano
    success, img = cap.read()

    # 2. Encontrar la punta de los dedos indice y medio.
    # 3. Verificar que dedo está levantado
    # 4. Solo el dedo incice mueve el raton
    # 5. Convertir las coordenadas
    # 6. Suavizar los valores para que el raton no de saltos
    # 7. Mover el raton
    # 8. El dedo indice y el del medio estan levantados: (Clicking mode)
    # 9. Buscar la distancia entre los dedos
    # 10. Si la distancia es corta entre los dedos hace click

    # 11. Frame rate (Este codigo imprime los FPS a los que va la camara)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    # 12. Display

    cv2.imshow('img', img)
    cv2.waitKey(1)