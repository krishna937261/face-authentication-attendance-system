from scipy.spatial import distance
import face_recognition

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1],eye[5])
    B = distance.euclidean(eye[2],eye[4])
    C = distance.euclidean(eye[0],eye[3])
    return (A+B)/(2.0*C)

def is_blinking(frame):
    landmarks = face_recognition.face_landmarks(frame)
    if not landmarks:
        return False
    left_eye=landmarks[0]['left_eye']
    right_eye=landmarks[0]['right_eye']
    ear = (eye_aspect_ratio(left_eye)+eye_aspect_ratio(right_eye))/2.0
    return ear < 0.20