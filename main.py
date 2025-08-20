from utils.luminosity import calcular_luminosidade
from utils.resolution import verify_resolution
from utils.shake import verificar_tremor
import csv



if __name__ == "__main__":
    video_path = "data/jogo.mp4"
    
    # Verifica a resolução do vídeo
    width, height = verify_resolution(video_path)
    #print(f"Resolução: {width}x{height}")

    # Calcula a luminosidade do vídeo
    mediana_luminosidade, media_luminosidade = calcular_luminosidade(video_path)
    #print(f"Mediana da luminosidade: {mediana_luminosidade:.2f}, Média da luminosidade: {media_luminosidade:.2f}")

    # Verifica o tremor do vídeo
    tremor = verificar_tremor(video_path)
    #print(f"Nível de tremor (média de movimento): {tremor:.2f}")
    
    #with open("results/analise_video.csv", "w", newline="", encoding="utf-8") as f:
    #    writer = csv.writer(f)
    #
    ## cabeçalho
    #    writer.writerow(["Width","Height", "MediaLuminosidade", "MedianaLuminosidade", "Tremor"])
    
    with open("results/analise_video.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        writer.writerow([width, height, media_luminosidade, mediana_luminosidade, tremor])

    
    