import cv2
print ("hehe")

testcascade = cv2.CascadeClassifier("Resource/ulathehe.xml")
video = cv2.VideoCapture(0)

while True :
    ret, img = video.read()
    testgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    test = testcascade.detectMultiScale(testgray,1.5,6)
    for(x,y,w,h) in test :
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
        cv2.putText(img,"Ulat",(x,y-5),cv2.FONT_ITALIC,1,(255,0,0),2)
    cv2.imshow('Hasil',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


