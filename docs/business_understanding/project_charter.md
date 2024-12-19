![Descripción de la imagen](images/Falla-cardiaca.jpg)

# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

### Predicción de Insuficiencia Cardíaca con Machine Learning

### 1. Entendimiento del Negocio

#### Insuficiencia Cardíaca
La insuficiencia cardíaca es una afección crónica y grave que se desarrolla con el tiempo. A medida que la capacidad de bombeo del corazón se debilita, resulta más difícil llenar y bombear sangre adecuadamente. Esto provoca diversos síntomas y puede afectar tanto el lado derecho, el lado izquierdo, o ambos lados del corazón.

- **Referencias**:
  - American Heart Association: [What is Heart Failure](https://www.heart.org/-/media/files/health-topics/answers-by-heart/answers-by-heart-spanish/what-is-heartfailure_span.pdf)
  - National Institute on Aging: [Insuficiencia Cardíaca](https://www.nia.nih.gov/espanol/corazon/insuficiencia-cardiaca#:~:text=La%20insuficiencia%20card%C3%ADaca%20es%20una,satisfacer%20las%20necesidades%20del%20cuerpo)

#### Datos Clave
- Las enfermedades cardiovasculares son la principal causa de muerte a nivel mundial.
- Las muertes relacionadas con cardiopatías y accidentes cerebrovasculares afectan desproporcionadamente a países de ingresos medianos y bajos.
- Factores como una alimentación poco saludable, inactividad física, y tabaquismo aumentan el riesgo de enfermedades cardiovasculares.

- **Referencias**:
  - Organización Panamericana de la Salud: [Enfermedades Cardiovasculares](https://www.paho.org/es/temas/enfermedades-cardiovasculares)
  - Organización Mundial de la Salud: [Enfermedades Cardiovasculares](https://www.who.int/es/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds))

#### Síntomas
- Dolor de pecho (angina de pecho)
- Falta de aire
- Dolor o entumecimiento en las extremidades
- Dolor en el cuello, mandíbula, garganta, abdomen superior o espalda

- **Referencias**:
  - Organización Panamericana de la Salud: [Síntomas de Enfermedades Cardiovasculares](https://www.paho.org/es/temas/enfermedades-cardiovasculares)
  - Organización Mundial de la Salud: [Síntomas de Enfermedades Cardiovasculares](https://www.who.int/es/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds))

#### Factores de Riesgo
- **Demográficos**: Edad, sexo, antecedentes familiares
- **Estilo de Vida**: Tabaquismo, alimentación, actividad física, consumo de alcohol
- **Condiciones Médicas**: Hipertensión, diabetes, hiperlipidemia, obesidad
- **Ambientales**: Contaminación atmosférica

- **Referencias**:
  - Organización Panamericana de la Salud: [Factores de Riesgo de Enfermedades Cardiovasculares](https://www.paho.org/es/temas/enfermedades-cardiovasculares)
  - Organización Mundial de la Salud: [Factores de Riesgo de Enfermedades Cardiovasculares](https://www.who.int/es/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds))

#### Diagnóstico
El diagnóstico de la insuficiencia cardíaca puede ser difícil, especialmente en las etapas iniciales. Muchos de los síntomas de la insuficiencia cardiaca no son específicos y, por lo tanto, no ayudan a distinguir entre la insuficiencia cardiaca y otros problemas. Los síntomas más específicos (ortopnea y disnea paroxística nocturna) son menos comunes, especialmente en pacientes con síntomas más leves, por lo que no son sensibles. Los síntomas y signos pueden ser especialmente difíciles de identificar e interpretar en obesos, persona mayor y paciente con EPOC

- **Referencias**: 
- scielo: [Factores que inciden en la insuficiencia cardíaca en pacientes de edades adultas](https://homolog-ve.scielo.org/scielo.php?script=sci_arttext&pid=S1316-48212023000200108)

#### Prevención
Las enfermedades cardiovasculares son la principal causa de defunción en el mundo. Según las estimaciones, se cobran cada año 17,9 millones de vidas. Para prevenir las defunciones prematuras es preciso conocer cuáles son las personas que corren más riesgo cardiovascular y velar por que reciban el tratamiento adecuado. Además, el acceso a medicamentos esenciales y tecnologías básicas de salud que permitan tratar las enfermedades no transmisibles en todos los centros de atención primaria es esencial para proporcionar tratamiento y asesoramiento a toda persona que lo necesite.

- **Referencias**: 
- Organización Mundial de la Salud: [Enfermedades cardiovasculares] (https://www.who.int/es/health-topics/cardiovascular-diseases#tab=tab_1)




### 2. Justificación del Uso de Machine Learning

#### Puntos Clave
1. **Complejidad del Diagnóstico Temprano**: Los síntomas no específicos dificultan el diagnóstico temprano.
2. **Impacto en la Salud Pública**: Principales causantes de muerte a nivel mundial, afectando especialmente a países de ingresos medianos y bajos.
3. **Múltiples Factores de Riesgo Interrelacionados**: Machine learning puede analizar múltiples factores simultáneamente para identificar patrones complejos.
4. **Necesidad de Prevención**: Identificación temprana de personas en riesgo para proporcionar tratamiento adecuado.

Machine learning se justifica porque puede procesar y analizar múltiples variables, detectar relaciones no lineales entre los factores de riesgo, identificar pacientes en riesgo antes de que desarrollen síntomas evidentes, y contribuir a los objetivos de salud pública.

### 3. Modelos de Machine Learning

#### 1. Modelos de Clasificación Binaria
a) **Regresión Logística**
- **Ventajas**: Alta interpretabilidad, puede proporcionar probabilidades de riesgo, útil para identificar la importancia de los factores de riesgo.
- **Uso**: Modelo base para evaluar el riesgo inicial de insuficiencia cardíaca.

b) **Random Forest**
- **Ventajas**: Maneja bien datos no lineales y correlacionados, proporciona importancia de características, robusto ante valores atípicos.
- **Uso**: Identificar interacciones complejas entre factores como edad, estilo de vida y condiciones médicas.

c) **XGBoost/LightGBM**
- **Ventajas**: Alto rendimiento en datos estructurados, maneja bien datos desbalanceados, puede capturar patrones sutiles.
- **Uso**: Modelo principal para predicción debido a su precisión y capacidad de manejo de datos complejos.

#### 2. Redes Neuronales
a) **Perceptrón Multicapa (MLP)**
- **Ventajas**: Puede capturar relaciones muy complejas, útil para integrar diferentes tipos de datos, puede procesar tanto variables continuas como categóricas.
- **Uso**: Especialmente útil si se integran datos de diferentes fuentes (historial médico, datos de sensores, etc.).

#### 3. Modelos de Supervivencia
a) **Cox Proportional Hazards**
- **Ventajas**: Puede predecir no solo si ocurrirá la insuficiencia cardíaca, sino cuándo, incorpora el factor tiempo en el análisis.
- **Uso**: Evaluar la progresión de la enfermedad y el riesgo a lo largo del tiempo.

### 4. Propuesta de Implementación

#### 1. Preparación y Preprocesamiento de Datos
- Recolección de datos relevantes (historial médico, demográficos, estilo de vida, etc.)
- Limpieza y normalización de datos.
- División del dataset en entrenamiento y prueba.

#### 2. Modelado
- Entrenamiento de diferentes modelos de machine learning.
- Validación cruzada para evaluar el rendimiento de los modelos.
- Selección del modelo óptimo basado en las métricas de rendimiento (precisión, recall, AUC, etc.).

#### 3. Evaluación
- Evaluación del modelo seleccionado en el conjunto de prueba.
- Interpretación de los resultados y ajuste de hiperparámetros si es necesario.

#### 4. Despliegue
- Implementación del modelo en un entorno de producción.
- Desarrollo de una interfaz para que los profesionales médicos puedan utilizar el modelo.
- Monitorización y actualización del modelo con nuevos datos.

### 5. Conclusiones y Futuras Mejoras
- Resumen de los hallazgos y el impacto potencial del modelo.
- Discusión sobre posibles mejoras y futuras direcciones de investigación.




## Objetivo del Proyecto

**Objetivo General:**
Desarrollar un modelo predictivo basado en técnicas de machine learning para identificar tempranamente el riesgo de insuficiencia cardíaca en pacientes, mediante el análisis de factores de riesgo clínicos y no clínicos, contribuyendo así a la prevención y diagnóstico temprano de la enfermedad.

**Objetivos Específicos:**

1. Relacionados con el Análisis de Datos:
- Identificar y analizar los principales factores de riesgo asociados con la insuficiencia cardíaca según la literatura médica y los datos disponibles
- Determinar las correlaciones y patrones entre los diferentes factores de riesgo y el desarrollo de la enfermedad
- Evaluar la importancia relativa de cada factor en el desarrollo de la insuficiencia cardíaca

2. Relacionados con el Modelo:
- Desarrollar un sistema de clasificación que combine múltiples modelos de machine learning para predecir el riesgo de insuficiencia cardíaca
- Optimizar el rendimiento del modelo para lograr un equilibrio entre sensibilidad y especificidad en la detección de casos de riesgo
- Implementar técnicas de interpretabilidad para explicar las predicciones del modelo de manera comprensible para el personal médico

3. Relacionados con la Aplicación Clínica:
- Crear una herramienta de screening que ayude a los profesionales de la salud en la identificación temprana de pacientes en riesgo
- Establecer un sistema de puntuación de riesgo que permita clasificar a los pacientes en diferentes niveles de prioridad para intervención médica
- Diseñar una interfaz usuario-amigable para la implementación práctica del modelo en entornos clínicos

4. Relacionados con el Impacto en Salud Pública:
- Contribuir a la reducción de la mortalidad por enfermedades cardiovasculares mediante la detección temprana
- Optimizar la asignación de recursos médicos priorizando la atención en pacientes con mayor riesgo



## Alcance del Proyecto

### Incluye:

1. Descripción de los datos disponibles:
- Datos demográficos:
  - Edad
  - Sexo

- Datos clínicos:
  - anaemia
  - creatinine_phosphokinase
  - diabetes
  - ejection_fraction
  - high_blood_pressure
  - platelets
  - serum_creatinine
  - serum_sodium

2. Resultados esperados:

a) Modelo predictivo:
- Sistema de clasificación de riesgo de insuficiencia cardíaca
- Puntuación de riesgo para cada paciente
- Identificación de factores de riesgo más relevantes
- Intervalos de confianza para las predicciones

b) Documentación técnica:
- Manual de implementación del modelo
- Documentación del código
- Guía de interpretación de resultados
- Reporte de validación y pruebas

c) Herramientas de visualización:
- Dashboard para monitoreo de predicciones
- Gráficos de importancia de variables
- Visualización de tendencias y patrones


3. Criterios de éxito:

a) Métricas técnicas:
- Sensibilidad > 80% (detección de casos positivos)
- Especificidad > 75% (identificación correcta de casos negativos)
- Área bajo la curva ROC > 0.85
- Valor predictivo positivo > 70%

b) Métricas de implementación:
- Tiempo de procesamiento < 5 segundos por predicción
- Tasa de error en producción < 1%
- Disponibilidad del sistema > 99%

