import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    amarillo_bajo = np.array([0,20,180])
    amarillo_oscuro = np.array([100,255,255])
    
    mask = cv2.inRange(hsv, amarillo_bajo, amarillo_oscuro)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('Camara',frame)
    cv2.imshow('Mascara',mask)
    cv2.imshow('Color',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
