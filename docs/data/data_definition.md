# Definición de los datos

## Origen de los datos

- Fuente:
  Los datos utilizados provienen del dataset público disponible en Kaggle: Heart Failure Clinical Data.
- Método de obtención:
  Se utiliza la API de Kaggle para descargar el archivo.
  El acceso se realiza configurando credenciales mediante un archivo kaggle.json.

## Especificación de los scripts para la carga de datos

- El script se encuentra en scripts/data_acquisition/Carga_Datos_Automatica_Insuficiencia_Cardiaca

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

- Ubicación de los archivos de origen
  - Descargados desde Kaggle en el archivo heart_failure_clinical_data.zip.
  - Archivo descomprimido: heart_failure_clinical_records_dataset.csv.
- Estructura del archivo de origen:
  - El archivo CSV contiene las siguientes columnas:
    - age: Edad del paciente.
- Procedimientos de transformación y limpieza:
  - Validación de valores nulos.
  - Conversión de tipos de datos donde sea necesario.
  - Normalización de valores categóricos.

### Base de datos de destino

- [ ] Especificar la base de datos de destino para los datos.
- [ ] Especificar la estructura de la base de datos de destino.
- [ ] Describir los procedimientos de carga y transformación de los datos en la base de datos de destino.