c) Métricas de impacto:
- Reducción del tiempo de diagnóstico
- Mejora en la identificación temprana de casos de riesgo
- Satisfacción del personal médico con la herramienta



### Excluye:

1. Desarrollo de hardware:
- No incluye desarrollo de dispositivos médicos
- No incluye integración con equipos de monitoreo cardíaco
- No incluye desarrollo de sensores o dispositivos de medición

2. Aspectos médicos:
- No reemplaza el diagnóstico médico profesional
- No genera planes de tratamiento
- No proporciona recomendaciones médicas específicas
- No incluye seguimiento de pacientes
- No realiza ajustes de medicación

3. Aspectos técnicos:
- No incluye desarrollo de aplicaciones móviles
- No incluye integración con sistemas de historias clínicas existentes
- No incluye procesamiento de imágenes médicas
- No incluye análisis de señales ECG
- No incluye procesamiento de datos en tiempo real

4. Aspectos administrativos:
- No incluye gestión de citas médicas
- No incluye gestión de inventario de medicamentos
- No incluye facturación o aspectos financieros
- No incluye gestión de recursos hospitalarios

5. Ámbito geográfico:
- No incluye adaptación a regulaciones internacionales
- No incluye localización para múltiples idiomas
- No incluye consideraciones específicas de diferentes sistemas de salud

