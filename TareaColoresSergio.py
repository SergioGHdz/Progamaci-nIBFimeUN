import cv2
import numpy as np

img1=cv2.imread('celeste.jpg')
img2=cv2.imread('cafe.jpg')
img3=cv2.imread('rojo.jpg')
hsv1=cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
hsv2=cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
hsv3=cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)

cafe_bajo = np.array([0,50,30])
cafe_alto = np.array([50,255,255])
celeste_bajo = np.array([10,0,100])
celeste_alto = np.array([255,220,255])
rojo_bajo = np.array([0,120,40])
rojo_alto = np.array([180,255,255])

mask1=cv2.inRange(hsv1,cafe_bajo,cafe_alto)
mask2=cv2.inRange(hsv2,celeste_bajo,celeste_alto)
mask3=cv2.inRange(hsv3,rojo_bajo,rojo_alto)


cv2.imshow('foto original',img1)
cv2.imshow('foto cafe extraido',mask1)
cv2.imshow('foto original2',img2)
cv2.imshow('foto celeste extraido.',mask2)
cv2.imshow('foto original3',img3)
cv2.imshow('foto rojo extraido.',mask3)

cv2.destroyALLWindows()
