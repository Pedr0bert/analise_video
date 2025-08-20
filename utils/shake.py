import numpy as np
import cv2

def verificar_tremor(video_path):
    cap = cv2.VideoCapture(video_path)
    tremores = []

    # Pegamos o primeiro frame
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

    # Detecta cantos para acompanhar
    p0 = cv2.goodFeaturesToTrack(old_gray, maxCorners=100, qualityLevel=0.3, minDistance=7)

    lk_params = dict(winSize=(15,15), maxLevel=2,
                     criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calcula fluxo óptico
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

        if p1 is not None and p0 is not None:
            movement = np.mean(np.linalg.norm(p1 - p0, axis=1))
            tremores.append(movement)

        old_gray = frame_gray.copy()
        p0 = p1

    cap.release()
    media_tremor = np.mean(tremores)
    return media_tremor
