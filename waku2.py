import cv2
import os
import waku

def Createwaku(Jpg_pass):
    src = cv2.imread(Jpg_pass)
    face_cascade_path = './haarcascade_frontalface_default.xml'

    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    assert os.path.isfile(face_cascade_path), 'haarcascade_frontalface_default.xml がない'
    faces = face_cascade.detectMultiScale(src_gray)

    for x, y, w, h in faces:
        cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = src[y: y + h, x: x + w]
        face_gray = src_gray[y: y + h, x: x + w]
        
    cv2.imwrite('img/a/opencv_face_detect_rectangle.jpg', src)