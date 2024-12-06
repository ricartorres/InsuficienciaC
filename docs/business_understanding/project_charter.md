# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Predicciòn del status de los vuelos

## Objetivo del Proyecto

Desarrollar un modelo predictivo que permita determinar la probabilidad de que un vuelo sea cancelado o experimenta retrasos

## Alcance del Proyecto

### Incluye:

- Se utilizará el conjunto de datos de vuelos que abarca 5 años desde enero de 2018. Este conjunto incluye información sobre vuelos, como horarios, aerolíneas, aeropuertos de origen y destino, motivos de cancelación y retrasos, así como condiciones climáticas relevantes.
- Se espera desarrollar un modelo predictivo que pueda identificar con precisión si un vuelo será cancelado o retrasado. Además, se pretende estimar el tiempo de retraso en caso de que ocurra.
- Será considerado exitoso si se logra una precisión superior al 70% en las predicciones del estado de los vuelos y una estimación razonable del tiempo de retraso. 

### Excluye:

- Este proyecto no incluirá la implementación de un sistema en tiempo real para la predicción de vuelos ni el análisis de datos más allá del periodo mencionado. Tampoco se abordarán aspectos relacionados con la gestión operativa de las aerolíneas o la logística asociada a las cancelaciones y retrasos.

## Metodología

La metodología seguirá las siguientes etapas:

1) Entendimiento del negocio y carga de datos: Definir objetivos y criterios de éxito, asegurando que el modelo predictivo cumpla con una precisión superior al 70% en identificar vuelos cancelados o retrasados y una estimación razonable del tiempo de retraso.

2) Preprocesamiento, análisis exploratorio, reporte del resumen: Limpiar y explorar el conjunto de datos histórico de vuelos (2018-2023), seleccionando variables clave como horarios, aeropuertos, aerolíneas, motivos de cancelación y condiciones climáticas.

3) Modelamiento y extracción de características: Desarrollar modelos predictivos utilizando distinto algoritmos de machine learning para clasificar el estado de los vuelos y estimar el tiempo de retraso, evaluando métricas como precisión y MAE.

4) Despliegue: Crear un prototipo funcional para ejecutar el modelo con datos históricos, documentar scripts reproducibles y generar recomendaciones para su integración en sistemas futuros.

5) Evaluación y Entrega Final: Validar los resultados del modelo frente a los objetivos definidos y presentar los hallazgos principales por medio de un video informativo.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semana | del 20 de noviembre al 28 de noviembre |
| Preprocesamiento, análisis exploratorio, reporte del resumen | 1 semana | del 29 de noviembre al 5 de diciembre |
| Modelamiento y extracción de características | 1 semana | del 6 de diciembre al 12 de diciembre |
| Despliegue | 1 semana | del 13 de diciembre al 19 de diciembre |
| Evaluación y entrega final | 2 semanas | del 13 de diciembre al 21 de diciembre |

## Equipo del Proyecto

- Cristhian David Mora Uribe cdmorau@unal.edu.co
- Martin Camilo Rodriguez Murcia mrodriguezmu@unal.edu.co
- Nestor Steven Negrete Pinilla narutones98@gmail.com
