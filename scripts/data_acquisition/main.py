import os
import pandas as pd

# Establecer la ruta al archivo kaggle.json
kaggle_path = os.path.join(os.getcwd(), '.kaggle')
os.environ["KAGGLE_CONFIG_DIR"] = kaggle_path

# Verificar si el archivo kaggle.json existe
if not os.path.exists(os.path.join(kaggle_path, 'kaggle.json')):
    raise FileNotFoundError("El archivo kaggle.json no se encuentra en la carpeta .kaggle.")

# Descargar y descomprimir el dataset
dataset_path = './flight_delays'
os.makedirs(dataset_path, exist_ok=True)
os.system(f"kaggle datasets download -d robikscube/flight-delay-dataset-20182022 --unzip -p {dataset_path}")

# Leer el archivo principal del dataset
data_file = os.path.join(dataset_path, 'Combined_Flights_2018-2022.csv')
if os.path.exists(data_file):
    print("Leyendo el archivo CSV...")
    data = pd.read_csv(data_file, nrows=1000)  # Leer las primeras 1000 filas como ejemplo
    print(data.head())
else:
    print(f"No se encontró el archivo: {data_file}")