## Metodología CRISP-DM para predicción de insuficiencia cardíaca

1. Comprensión del negocio

a) Objetivos del negocio:
- Mejorar la detección temprana de insuficiencia cardíaca
- Reducir la mortalidad por enfermedades cardiovasculares
- Optimizar recursos médicos mediante la identificación preventiva de casos de riesgo

b) Evaluación de la situación:
- Las enfermedades cardiovasculares son la principal causa de muerte global
- El diagnóstico temprano es difícil y los síntomas no son específicos
- Se necesitan herramientas de apoyo para la identificación de pacientes en riesgo

c) Objetivos de minería de datos:
- Desarrollar un modelo predictivo con alta sensibilidad y especificidad
- Identificar los factores de riesgo más relevantes
- Generar un sistema de puntuación de riesgo interpretable

2. Comprensión de los datos

a) Recolección de datos:
- Datos demográficos de pacientes
- Mediciones clínicas

b) Exploración de datos:
- Análisis estadístico descriptivo
- Identificación de patrones y correlaciones
- Visualización de distribuciones
- Análisis de valores atípicos

c) Verificación de calidad:
- Identificación de datos faltantes
- Validación de rangos y valores
- Verificación de consistencia
- Identificación de sesgos potenciales


3. Preparación de los datos

a) Selección de datos:
- Identificación de variables relevantes
- Eliminación de variables redundantes
- Selección de período de análisis
- Definición de criterios de inclusión/exclusión

