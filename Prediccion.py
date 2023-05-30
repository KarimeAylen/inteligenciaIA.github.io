import cv2
import mediapipe as mp
import os
import numpy as np
from keras_preprocessing.image import load_img, img_to_array
from keras.models import load_model

modelo = __path__=r'C:\Users\karim\Desktop\IAPeteVScode\modelo.h5'
peso =__path__=r'C:\Users\karim\Desktop\IAPeteVScode\pesos.h5'
cnn = load_model(modelo)  #Cargamos el modelo
cnn.load_weights(peso)  #Cargamos los pesos

direccion =__path__=r'C:/Users/karim/Desktop/IAPeteVScode/Validacion'
dire_img = os.listdir(direccion)
print("Nombres: ", dire_img)

#Leemos la camara
cap = cv2.VideoCapture(0)

#----------------------------Creamos un obejto que va almacenar  la deteccion y el seguimiento de las manos------------
clase_manos  =  mp.solutions.hands
manos = clase_manos.Hands()

#----------------------------------Metodo para dibujar las manos---------------------------
dibujo = mp.solutions.drawing_utils #Con este metodo dibujamos 21 puntos criticos de la mano


while (1):
    ret,frame = cap.read()
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    copia = frame.copy()
    resultado = manos.process(color)
    posiciones = []  # En esta lista vamos a almcenar las coordenadas de los puntos
    #print(resultado.multi_hand_landmarks) #Si queremos ver si existe la deteccion

    if resultado.multi_hand_landmarks: #Si hay algo en los resultados entramos al if
        for mano in resultado.multi_hand_landmarks:  #Buscamos la mano dentro de la lista de manos que nos da el descriptor
            for id, lm in enumerate(mano.landmark):  #Vamos a obtener la informacion de cada mano encontrada por el ID
                alto, ancho, c = frame.shape  #Extraemos el ancho y el alto de los fotpgramas para multiplicarlos por la proporcion
                corx, cory = int(lm.x*ancho), int(lm.y*alto) #Extraemos la ubicacion de cada punto que pertence a la mano en coordenadas
                posiciones.append([id,corx,cory])
                dibujo.draw_landmarks(frame, mano, clase_manos.HAND_CONNECTIONS)
            if len(posiciones) != 0:
                pto_i1 = posiciones[3] 
                pto_i2 = posiciones[17]
                pto_i3 = posiciones[10]
                pto_i4 = posiciones[0]
                pto_i5 = posiciones[9]
                x1,y1 = (pto_i5[1]-100),(pto_i5[2]-100) #Obtenemos el punto incial y las longitudes
                ancho, alto = (x1+200),(y1+200)
                x2,y2 = x1 + ancho, y1 + alto
                dedos_reg = copia[y1:y2, x1:x2]
                dedos_reg = cv2.resize(dedos_reg, (200, 200), interpolation=cv2.INTER_CUBIC)  # Redimensionamos las fotos
                x = img_to_array(dedos_reg)  # Convertimos la imagen a una matriz
                x = np.expand_dims(x, axis=0)  # Agregamos nuevo eje
                vector = cnn.predict(x)  # Va a ser un arreglo de 2 dimensiones, donde va a poner 1 en la clase que crea correcta
                resultado = vector[0]  # [1,0] | [0, 1]
                respuesta = np.argmax(resultado)  # Nos entrega el indice del valor mas alto 0 | 1
                if respuesta == 0: #DEPENDIENDO DE LAS CLASES por lo tanto son 20
                    print(vector,resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    cv2.putText(frame, '{}'.format(dire_img[0]), (x1, y1 - 5), 1, 1.3, (0, 255, 0), 1, cv2.LINE_AA)
                elif respuesta == 1:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[1]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 2:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[2]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 3:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[3]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 4:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[4]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 5:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[5]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 6:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[6]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 7:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[7]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 8:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[8]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 9:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[9]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 10:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[10]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 11:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[11]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 12:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[12]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 13:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[13]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 14:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[14]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 15:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[15]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 16:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[16]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 17:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[17]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 18:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[18]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                elif respuesta == 19:
                    print(vector, resultado)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, '{}'.format(dire_img[19]), (x1, y1 - 5), 1, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
                else:
                    cv2.putText(frame,'Letra desconocida',(x1, y1-20), 1, 1.3,(0,255,255),1, cv2.LINE_AA)

    cv2.imshow("Video",frame)
    k = cv2.waitKey(1)
    if k == 20:
        break
cap.release()
cv2.destroyAllWindows()











