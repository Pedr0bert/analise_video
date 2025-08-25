import os
import csv
import time
from utils.luminosity import calcular_luminosidade
from utils.resolution import verify_resolution
from utils.shake import verificar_tremor
from utils.quality import video_quality, medir_desfoque


if __name__ == "__main__":
    data_folder = "data"
    results_file = "results/analise_video.csv"

    # garante que a pasta results existe
    os.makedirs("results", exist_ok=True)

    # abre o CSV em modo de escrita (cria do zero a cada execução)
    with open(results_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # cabeçalho
        writer.writerow(["FileName", "Width", "Height", "MediaLuminosidade", 
                         "MedianaLuminosidade","MediaBlur","MedianaBlur", 
                         "Tremor", "TempoSegundos"])

        # percorre todos os vídeos da pasta data/
        for filename in os.listdir(data_folder):
            try:                
                if filename.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
                    video_path = os.path.join(data_folder, filename)
                    print(f"Analisando: {filename}")
                    
                    start_time = time.time()  # <-- início da contagem

                    # Resolução
                    print("  Verificando resolução...")
                    width, height = verify_resolution(video_path)

                    # Luminosidade
                    print("  Calculando luminosidade...")
                    mediana_luminosidade, media_luminosidade = calcular_luminosidade(video_path)

                    # Tremor
                    print("  Verificando tremor...")
                    tremor = verificar_tremor(video_path)
                    
                    # Qualidade (desfoque)
                    print("  Medindo desfoque...")
                    media_blur, mediana_blur = video_quality(video_path)
                    
                    end_time = time.time()  # <-- fim da contagem
                    tempo_exec = end_time - start_time

                    # Escreve no CSV
                    writer.writerow([filename, width, height, float(f"{media_luminosidade:.2f}"), 
                                     float(f"{mediana_luminosidade:.2f}"), 
                                     float(f"{media_blur:.2f}"), float(f"{mediana_blur:.2f}"), float(f"{tremor:.2f}"), 
                                     float(f"{tempo_exec:.2f}")])
            
            except Exception as e:
                print(f"Erro ao processar {filename}: {e}")
                
    print(f"\nAnálise concluída! Resultados salvos em {results_file}")