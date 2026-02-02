import cv2
import face_recognition
from utils import load_encodings, save_encodings
name = input ("Enter your name: ")
video = cv2.VideoCapture(0)
data = load_encodings()
count = 0
print("Look at the camera. Press 'q' to stop.")
while True:
    ret, frame = video.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)

    for encoding in encodings:
        data["names"].append(name)
        data["encodings"].append(encoding)
        count += 1

    cv2.putText(frame, f"Samples: {count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Register Face", frame)

    if cv2.waitKey(1) & 0xFF == ord("q") or count >= 20:
        break
video.release()
cv2.destroyAllWindows()
save_encodings(data)
print("Face registered successfully!")


