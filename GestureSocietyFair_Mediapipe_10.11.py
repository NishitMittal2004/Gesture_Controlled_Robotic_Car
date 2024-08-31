import cv2
import mediapipe as mp
import time
import math
import serial

class handDetector():
    def _init_(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append((id, cx, cy))
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)

        return lmlist

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(10, 450)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

ser = serial.Serial('COM9', 9600)  # According to HC05 bluetooth module 'Outgoing'

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[9][1], lmList[9][2]
        length = math.hypot(x2 - x1, y2 - y1)
        if length > 50:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        print(fingers)
        totalFingers = fingers.count(1)

        if fingers == [1, 0, 0, 0, 0]:
            cv2.rectangle(img, (20, 25), (230, 120), (156, 83, 0), cv2.FILLED)
            cv2.putText(img, "Left", (65, 90), cv2.FONT_HERSHEY_DUPLEX, 2, (127, 164, 238), 5)
            ser.write(b'L')  # Send 'L' to Arduino for 'Left' gesture
            ser.flush()

            # ser.readline()
            # time.sleep(0.02)

        elif fingers == [0, 0, 0, 0, 1]:
            cv2.rectangle(img, (20, 25), (230, 120), (156, 83, 0), cv2.FILLED)
            cv2.putText(img, "Right", (45, 90), cv2.FONT_HERSHEY_DUPLEX, 2, (127, 164, 238), 5)
            ser.write(b'R')  # Send 'R' to Arduino for 'Right' gesture
            ser.flush()

            # ser.readline()
            # time.sleep(0.02)

        elif fingers == [0, 1, 0, 0, 0]:
            cv2.rectangle(img, (20, 25), (320, 120), (156, 83, 0), cv2.FILLED)
            cv2.putText(img, "Forward", (40, 90), cv2.FONT_HERSHEY_DUPLEX, 2, (127, 164, 238), 5)
            ser.write(b'F')  # Send 'L' to Arduino for 'Forward' gesture
            ser.flush()

            # ser.readline()
            # time.sleep(0.02)

        elif fingers == [1, 1, 1, 1, 1]:
            cv2.rectangle(img, (20, 25), (350, 120), (156, 83, 0), cv2.FILLED)
            cv2.putText(img, "Backward", (30, 90), cv2.FONT_HERSHEY_DUPLEX, 2, (127, 164, 238), 5)
            ser.write(b'B')  # Send 'L' to Arduino for 'Backward' gesture
            ser.flush()

            # ser.readline()
            # time.sleep(0.02)

        elif fingers == [0, 0, 0, 0, 0]:
            cv2.rectangle(img, (20, 25), (180, 120), (156, 83, 0), cv2.FILLED)
            cv2.putText(img, "Stop", (30, 90), cv2.FONT_HERSHEY_DUPLEX, 2, (127, 164, 238), 5)
            ser.write(b'S')  # Send 'S' to Arduino for 'Stop' gesture
            ser.flush()

            # ser.readline()
            # time.sleep(0.02)

    else:
        fingers = [0, 0, 0, 0, 0]
        print(fingers)
        ser.write(b'S')  # Send 'S' to Arduino for 'Stop' gesture
        ser.flush()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.rectangle(img, (430, 10), (633, 60), (255, 255, 255), cv2.FILLED)
    cv2.putText(img, f'FPS: {int(fps)}', (440, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 100), 3)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break