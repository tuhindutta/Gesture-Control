import cv2 as cv
import mediapipe as mp
import time


class handDetector():
    def __init__(self, static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence


        # Function within mediapipe library to detect hands
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.static_image_mode, self.max_num_hands, self.min_detection_confidence, self.min_tracking_confidence)

        # Function to draw connections on hands connecting landmarks
        self.mpDraw = mp.solutions.drawing_utils

        

    def findHands(self, frame, draw=True):   
        img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(img)

        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, handlms, self.mpHands.HAND_CONNECTIONS)
        return frame




    def findPositions(self, frame, handNo=0, draw=True):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id,landmark in enumerate(myHand.landmark):
                h, w, c = frame.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv.circle(frame, (cx,cy), 5, (0,178,240), cv.FILLED)

        return lmList

        




def main():
    
    pTime = 0
    cTime = 0
    cap = cv.VideoCapture(0)

    detector = handDetector()

    while True:
        isTrue, frame = cap.read() 
        frame = detector.findHands(frame) 
        lmList = detector.findPositions(frame)

        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        # FPS is printed on video
        cv.putText(frame, 'Frame Rate ='+str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (175,200,250), 3)

        cv.imshow('Video', frame)

        # cv.waitKey(1)
        if cv.waitKey(1) == 27:
            break

if __name__ == "__main__":
    main()
# cv.destroyAllWindows()
# cap.release()