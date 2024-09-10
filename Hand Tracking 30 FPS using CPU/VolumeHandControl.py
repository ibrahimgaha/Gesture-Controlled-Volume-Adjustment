import cv2
import numpy as np
import time
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

##########################
wCam, hCam = 640, 480
##########################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
cTime = 0

detector = htm.HandDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

volumeRange = volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-20.0, None)

minVolume = volumeRange[0]
maxVolume= volumeRange[1]
vol = 0
volBar= 400
volPercentage = 0

while True:
    success, img = cap.read()
    img = detector.find_hands(img)
    lmList = detector.find_position(img, draw=False)

    # Check if lmList is not None and contains landmarks
    if lmList and len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2)//2, (y1 + y2)//2

        cv2.circle(img,(x1,y1),10,(255,0,0),cv2.FILLED)
        cv2.circle(img,(x2,y2),10,(255,0,0),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)
        cv2.circle(img,(cx,cy),10,(0,0,255),cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)

         #Hand range 50 -> 300
         #Volume Range -65 -> 0

        vol = np.interp(length,[50,300],[minVolume,maxVolume])
        volBar = np.interp(length,[50,300],[400,150])
        volPercentage = np.interp(length,[50,300],[0,100])

        volume.SetMasterVolumeLevel(vol, None)

        if(length < 50):
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img,(50,150),(85,400),(255, 0, 0),3)
    cv2.rectangle(img,(50,int(volBar)),(85,400),(255, 0, 0),cv2.FILLED)
    cv2.putText(img, f'{int(volPercentage)}%', (50,460),cv2.FONT_HERSHEY_PLAIN,2,(255, 0, 0),2)



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 3)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
