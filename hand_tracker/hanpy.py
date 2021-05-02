import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(False, 4)
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    tik = time.time()
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_lm in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_lm, mp_hands.HAND_CONNECTIONS)

    tok = time.time()
    fps = 1 / (tok - tik)
    
    cv2.putText(img, f'FPS: {int(fps)}', (10,40), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255),3)


    cv2.imshow('Image', img)
    cv2.waitKey(1)