b) Limpieza de datos:
- Tratamiento de valores faltantes
- Manejo de valores atípicos
- Corrección de inconsistencias
- Estandarización de formatos

c) Construcción de datos:
- Creación de nuevas características
- Agregación de variables
- Normalización de mediciones
- Codificación de variables categóricas

d) Integración de datos:
- Combinación de múltiples fuentes
- Validación de integridad
- Resolución de conflictos
- Creación de conjunto de datos final

4. Modelado

a) Selección de técnicas:
- Random Forest
- XGBoost
- Regresión Logística
- Redes Neuronales

b) Diseño de pruebas:
- Definición de esquema de validación cruzada
- Establecimiento de métricas de evaluación
- Diseño de experimentos
- Planificación de pruebas de robustez

c) Construcción del modelo:
- Entrenamiento de modelos individuales
- Optimización de hiperparámetros
- Implementación de ensemble
- Validación de resultados

5. Evaluación

a) Evaluación de resultados:
- Análisis de métricas de rendimiento
- Verificación de cumplimiento de objetivos
- Evaluación de generalización
- Análisis de casos de error

b) Validación del proceso:
- Revisión de cada paso del desarrollo
- Verificación de decisiones tomadas
- Evaluación de alternativas
- Documentación de lecciones aprendidas

c) Determinación de próximos pasos:
- Identificación de mejoras potenciales
- Planificación de iteraciones
- Definición de mantenimiento
- Establecimiento de monitoreo

6. Despliegue

a) Planificación del despliegue:
- Diseño de arquitectura de implementación
- Definición de requisitos técnicos
- Establecimiento de procedimientos de actualización
- Desarrollo de documentación

b) Monitoreo y mantenimiento:
- Implementación de sistema de monitoreo
- Definición de procedimientos de actualización
- Establecimiento de controles de calidad
- Plan de mantenimiento continuo

c) Producción de reporte final:
- Documentación técnica completa
- Manual de usuario
- Guía de interpretación de resultados
- Reporte de evaluación final

d) Revisión del proyecto:
- Evaluación de cumplimiento de objetivos
- Documentación de experiencias
- Identificación de mejores prácticas
- Recomendaciones para proyectos futuros



## Cronograma

![Descripción de la imagen](images/CronogramaFallaCardiaca.png)

## Reuniones de Trabajo

Semana1
![Descripción de la imagen](images/Semana1.png)

Semana2
![Descripción de la imagen](images/Semana2.png)

Semana3
![Descripción de la imagen](images/Semana3.png)

Semana4
![Descripción de la imagen](images/Semana4.png)

Semana5
![Descripción de la imagen](images/Semana5.png)



## Equipo del Proyecto

- Ricardo Torres
- Henry Bolaños

## Presupuesto

Este se encuentra en el plan de direccionamiento de proyecto según definición de oficina de proyectos

## Stakeholders

Los stakeHolders se encuentran en el archivo de interesados relacionado al acta de constitución del proyecto

## Aprobaciones

- Oscar Alberto Bustos Briñez
- [Firma del aprobador]
- 21 Diciembre 2024

- Jorge Eliecer Camargo Mendoza
- [Firma del aprobador]
- 21 Diciembre 2024
