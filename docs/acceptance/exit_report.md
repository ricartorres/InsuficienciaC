# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de machine learning y presenta los principales logros y lecciones aprendidas durante el proceso.

## Resultados del proyecto

- Resumen de los entregables y logros alcanzados en cada etapa del proyecto.
  Preprocesamiento de datos: Se completó con éxito la limpieza, transformación y normalización de los datos, lo que permitió mejorar la calidad de la información utilizada en los modelos.
Entrenamiento de modelos: Cinco modelos diferentes fueron entrenados y evaluados: XGBoost, LightGBM, MLPClassifier, Random Forest y Regresión Logística.
Evaluación del rendimiento: Se utilizaron diversas métricas de evaluación (accuracy, precision, recall, F1 score, AUC-ROC, log loss, MCC y specificity) para evaluar y comparar los modelos.


- Evaluación del modelo final y comparación con el modelo base.
  El modelo XGBoost se identificó como el mejor modelo debido a su capacidad para obtener una precisión de 1.0, un AUC-ROC de 0.96 y un log loss bajo (0.29), lo que lo convierte en una opción óptima para tareas de clasificación binaria.
   El modelo base sirvió como punto de referencia, proporcionando un rendimiento inicial con métricas moderadas que luego fueron superadas por XGBoost y otros modelos.
  
- Descripción de los resultados y su relevancia para el negocio.
Los resultados del modelo XGBoost sugieren que la clasificación binaria puede realizarse con alta precisión y robustez, lo que es crucial para aplicaciones donde la detección temprana de eventos es importante.

El alto AUC-ROC indica que el modelo puede distinguir eficientemente entre las clases, lo cual es valioso para tomar decisiones informadas en escenarios críticos como predicciones de reingreso hospitalarioc.

## Lecciones aprendidas

- Identificación de los principales desafíos y obstáculos encontrados durante el proyecto.
  - La calidad de los datos fue un desafío inicial. Se presentaron datos desbalanceados y algunas variables tuvieron valores faltantes que requirieron tratamiento adecuado para no afectar el desempeño de los modelos.
  - Durante el entrenamiento de los modelos, la optimización de hiperparámetros fue crucial para mejorar el rendimiento, especialmente en modelos como XGBoost y MLPClassifier.
  - El desbalance de clases también presentó un desafío, pero fue mitigado utilizando técnicas como SMOTE para el sobreajuste de clases minoritarias.

- Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación del modelo.
  - x
- Recomendaciones para futuros proyectos de machine learning.
  - y

## Impacto del proyecto

- Descripción del impacto del modelo en el negocio o en la industria.
  - El modelo XGBoost tiene el potencial de impactar positivamente en diversas aplicaciones industriales y empresariales, como la mejora en la detección de riesgos de salud, la optimización de procesos de producción y la predicción de comportamientos futuros de clientes.
  - En el contexto hospitalario, este modelo podría mejorar la predicción de reingresos hospitalarios, permitiendo una mejor asignación de recursos y un tratamiento más eficiente de los pacientes.
  - 
- Identificación de las áreas de mejora y oportunidades de desarrollo futuras.
  - La integración del modelo en sistemas de producción requiere pruebas adicionales y validación en tiempo real.
  - Explorar el uso de modelos híbridos que combinen los puntos fuertes de modelos como XGBoost y LightGBM para mejorar aún más la precisión.

## Conclusiones

- Resumen de los resultados y principales logros del proyecto.
  - Logramos usar la metodología encontrandonos con inconvenientes que supimos resolver, sobretodo en el despliegue.
  - Es importante tener en cuenta los roles que se deben tener en cuenta en las etapas de despliegue. Seguramente un admisnitardoe de repositorio hubiera tenido una política de backups y hubieramos recuperado el total del repositorio.
  - El proyecto logró desarrollar y entrenar varios modelos de machine learning, con XGBoost destacándose como el modelo más eficiente en términos de precisión y capacidad de discriminación entre clases.
  - Las métricas de evaluación confirmaron que XGBoost es el modelo más robusto para esta tarea de clasificación binaria.
- Conclusiones finales y recomendaciones para futuros proyectos.

## Agradecimientos

- Agradecemos al equipo de trabajo de la Universidad Nacional por su dedicación, habilidades técnicas y esfuerzo continuo durante todas las etapas del proyecto.
- Agradecimientos especiales a mis compañero de estudio quienes colaboraron resolviendo dudas e inquietudes a través de las plataformas de colaboración.
- Un agradecimiento especial a mi compañero Henry, con quien tuve el privilegio de trabajar en equipo, avanzando día a día en la consecución del proyecto. Aprendí mucho de su calidad humana, así como de su profesionalismo tanto en el ámbito médico como en sistemas.
