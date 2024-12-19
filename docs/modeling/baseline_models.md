# Reporte del Modelo Baseline

Este documento contiene los resultados de los modelos entrenados.

## Descripción de los modelos

1. XGBoost
XGBoost (Extreme Gradient Boosting) es un algoritmo basado en árboles de decisión que utiliza un enfoque de ensamble para mejorar la precisión del modelo. Se construyen varios árboles de decisión de manera secuencial, y cada nuevo árbol intenta corregir los errores cometidos por los árboles anteriores. Este modelo es altamente eficiente, y es muy utilizado en competencias de machine learning debido a su capacidad para manejar tanto datos lineales como no lineales. Además, XGBoost es conocido por su velocidad y precisión, y es particularmente útil para grandes volúmenes de datos.

2. MLPClassifier (Perceptrón Multicapa)
El MLPClassifier es un tipo de red neuronal que utiliza múltiples capas de perceptrones para procesar datos de entrada y realizar clasificaciones. Este modelo es capaz de aprender patrones complejos en los datos, lo que lo hace adecuado para problemas no lineales. A diferencia de los árboles de decisión, las redes neuronales pueden capturar relaciones más complejas entre las características de entrada. El MLPClassifier se entrena utilizando el algoritmo de retropropagación y es muy flexible en cuanto a la arquitectura de las redes neuronales.

3. LightGBM
LightGBM (Light Gradient Boosting Machine) es otro algoritmo basado en boosting, pero se diferencia de XGBoost en que es más rápido y consume menos memoria. Utiliza una técnica de histogramas para reducir el costo computacional, lo que lo hace eficiente con grandes volúmenes de datos. LightGBM es particularmente útil para problemas en los que se manejan grandes conjuntos de datos y se necesitan tiempos de entrenamiento rápidos.

4. Random Forest
Random Forest es un modelo de ensamble que utiliza múltiples árboles de decisión para mejorar la precisión general del modelo. Cada árbol en el bosque es entrenado en un subconjunto aleatorio de los datos, y luego se realiza una votación para determinar la predicción final. Este enfoque ayuda a reducir el sobreajuste, haciendo que el modelo sea robusto incluso con datos ruidosos.

5. Regresión Logística
La regresión logística es un modelo de clasificación binaria que estima la probabilidad de que una entrada pertenezca a una clase específica. Este modelo es muy simple y eficiente para problemas de clasificación, pero generalmente tiene un rendimiento inferior cuando los datos no son lineales.


## Variables de entrada

Lista de las variables de entrada utilizadas en el modelo.

- time
- ejection_fraction
- serum_creatinine

## Variable objetivo

Nombre de la variable objetivo utilizada en el modelo.

- DEATH_EVENT

## Evaluación del modelo

### Métricas de evaluación

Descripción de las métricas utilizadas para evaluar el rendimiento del modelo.

### Resultados de evaluación

1. XGBoost
   
3. MLPClassifier (Perceptrón Multicapa)
4. LightGBM
5. Random Forest
6. Regresión Logística

Tabla que muestra los resultados de evaluación del modelo baseline, incluyendo las métricas de evaluación.

## Análisis de los resultados

1. XGBoost

- Fortalezas: El modelo XGBoost muestra una precisión perfecta (1.00), lo que sugiere que es extremadamente efectivo para identificar los casos positivos. El AUC-ROC de 0.96 indica que el modelo tiene una excelente capacidad de discriminación entre las clases. Además, el MCC de 0.79 es alto, lo que refleja un buen desempeño general del modelo en términos de balance entre las clases.

- Debilidades: Aunque la precisión es muy alta, el recall de 0.70 indica que el modelo tiene dificultades para identificar todos los casos positivos. El log loss es relativamente bajo (0.29), lo que sugiere que el modelo realiza predicciones razonablemente confiables, pero podría mejorarse en términos de la estimación de probabilidades.
  
2. MLPClassifier (Perceptrón Multicapa)

- Fortalezas: El modelo tiene un excelente rendimiento en términos de precisión (0.92) y recall (0.76), lo que indica que es efectivo tanto para identificar correctamente los positivos como para minimizar los falsos negativos. Además, el AUC-ROC de 0.93 es una señal de que el modelo puede discriminar bien entre las clases.
- Debilidades: Aunque el modelo muestra un buen rendimiento general, el log loss es relativamente alto (0.32), lo que sugiere que las predicciones probabilísticas no son tan precisas. Además, la diferencia entre precisión y recall indica que puede haber algunos problemas con la identificación de todos los casos positivos.
   
3. LightGBM
- Fortalezas: LightGBM tiene un AUC-ROC muy alto (0.96), lo que indica una excelente capacidad de discriminación entre las clases. También presenta un log loss muy bajo (0.23), lo que refleja predicciones confiables.
- Debilidades: Aunque el modelo tiene un buen recall (0.82), su precisión es menor (0.73), lo que sugiere que el modelo predice un mayor número de falsos positivos.

4. Random Forest

- Fortalezas: El modelo tiene un recall alto (0.80), lo que significa que tiene una buena capacidad para identificar casos positivos.
- Debilidades: La precisión y AUC-ROC son muy bajas, lo que sugiere que el modelo está cometiendo muchos falsos positivos. Además, el log loss es muy alto (0.71), lo que refleja predicciones poco confiables.
   
5. Regresión Logística

- Fortalezas: La regresión logística muestra un buen rendimiento en términos de recall (0.72), lo que indica que el modelo es efectivo para identificar los casos positivos.
- Debilidades: La precisión y el AUC-ROC son relativamente bajos, lo que sugiere que el modelo no discrimina bien entre las clases. El log loss es alto, lo que refleja predicciones inexactas.

## Conclusiones

Conclusiones generales sobre el rendimiento del modelo baseline y posibles áreas de mejora.

1. XGBoost
Es un modelo robusto con excelentes resultados en términos de precisión y AUC-ROC. Sin embargo, el recall podría mejorarse para garantizar que se identifiquen más casos positivos. Este modelo es ideal para aplicaciones en las que la precisión es más importante que el recall.
   
2. MLPClassifier (Perceptrón Multicapa)

Muestra un excelente equilibrio entre precisión y recall, siendo adecuado para problemas en los que es crucial identificar correctamente los casos positivos sin perder demasiados. Su rendimiento en términos de AUC-ROC también es muy bueno.

3. LightGBM

Es un modelo eficiente y rápido, con un alto AUC-ROC. Sin embargo, su precisión podría mejorarse, especialmente en escenarios en los que la reducción de falsos positivos es crítica.
   
4. Random Forest

Aunque el modelo tiene un buen recall, su baja precisión y AUC-ROC indican que necesita ajustes significativos para mejorar su desempeño general.
   
5. Regresión Logística

La regresión logística es un modelo básico que, aunque adecuado para problemas simples, no es tan preciso como otros modelos más complejos como XGBoost o MLPClassifier.


## Referencias

Lista de referencias utilizadas para construir el modelo baseline y evaluar su rendimiento.

Espero que te sea útil esta plantilla. Recuerda que puedes adaptarla a las necesidades específicas de tu proyecto.
