import cv2
import numpy as np

def calcular_luminosidade(video_path):
    cap = cv2.VideoCapture(video_path)
    luminosidades = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        media = np.mean(gray)
        luminosidades.append(media)

    cap.release()
    mediana_luminosidade = np.median(luminosidades)
    media_luminosidade = np.mean(luminosidades)
    #f"mediana da luminosidade: {mediana_luminosidade:.2f}, media da luminosidade: {media_luminosidade:.2f}"
    return mediana_luminosidade, media_luminosidade

#luminosidade = calcular_luminosidade("data/jogo.mp4")
#print(f"{luminosidade}")
