import cv2;

facecasd = cv2.CascadeClassifier("casd/haarcascade_frontalface_default.xml");

cap = cv2.VideoCapture(0);
cap.set(3,600)
cap.set(4,400)
cap.set(10,100)
while True:
    success,img =cap.read();
    imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces =facecasd.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(10,222,10),2)
        cv2.imshow("FaceDetector",img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break