import cv2
import mediapipe as mp
import time

TARGET_RES = 1080

cap = cv2.VideoCapture(0)

mp_face = mp.solutions.face_mesh
face = mp_face.FaceMesh(
    max_num_faces=2, 
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils
draw_spec = mp_draw.DrawingSpec(thickness=2, circle_radius=1)

while True:
    success, img = cap.read()
    y, x, _ = img.shape
    ratio = x/y
    scaling = TARGET_RES/y
    img = cv2.resize(img, None, None, fx=scaling, fy=scaling)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # print(f'x = {x} -> {x*scaling} | y = {y} -> {scaling * y}')
    tik = time.time()
    results = face.process(img_rgb)

    if results.multi_face_landmarks:
        for face_lms in results.multi_face_landmarks:
            mp_draw.draw_landmarks(img, face_lms, mp_face.FACE_CONNECTIONS, draw_spec, draw_spec)

    tok = time.time()
    fps = 1 / (tok - tik)
    
    cv2.putText(img, f'FPS: {int(fps)}', (10,40), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255),3)

    cv2.imshow('Image', img)
    cv2.waitKey(1)