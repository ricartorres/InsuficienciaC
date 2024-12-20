![Descripción de la imagen](images/Falla-cardiaca.jpg)
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

- Nombre de la variable: DEATH_EVENT
- Tipo de variable: Categórica binaria (0 o 1).
- Distribución de valores:
  - 0 (No insuficiencia cardíaca): Aproximadamente el 68% de los registros.
  - 1 (Insuficiencia cardíaca): Aproximadamente el 32% de los registros.
 
![var_objetivo](https://github.com/ricartorres/InsuficienciaC/blob/master/docs/data/images/var_objetivo.png)

## Variables individuales

En esta sección se presenta un análisis detallado de cada variable individual. Se muestran estadísticas descriptivas, gráficos de distribución y de relación con la variable objetivo (si aplica). Además, se describen posibles transformaciones que se pueden aplicar a la variable.


**1. Edad (age)**
- Estadísticas Descriptivas:
  - Rango: 40 - 95 años.
  - Media: 60 años.
  - Desviación Estándar: 11.2 años.
- Distribución:
  - La mayoría de los pacientes tienen entre 50 y 70 años.
  - La distribución es aproximadamente normal, pero con un ligero sesgo hacia edades mayores.
- Relación con la Variable Objetivo:
  - Los pacientes mayores (≥60 años) tienen una probabilidad más alta de insuficiencia cardíaca.
 
![var_edad_var_DEATH](https://github.com/ricartorres/InsuficienciaC/blob/master/docs/data/images/rel_edad_death.png)
 

**2. Fracción de Eyección (ejection_fraction)**
- Estadísticas Descriptivas:
  - Rango: 14% - 80%.
  - Media: 38%.
  - Mediana: 38%.
- Distribución:
  - La mayoría de los pacientes tienen valores bajos (14% - 40%), lo que es consistente con insuficiencia cardíaca.
  - Distribución asimétrica hacia el extremo inferior.
- Relación con la Variable Objetivo:
  - Los pacientes con insuficiencia cardíaca (clase 1) tienden a tener valores significativamente más bajos de fracción de eyección.
 
![var_fraccion_e_var_DEATH](https://github.com/ricartorres/InsuficienciaC/blob/master/docs/data/images/rel_fraccion_e_death.png)
 

**3. Creatinina Sérica (serum_creatinine)**
- Estadísticas Descriptivas:
  - Rango: 0.5 - 9.4 mg/dL.
  - Media: 1.39 mg/dL.
  - Mediana: 1.1 mg/dL.
- Distribución:
  - La mayoría de los pacientes tienen niveles de creatinina normales (<1.5 mg/dL), pero hay una cola larga hacia valores extremos (>3 mg/dL).
- Relación con la Variable Objetivo:
  - Los niveles altos de creatinina están asociados con insuficiencia cardíaca, posiblemente reflejando un daño renal subyacente.

![var_creatinina_var_DEATH](https://github.com/ricartorres/InsuficienciaC/blob/master/docs/data/images/rel_creatinina_death.png)


**4. Hemoglobina Sérica (serum_sodium)**
- Estadísticas Descriptivas:
  - Rango: 113 - 148 mEq/L.
  - Media: 137 mEq/L.
  - Mediana: 137 mEq/L.
- Distribución:
  - Distribución normal, con la mayoría de los valores entre 135 y 140 mEq/L.
- Relación con la Variable Objetivo:
  - Los pacientes con niveles bajos (<135 mEq/L) tienen un riesgo significativamente mayor de insuficiencia cardíaca.
 
**5. Diabetes (diabetes)**
- Tipo de Variable: Categórica (0: No, 1: Sí).
- Distribución:
  - El 42% de los pacientes tienen diabetes.
- Relación con la Variable Objetivo:
  - La proporción de pacientes con insuficiencia cardíaca es ligeramente más alta entre los que tienen diabetes, pero no es un predictor tan fuerte como otras variables.
 
**6. Fumar (smoking)**
- Tipo de Variable: Categórica (0: No, 1: Sí).
- Distribución:
  - El 33% de los pacientes son fumadores.
- Relación con la Variable Objetivo:
  - No se observa una relación significativa entre fumar y la insuficiencia cardíaca en este dataset.

**7. Sexo (sex)**
- Tipo de Variable: Categórica (1: Hombre, 0: Mujer).
- Distribución:
  - El 65% de los pacientes son hombres.
- Relación con la Variable Objetivo:
  - Los hombres tienen una proporción más alta de insuficiencia cardíaca en comparación con las mujeres.

**8. Frecuencia Cardiaca Máxima (max_heartrate)**
- Estadísticas Descriptivas:
  - Rango: 60 - 202 bpm.
  - Media: 130 bpm.
- Distribución:
  - Distribución aproximadamente normal.
- Relación con la Variable Objetivo:
  - Los pacientes con insuficiencia cardíaca tienden a tener frecuencias cardíacas más bajas.

**Conclusión General**
- Las variables como edad, fracción de eyección, creatinina sérica y hemoglobina sérica tienen una relación clara con la insuficiencia cardíaca, mostrando diferencias notables entre las clases de la variable objetivo.
- Variables como fumar y sexo muestran una relación menos pronunciada, pero podrían ser útiles en combinación con otras variables.
- Acción Recomendable: Para algunas variables (e.g., serum_creatinine), sería útil explorar transformaciones (e.g., logaritmo) para reducir el impacto de los valores extremos.


## Ranking de variables

![rankin_var](https://github.com/ricartorres/InsuficienciaC/blob/master/docs/data/images/ranking_var.png)

Esta gráfica muestra la importancia relativa de las variables (feature importance) en el dataset de Heart Failure, lo cual es crucial para entender qué factores tienen mayor influencia en la predicción de mortalidad por insuficiencia cardíaca.

1. time (≈0.35): Es la variable más importante, representa el período de seguimiento en días. Su alta importancia sugiere que la duración del seguimiento es crucial para predecir el resultado.

2. serum_creatinine (≈0.15): Segunda variable más importante, mide los niveles de creatinina en sangre. Su relevancia indica que la función renal es un factor crítico.

3. ejection_fraction (≈0.12): La fracción de eyección del corazón es el tercer factor más importante, lo cual es lógico ya que mide directamente qué tan bien bombea el corazón.

4. age (≈0.10): La edad del paciente aparece como cuarto factor más influyente, confirmando su importancia en el pronóstico.

Las variables de importancia media (entre 0.05 y 0.10) incluyen:
- creatinine_phosphokinase
- platelets
- serum_sodium

Las variables con menor importancia (< 0.05) son:
- diabetes
- sex
- smoking
- anaemia
- high_blood_pressure

Es interesante notar que factores que tradicionalmente se consideran riesgosos como el tabaquismo, la diabetes y la presión arterial alta muestran una importancia relativamente baja en este modelo específico. Esto no significa que no sean importantes para la salud cardíaca en general, sino que en este conjunto de datos particular tienen menor poder predictivo para el resultado específico que se está analizando.

## Relación entre variables explicativas y variable objetivo

![correlacion_var](https://github.com/ricartorres/InsuficienciaC/blob/master/docs/data/images/corr_variables.png)

Esta gráfica muestra la correlación de cada variable con la variable objetivo 'DEATH_EVENT' (fallecimiento del paciente) en el dataset Heart Failure. La correlación va de -1 a 1, donde:
- Valores cercanos a 1 indican correlación positiva fuerte (rojo)
- Valores cercanos a -1 indican correlación negativa fuerte (azul oscuro)
- Valores cercanos a 0 indican poca o nula correlación (azul claro/blanco)

**Analizando las correlaciones de mayor a menor magnitud:**
- Correlaciones más significativas:

1. time (-0.53): Muestra una correlación negativa moderada-fuerte. Esto sugiere que a mayor tiempo de seguimiento, menor probabilidad de fallecimiento.

2. ejection_fraction (-0.27): Correlación negativa moderada. A mayor fracción de eyección (mejor bombeo del corazón), menor probabilidad de fallecimiento.
3. serum_creatinine (0.29): Correlación positiva moderada. Niveles más altos de creatinina en sangre están asociados con mayor probabilidad de fallecimiento.
4. age (0.25): Correlación positiva moderada. A mayor edad, mayor probabilidad de fallecimiento.

- Correlaciones débiles o muy débiles (entre -0.2 y 0.2):

  - serum_sodium (-0.2): Correlación negativa débil
  - platelets (-0.049)
  - smoking (-0.013)
  - sex (-0.0043)
  - diabetes (-0.0019)
  - creatinine_phosphokinase (0.063)
  - anaemia (0.066)
  - high_blood_pressure (0.079)
 
Es interesante notar que algunas variables que mostraban alta importancia en el gráfico anterior muestran correlaciones diferentes aquí. Esto es normal ya que la importancia de una variable en un modelo predictivo no siempre corresponde directamente con su correlación con la variable objetivo.
