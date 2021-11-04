import cv2 as cv
import time
import numpy as np
import math
import handTrackingModule as htm
import screen_brightness_control as sbc


cap = cv.VideoCapture(0)

# Setting the dimension of the camera
wCam, hCam = 640, 480
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0


# Calling the hand detector
detector = htm.handDetector(min_detection_confidence=0.7)

while True:
    is_True, frame = cap.read()
    frame = detector.findHands(frame)

    # Finding the position of all landmark points
    lmlist = detector.findPositions(frame, draw=False)


    if len(lmlist) != 0:
        # print(lmlist[4], lmlist[8])
        # For the 4th landmark position
        x1,y1 = lmlist[4][1], lmlist[4][2]
        # For the 8th landmark position
        x2, y2 = lmlist[8][1], lmlist[8][2]
        # Center between both the positions
        cx, cy = (x1+x2)//2, (y1+y2)//2
        # Drawing circle at position 4
        cv.circle(frame, (x1,y1), 7, (255,12,136), cv.FILLED)
        # Drawing circle at position 8
        cv.circle(frame, (x2,y2), 7, (255,12,136), cv.FILLED)
        # Drawing line between both the positions
        cv.line(frame, (x1,y1), (x2,y2), (255,0,255), 3)
        # Drawing midpoint between both the positions
        cv.circle(frame, (cx,cy), 7, (255,12,136), cv.FILLED)
        # Calculating lengrh between 4 and 8 positions
        length = math.hypot(x2-x1, y2-y1)
        # print(length)
        # Interpreting the length maximum and minimim range to 0% to 150% of volume
        brightness = np.interp(length, (15,200), (0,100))
        # Calling the function to execute the command for volume change
        sbc.set_brightness(brightness, display=0)
        print(brightness)
        # If the length is less than or equal to 15 mid point circle colour changes to green
        if length <= 15:
            cv.circle(frame, (cx,cy), 7, (0,255,0), cv.FILLED)
        # If the length is greater than or equal to 200 mid point circle colour changes to red
        if length >= 200:
            cv.circle(frame, (cx,cy), 7, (0,0,255), cv.FILLED)

    # Code for calculating frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(frame, f'FPS: {int(fps)}', (40,50), cv.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)

    cv.imshow('Video', frame)
    cv.waitKey(1)