import os
import pandas as pd

# Establecer la ruta al archivo kaggle.json
kaggle_path = os.path.join(os.getcwd(), 'scripts/data_acquisition/.kaggle')
os.environ["KAGGLE_CONFIG_DIR"] = kaggle_path

# Verificar si el archivo kaggle.json existe
if not os.path.exists(os.path.join(kaggle_path, 'kaggle.json')):
    raise FileNotFoundError("El archivo kaggle.json no se encuentra en la carpeta .kaggle.")

# Descargar y descomprimir el dataset
dataset_path = './flight_delays'
os.makedirs(dataset_path, exist_ok=True)
os.system(f"kaggle datasets download -d robikscube/flight-delay-dataset-20182022 --unzip -p {dataset_path}")

# Función para leer las primeras 5 filas de los primeros 5 archivos CSV
def show_first_rows_of_files(base_path, subfolder=None, num_files=5, num_rows=5):
    folder_path = os.path.join(base_path, subfolder) if subfolder else base_path
    csv_files = []

    # Buscar todos los archivos CSV en la carpeta
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                csv_files.append(os.path.join(root, file))

    # Leer y mostrar las primeras filas de los primeros archivos
    for i, file in enumerate(csv_files[:num_files]):
        print(f"Archivo {i + 1}: {file}")
        try:
            data = pd.read_csv(file, nrows=num_rows)  # Leer solo las primeras filas
            print(data.head())  # Mostrar las primeras filas
        except Exception as e:
            print(f"Error al leer el archivo {file}: {e}")
        print("\n" + "=" * 50 + "\n")

# Mostrar las primeras filas de los primeros 5 archivos en la subcarpeta "raw"
try:
    print("Leyendo los primeros 5 archivos en la carpeta raw...")
    show_first_rows_of_files(dataset_path, subfolder="raw", num_files=5, num_rows=5)
except Exception as e:
    print(f"Error: {e}")
