import cv2
import numpy as np

def medir_desfoque(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    var_lap = lap.var()  # variância
    return var_lap

def video_quality(video_path):
    cap = cv2.VideoCapture(video_path)
    blur_scores = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        blur_scores.append(medir_desfoque(frame))

    cap.release()

    if blur_scores:
        media_blur = np.mean(blur_scores)
        mediana_blur = np.median(blur_scores)
    else:
        media_blur = mediana_blur = 0

    return media_blur, mediana_blur