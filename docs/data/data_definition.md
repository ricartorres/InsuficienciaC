![Descripción de la imagen](images/Falla-cardiaca.jpg)
# Definición de los datos

## Origen de los datos

- Fuente:
  Los datos utilizados provienen del dataset público disponible en Kaggle: Heart Failure Clinical Data.
- Método de obtención:
  Se utiliza la API de Kaggle para descargar el archivo.
  El acceso se realiza configurando credenciales mediante un archivo kaggle.json.

## Especificación de los scripts para la carga de datos

- El script se encuentra en scripts/data_acquisition/Carga_Datos_Automatica_Insuficiencia_Cardiaca
  Scripts utilizados:
  Se emplearon scripts en Python para la descarga, descompresión, y lectura de los datos.
  Las bibliotecas utilizadas incluyen os y pandas para gestionar el sistema de archivos y estructurar los datos en un DataFrame.
  El dataset fue guardado en formato CSV para facilitar su integración con herramientas de análisis y modelado.

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

- Ubicación de los archivos de origen
  - Descargados desde Kaggle en el archivo heart_failure_clinical_data.zip.
  - Archivo descomprimido: heart_failure_clinical_records_dataset.csv.
- Estructura del archivo de origen:
  - El archivo CSV contiene las siguientes columnas:
    - age: Edad del paciente.
    - creatinine_phosphokinase (nivel de enzima CPK en sangre)
    - ejection_fraction (porcentaje de sangre que sale del corazón en cada contracción)
    - platelets (conteo de plaquetas en sangre)
    - serum_creatinine (nivel de creatinina en sangre)
    - serum_sodium (nivel de sodio en sangre)
    - time (período de seguimiento en días)
    - anaemia (0 = no, 1 = sí)
    - diabetes (0 = no, 1 = sí)
    - high_blood_pressure (0 = no, 1 = sí)
    - sex (0 = mujer, 1 = hombre)
    - smoking (0 = no, 1 = sí)
    - DEATH_EVENT (0 = sobrevivió, 1 = falleció) - Esta es la variable objetivo
      
- Procedimientos de transformación y limpieza:
  - Validación de valores nulos.
  - Conversión de tipos de datos donde sea necesario.
  - Normalización de valores categóricos.

### Base de datos de destino

- Especificar la base de datos de destino para los datos
    - Destino seleccionado: El almacenamiento remoto de los datos se realizó en Google Drive utilizando la herramienta de control de versiones DVC (Data Version Control).
    - Propósito del almacenamiento remoto: Garantizar que el dataset sea accesible de forma segura, rastreable y compartible entre colaboradores.
    - Ubicación del almacenamiento remoto: Se configuró una carpeta específica en Google Drive, identificada mediante un ID único, para almacenar los datos y su historial de versiones.

- Especificar la estructura de la base de datos de destino.
  - Estructura local:
    - Los datos se almacenan en una carpeta llamada data/ dentro de un repositorio de trabajo.
    - La carpeta incluye:
      - El archivo original del dataset en formato CSV (insuficiencia_cardiaca.csv).
      - Archivos de configuración y control de DVC para rastrear el dataset.
      - Un archivo .gitignore que asegura que el archivo original no sea rastreado directamente por Git.
  - Estructura en el almacenamiento remoto:
    - El archivo de datos y su historial de cambios se encuentran sincronizados en Google Drive.
    - Esto incluye tanto los datos originales como los archivos de rastreo generados por DVC.
        
- Describir los procedimientos de carga y transformación de los datos en la base de datos de destino
  - Inicialización del entorno local:
    - Se preparó un repositorio de trabajo para almacenar y gestionar los datos localmente.
    - El archivo de datos fue almacenado en la carpeta data/ y rastreado utilizando DVC.
  - Configuración del almacenamiento remoto:
    - Se definió Google Drive como la ubicación de respaldo remoto para los datos.
    - La configuración incluyó el enlace a una carpeta en Google Drive con permisos adecuados para su acceso.
  - Gestión de los datos:
    - Se estableció un sistema de versionamiento que rastrea cada cambio realizado en el dataset, asegurando reproducibilidad y control en los procesos de análisis.
    - Los cambios registrados en el repositorio de trabajo fueron respaldados automáticamente en el almacenamiento remoto.
  - Sincronización de datos:
    - Los datos del repositorio local fueron cargados en la carpeta remota de Google Drive para su almacenamiento y acceso a largo plazo.
    - Este proceso garantiza la disponibilidad del dataset y su historial de cambios para todos los colaboradores del proyecto.
