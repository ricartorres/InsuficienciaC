```markdown
# Flight Delay Analysis

Este repositorio contiene un conjunto de scripts para analizar los retrasos de vuelos utilizando datos descargados de Kaggle. La estructura principal se organiza para facilitar la adquisición y el procesamiento de datos.

## **Estructura del Proyecto**
scripts/
├── data_acquisition/
│   ├── .kaggle/           # Carpeta con el kaggle.json config
│   ├── main.py            # Script principal para la descarga y preparación de datos
│   ├── requirements.txt   # Archivo con las dependencias necesarias para ejecutar el script
```

## **Instrucciones de Configuración**
### 1. **Clonar el Repositorio**
Primero, clona este repositorio en tu máquina local:
```bash
git clone https://github.com/usuario/flight-delay-analysis.git
cd flight-delay-analysis
```

### 2. **Instalar Dependencias**
El archivo `requirements.txt` dentro de `scripts/data_acquisition` contiene las dependencias necesarias, como `kaggle` y `pandas`. Para instalarlas, ejecuta:
```bash
pip install -r scripts/data_acquisition/requirements.txt
```

### 3. **Configurar Kaggle**
Asegúrate de que el archivo `kaggle.json` ya se encuentra dentro de la carpeta `.kaggle` junto al script `main.py`. Este archivo contiene tus credenciales de acceso a la API de Kaggle. Si no tienes este archivo:
1. Inicia sesión en tu cuenta de Kaggle.
2. Dirígete a **My Account** y desciende hasta la sección **API**.
3. Haz clic en **Create New API Token** para descargar el archivo `kaggle.json`.
4. Coloca el archivo en la carpeta `.kaggle` dentro de `scripts/data_acquisition/`.

### 4. **Ejecutar el Script**
Ejecuta el script principal para descargar y preparar los datos:
```bash
python scripts/data_acquisition/main.py
```
Este script descargará el conjunto de datos `flight-delay-dataset-20182022` de Kaggle y procesará los datos para análisis posterior.

Por ahora este archivo simplemente imprime las primeras 5 filas de los primeros 5 archivos contenidos en la carpeta raw del proyecto en kaggle: https://www.kaggle.com/datasets/robikscube/flight-delay-dataset-20182022

El archivo outputExample.txt es el resultado esperado al ejecutar este script.


## **Dependencias**
Las dependencias necesarias se encuentran en `scripts/data_acquisition/requirements.txt`. Incluyen:
- `kaggle`: Para la descarga de datos directamente desde Kaggle.
- `pandas`: Para la manipulación de datos.

## **Notas Importantes**
- **Configuración del Entorno:** Asegúrate de usar un entorno virtual para evitar conflictos de dependencias. Puedes crear uno con:
```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows
```
- **Privacidad de Kaggle API:** Nunca compartas públicamente tu archivo `kaggle.json`.

## **Contribuciones**
Si deseas contribuir a este proyecto, abre un *Pull Request* o crea un *Issue* describiendo el cambio propuesto.

