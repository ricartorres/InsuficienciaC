# Definición de los datos

## Origen de los datos

El set de datos es una recopilación de datos médicos y demográficos de los pacientes, que incluye su estado de diabetes, indicando si es positivo o negativo. Este conjunto de datos se adquirió de kaggle el set de datos se llama "Diabetes prediction dataset".

## Especificación de los scripts para la carga de datos

El cargue de datos se hace por medio del archivo .csv, en donde el código se encuentra en la subcarpeta data_acquisition en el archivo main.py

## Referencias a rutas o bases de datos origen y destino

Solo se cuenta con una base de datos que es diabetes.csv

### Rutas de origen de datos

El proceso de preprocesamiento del conjunto de datos de predicción de la diabetes comienza identificando y eliminando registros duplicados. Luego, se separan las características de las etiquetas, asignándoles las variables X e y, siendo "Diabetes" nuestra etiqueta. Se aplican métodos de preprocesamiento específicos para variables booleanas, numéricas y categóricas. La normalización se realiza utilizando MinMaxScaler debido a las variaciones en los rangos de los valores. Las variables categóricas se codifican con one-hot encoding. Finalmente, se divide el conjunto de datos en un 80% para entrenamiento y un 20% para pruebas

Todo el procedimiento del preprocesamiento de los datos se encuentra en una nueva rama que se llama preprocesamiento, en la carpeta scripts en la subcarpeta preprocessing, el archivo preprocessing.ipynb es donde se encuentra el respectivo codigo. 

