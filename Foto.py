import cv2
camara = cv2.VideoCapture(0)
leido,img=camara.read()


if leido == True:
    cv2.imwrite('SergioGHdz.jpg',img)
    img = cv2.imread('SergioGHdz.jpg', cv2.IMREAD_COLOR)
    cv2.imshow('SergioGHdz', img)

    cv2.waitKey(30)
    print ("Se tomo con exito la foto")
    
    x= input ("\n¿Desea tomar otra fotografia? ")
    while x==('si'):
        cv2.imwrite('SergioGHdz.jpg',img)
        img = cv2.imread('SergioGHdz.jpg', cv2.IMREAD_COLOR)
        cv2.imshow('SergioGHdz', img)
        cv2.waitKey(30)
        print ("Se tomo con exito la foto")
        x= input ("\n¿Desea tomar otra fotografia? ")
        continue
        
    else :
        print ("Fin")

else:
    print ("Error Camara no existe o esta apagada o no esta configurada")

camara.release()
