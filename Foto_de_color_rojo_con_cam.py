import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, camara = cap.read()
    hsv = cv2.cvtColor(camara, cv2.COLOR_BGR2HSV)
    
    rojo_claro = np.array([236, 100,93])
    rojo_oscuro = np.array([0,100,48])
 
    
    mask = cv2.inRange(hsv, rojo_claro, rojo_oscuro)
    col = cv2.bitwise_and(camara,camara, mask= mask)

    cv2.imshow('Camara',camara)
    cv2.imshow('Recibido',mask)
    cv2.imshow('Color',col)
    
    k = cv2.waitKey(2) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
