import cv2
import time
import math
import HandTrackingModule as htm
import serial

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(10,450)
cap.set(3,wCam)
cap.set(4,hCam)

pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

ser = serial.Serial('COM12', 9600)  # According to HC05 bluetooth module 'Outgoing'

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[9][1], lmList[9][2]
        length = math.hypot(x2 - x1, y2 - y1)
        # print(int(length))
        if length > 50:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other 4 Fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        print(fingers)
        totalFingers = fingers.count(1)
        # print(totalFingers)


        if fingers == [1,0,0,0,0]:
            cv2.rectangle(img, (20,25), (230,120),(156,83,0), cv2.FILLED)
            cv2.putText(img, "Left", (65,90), cv2.FONT_HERSHEY_DUPLEX,
                        2,(127,164,238), 5)
            ser.write(b'L')  # Send 'L' to Arduino for 'Left' gesture
            ser.flush()

            # ser.readline()
            # time.sleep(0.02)
        elif fingers == [0,0,0,0,1]:
            cv2.rectangle(img, (20, 25), (230, 120), (156,83,0), cv2.FILLED)
            cv2.putText(img, "Right", (45, 90), cv2.FONT_HERSHEY_DUPLEX,
                        2, (127,164,238), 5)
            ser.write(b'R')  # Send 'R' to Arduino for 'Right' gesture
            ser.flush()

            # ser.readline()
            # time.sleep(0.02)
        elif fingers == [0,1,0,0,0]:
            cv2.rectangle(img, (20, 25), (320, 120), (156,83,0), cv2.FILLED)
            cv2.putText(img, "Forward", (40, 90), cv2.FONT_HERSHEY_DUPLEX,
                        2, (127,164,238), 5)
            ser.write(b'F')  # Send 'L' to Arduino for 'Forward' gesture
            ser.flush()

            # ser.readline()
            # time.sleep(0.02)
        elif fingers == [1,1,1,1,1]:
            cv2.rectangle(img, (20, 25), (350, 120), (156,83,0), cv2.FILLED)
            cv2.putText(img, "Backward", (30, 90), cv2.FONT_HERSHEY_DUPLEX,
                        2, (127,164,238), 5)
            ser.write(b'B')  # Send 'L' to Arduino for 'Backward' gesture
            ser.flush()

            # ser.readline()
            # time.sleep(0.02)
        elif fingers == [0, 0, 0, 0, 0]:
            cv2.rectangle(img, (20, 25), (180, 120), (156, 83, 0), cv2.FILLED)
            cv2.putText(img, "Stop", (30, 90), cv2.FONT_HERSHEY_DUPLEX,
                        2, (127, 164, 238), 5)
            ser.write(b'S')  # Send 'S' to Arduino for 'Stop' gesture
            ser.flush()

            # ser.readline()
            # time.sleep(0.02)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.rectangle(img, (430,10), (633,60), (255,255,255), cv2.FILLED)
    cv2.putText(img, f'FPS: {int(fps)}', (440,50), cv2.FONT_HERSHEY_PLAIN,
                3, (255,0,100), 3)


    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        ser.close()
        break