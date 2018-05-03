import numpy as np
import cv2

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create();
rec.read("recognizer/trainningData.yml")
id=0
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cam = cv2.VideoCapture(0)
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 255, 255)

while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        id, conf = rec.predict(gray[y:y + h, x:x + w])
        if(id==1):
            id="SRIJA"
        if (id == 3):
            id = "mani"
        if (id == 4):
            id = "Snha"
        if (id == 5):
            id = "Likhi"


        cv2.putText(img, str(id), (x, y + h), fontface, fontscale, fontcolor)
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()