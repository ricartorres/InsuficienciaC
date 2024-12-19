# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

- Número de observaciones: 299 registros
- Número de variables: Incluye tanto las características predictoras como la variable objetivo: 13 variables
- Tipos de variables:

  a) Variables Numéricas Continuas:
  - age (edad en años)
  - creatinine_phosphokinase (nivel de enzima CPK en sangre)
  - ejection_fraction (porcentaje de sangre que sale del corazón en cada contracción)
  - platelets (conteo de plaquetas en sangre)
  - serum_creatinine (nivel de creatinina en sangre)
  - serum_sodium (nivel de sodio en sangre)

  b) variables Numéricas Discretas:
  - time (período de seguimiento en días)

  c) Variables categóricas Binarias (dicotómicas):
  - anaemia (0 = no, 1 = sí)
  - diabetes (0 = no, 1 = sí)
  - high_blood_pressure (0 = no, 1 = sí)
  - sex (0 = mujer, 1 = hombre)
  - smoking (0 = no, 1 = sí)
  - DEATH_EVENT (0 = sobrevivió, 1 = falleció) - Esta es la variable objetivo
 

- Valores faltantes:
  - Describe si hay valores faltantes y cuántos hay en cada columna.
  - Incluye un porcentaje de valores faltantes para cada variable.
- Distribución de las variables:
  - Resumen estadístico para las variables numéricas (media, mediana, desviación estándar, rango).
  - Tablas de frecuencia para las variables categóricas.

## Resumen de calidad de los datos

En esta sección se presenta un resumen de la calidad de los datos. Se describe la cantidad y porcentaje de valores faltantes, valores extremos, errores y duplicados. También se muestran las acciones tomadas para abordar estos problemas.

## Variable objetivo

En esta sección se describe la variable objetivo. Se muestra la distribución de la variable y se presentan gráficos que permiten entender mejor su comportamiento.

## Variables individuales

En esta sección se presenta un análisis detallado de cada variable individual. Se muestran estadísticas descriptivas, gráficos de distribución y de relación con la variable objetivo (si aplica). Además, se describen posibles transformaciones que se pueden aplicar a la variable.

## Ranking de variables

En esta sección se presenta un ranking de las variables más importantes para predecir la variable objetivo. Se utilizan técnicas como la correlación, el análisis de componentes principales (PCA) o la importancia de las variables en un modelo de aprendizaje automático.

## Relación entre variables explicativas y variable objetivo

En esta sección se presenta un análisis de la relación entre las variables explicativas y la variable objetivo. Se utilizan gráficos como la matriz de correlación y el diagrama de dispersión para entender mejor la relación entre las variables. Además, se pueden utilizar técnicas como la regresión lineal para modelar la relación entre las variables.
