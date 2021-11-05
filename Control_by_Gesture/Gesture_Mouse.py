import cv2 as cv
import time
import numpy as np
import math
import handTrackingModule as htm
import wx
import pyautogui


cap = cv.VideoCapture(0)

# Setting the dimension of the camera
wCam, hCam = 640, 480
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0


app = wx.App(False)
screen_width, screen_height = wx.GetDisplaySize()


# Calling the hand detector
detector = htm.handDetector(min_detection_confidence=0.7)

while True:
    is_True, frame = cap.read()
    frame = cv.flip(frame, 1)
    frame = detector.findHands(frame)
    

    # Finding the position of all landmark points
    lmlist = detector.findPositions(frame, draw=False)


    if len(lmlist) != 0:
        # print(lmlist[4], lmlist[8])
        # For the 4th landmark position
        x1,y1 = lmlist[8][1], lmlist[8][2]
        # For the 8th landmark position
        x2,y2 = lmlist[12][1], lmlist[12][2]
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

        # Calculating mouse position        
        mousePos_x = np.interp(x1, (0,wCam), (0,screen_width))
        mousePos_y = np.interp(y1, (0,hCam), (0,screen_height))
        pyautogui.FAILSAFE = False
        # Moving mouse to the desired location
        pyautogui.moveTo(mousePos_x, mousePos_y, duration = 1)

        # The mouse button will be hold if the length is less than or equal to 20
        length = math.hypot(x2-x1, y2-y1)
        if length <= 20:
            pyautogui.mouseDown(button='left')
        else:
            pyautogui.mouseUp(button='left')
       
        cv.putText(frame, f'X: {int(mousePos_x)}', (40,80), cv.FONT_HERSHEY_PLAIN, 1, (0,255,0), 2)
        cv.putText(frame, f'Y: {int(mousePos_y)}', (40,110), cv.FONT_HERSHEY_PLAIN, 1, (0,255,0), 2)
        # If the length is less than or equal to 20 mid point circle colour changes to green
        if length <= 20:
            cv.circle(frame, (cx,cy), 7, (0,255,0), cv.FILLED)


    
    # Code for calculating frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(frame, f'FPS: {int(fps)}', (40,50), cv.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)

    
    cv.imshow('Video', frame)
    key = cv.waitKey(5)

    if key==ord('q'):
        break