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
  - Este dataset no tiene valores faltantes explícitos en las columnas (¡excelente calidad de datos!).

- Distribución de las variables:
  - Resumen estadístico para las variables numéricas (media, mediana, desviación estándar, rango).

    
 | Variable | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|---|---|---|---|---|---|---|---|---|
| age | 299 | 60.833893 | 11.894809 | 40.0 | 51.0 | 60.0 | 70.0 | 95.0 |
| anaemia | 299 | 0.431438 | 0.496107 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 |
| creatinine_phosphokinase | 299 | 581.839465 | 970.287881 | 23.0 | 116.5 | 250.0 | 582.0 | 7861.0 |
| diabetes | 299 | 0.418060 | 0.494067 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 |
| ejection_fraction | 299 | 38.083612 | 11.834841 | 14.0 | 30.0 | 38.0 | 45.0 | 80.0 |
| high_blood_pressure | 299 | 0.351171 | 0.478136 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 |
| platelets | 299 | 263358.029264 | 97804.236869 | 25100.0 | 212500.0 | 262000.0 | 303500.0 | 850000.0 |
| serum_creatinine | 299 | 1.393880 | 1.034510 | 0.5 | 0.9 | 1.1 | 1.4 | 9.4 |
| serum_sodium | 299 | 136.625418 | 4.412477 | 113.0 | 134.0 | 137.0 | 140.0 | 148.0 |
| sex | 299 | 0.648829 | 0.478136 | 0.0 | 0.0 | 1.0 | 1.0 | 1.0 |
| smoking | 299 | 0.321070 | 0.467670 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 |
| time | 299 | 130.260870 | 77.614208 | 4.0 | 73.0 | 115.0 | 203.0 | 285.0 |
| DEATH_EVENT | 299 | 0.321070 | 0.467670 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 |



  - **Tablas de frecuencia para las variables categóricas.**
Interpretación de las tablas de frecuencias para cada variable categórica:

Anemia (anaemia):
- 0 (No anemia): ~57% de los pacientes
- 1 (Sí anemia): ~43% de los pacientes

Diabetes (diabetes):
- 0 (No diabetes): ~58% de los pacientes
- 1 (Sí diabetes): ~42% de los pacientes

Hipertensión (high_blood_pressure):

- 0 (No hipertensión): ~65% de los pacientes
- 1 (Sí hipertensión): ~35% de los pacientes

Sexo (sex):
- 0 (Mujer): ~35% de los pacientes
- 1 (Hombre): ~65% de los pacientes

Tabaquismo (smoking):
- 0 (No fumador): ~68% de los pacientes
- 1 (Fumador): ~32% de los pacientes

Fallecimiento (DEATH_EVENT):
- 0 (Sobrevivió): ~68% de los pacientes
- 1 (Falleció): ~32% de los pacientes

**Observaciones importantes:**
- Hay un desbalanceo en la variable objetivo (DEATH_EVENT), lo que podría requerir técnicas de balanceo de clases
- La mayoría de los pacientes son hombres (65%)
- La hipertensión y el tabaquismo están presentes en aproximadamente un tercio de los pacientes
- La diabetes y la anemia están presentes en cerca del 40% de los casos


## Resumen de calidad de los datos

**1. Valores Faltantes**
- Cantidad y Porcentaje: Tras el análisis exploratorio, no se identificaron valores faltantes en el conjunto de datos. Esto indica que todas las variables cuentan con observaciones completas, lo que evita la necesidad de técnicas de imputación o eliminación de registros.
- Acciones Tomadas: No se realizaron acciones para tratar valores faltantes, ya que no existen en el dataset.

**2. Valores Extremos**
- Identificación:
  - Las variables numéricas como serum_creatinine y serum_sodium presentan valores extremos que podrían influir significativamente en los análisis y modelos.
  - Por ejemplo, en serum_creatinine, se observaron valores considerablemente altos (por encima de 4 mg/dL), lo que puede representar casos clínicos reales, pero también puede ser ruido.
- Acciones Tomadas:
  - Los valores extremos no se eliminaron ni transformaron, ya que pueden representar información valiosa sobre casos clínicos específicos. Sin embargo, se recomienda normalizar estas variables para modelos predictivos.
 
**3. Errores**
- Identificación: No se detectaron valores claramente erróneos en el conjunto de datos, como números fuera de rango o inconsistencias en variables categóricas.
- Acciones Tomadas: No fue necesario corregir errores, ya que no se identificaron problemas en las observaciones.

**4. Duplicados**
- Identificación:
  - Se verificó la presencia de registros duplicados en el conjunto de datos.
  - No se encontraron duplicados, lo que sugiere que cada fila representa un caso único.
- Acciones Tomadas: No se eliminaron registros, ya que no existían duplicados.

**Conclusión**
- La calidad de los datos es alta, ya que:
1. No hay valores faltantes ni duplicados, lo que evita pérdida de información o sesgos por eliminación de registros.

2. Los valores extremos están presentes en algunas variables relevantes como serum_creatinine. Sin embargo, dado que estos valores podrían ser clínicamente significativos, no se eliminaron, pero se recomienda manejarlos con técnicas como normalización o transformación logarítmica en análisis posteriores.
3. No se detectaron errores evidentes en los datos.

Este conjunto de datos está en condiciones óptimas para proceder con análisis avanzados y modelado predictivo.


## Variable objetivo

En esta sección se describe la variable objetivo. Se muestra la distribución de la variable y se presentan gráficos que permiten entender mejor su comportamiento.

## Variables individuales

En esta sección se presenta un análisis detallado de cada variable individual. Se muestran estadísticas descriptivas, gráficos de distribución y de relación con la variable objetivo (si aplica). Además, se describen posibles transformaciones que se pueden aplicar a la variable.

## Ranking de variables

En esta sección se presenta un ranking de las variables más importantes para predecir la variable objetivo. Se utilizan técnicas como la correlación, el análisis de componentes principales (PCA) o la importancia de las variables en un modelo de aprendizaje automático.

## Relación entre variables explicativas y variable objetivo

En esta sección se presenta un análisis de la relación entre las variables explicativas y la variable objetivo. Se utilizan gráficos como la matriz de correlación y el diagrama de dispersión para entender mejor la relación entre las variables. Además, se pueden utilizar técnicas como la regresión lineal para modelar la relación entre las variables.
