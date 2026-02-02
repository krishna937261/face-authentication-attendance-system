import cv2
import face_recogniton
import numpy as np
from utils import load_encodings, mark_attendance
from spoof_detection import is_blinking 
data = load_encodings()
video = cv2.VideoCapture(0)
print("Press 'q' to exit")
while True:
    ret, frame = video.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recogniton.face_location(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)

    for encoding, box in zip(encodings, boxes):
        matches = face_recognition.compare_faces(
            data["encodings"], encoding, tolerance=0.6
        )

        name = "Unknown"

        if True in matches and is_blinking(rgb):
            idx = matches.index(True)
            name = data["names"][idx]
            mark_attendance(name)

        top, right, bottom, left = box
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()