## OpenCV-Plutella-xylostellaL.-Detection
this program was used in PKM-PI 2020  
it can detect Plutella xylostellaL Larva using camera  
trained .xml data is trained using cascade trainer GUI  
the accuracy not good enough because lack of dataset for training
>How to use
````
- install opencv-python library
- place trained .xml and python program in the same directories
- double click to run or u can use terminal instead
````
>Change camera input source
````
video = cv2.VideoCapture(0) #usb camera
video = cv2.VideoCapture(rtsp://<ip>:<port>/video/live) #ip camera
````
>Change trained .xml
````
#u can use ur own trained .xml file
#just replace path/filename inside "()"
testcascade = cv2.CascadeClassifier("Resource/ulathehe.xml") 
````
