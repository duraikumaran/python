import numpy as np
import cv2

cap = cv2.VideoCapture(0)
front_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
left_eye = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')

while True:
    ret, frame = cap.read()
    faces = front_face.detectMultiScale(frame, 1.3, 5)
    car = car_det.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
            imu = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = frame[y:y + h, x:x + w]
            roi_color = imu[y:y + h, x:x + w]
            rio_car = frame[y:y + h, x:x + w]
            eyes = left_eye.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('op', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()
