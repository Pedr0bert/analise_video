import os
import csv
from utils.luminosity import calcular_luminosidade
from utils.resolution import verify_resolution
from utils.shake import verificar_tremor


if __name__ == "__main__":
    data_folder = "data"
    results_file = "results/analise_video.csv"

    # garante que a pasta results existe
    os.makedirs("results", exist_ok=True)

    # abre o CSV em modo de escrita (cria do zero a cada execução)
    with open(results_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # cabeçalho
        writer.writerow(["FileName", "Width", "Height", "MediaLuminosidade", "MedianaLuminosidade", "Tremor"])

        # percorre todos os vídeos da pasta data/
        for filename in os.listdir(data_folder):
            try:                
                if filename.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
                    video_path = os.path.join(data_folder, filename)
                    print(f"Analisando: {filename}")

                    # Resolução
                    width, height = verify_resolution(video_path)

                    # Luminosidade
                    mediana_luminosidade, media_luminosidade = calcular_luminosidade(video_path)

                    # Tremor
                    tremor = verificar_tremor(video_path)

                    # Escreve no CSV
                    writer.writerow([filename, width, height, f"{media_luminosidade:.2f}", f"{mediana_luminosidade:.2f}", f"{tremor:.2f}"])
            
            except Exception as e:
                print(f"Erro ao processar {filename}: {e}")
                
    print(f"\nAnálise concluída! Resultados salvos em {results_file}")