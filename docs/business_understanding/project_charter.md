# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Clasificador para detección de neumonía pediátrico Pulmonar

## **1. Marco de Proyecto**
---

Normalmente, se suele construir un marco de proyecto para mostrar los resultados del entendimiento del negocio, es decir, debemos dar respuesta a los siguientes elementos:

### **1.1. Trasfondo del Negocio**
---

- ¿Quién es el cliente o los beneficiarios del proyecto? ¿En qué dominio se encuentran (marketing, medicina, entre otros)?
- ¿Qué problemas del negocio o del dominio estamos tratando de solucionar?

El proyecto tiene como objetivo el desarrollo de un modelo de deep learning que permita clasificar y detectar la presencia de neumonía en imágenes de rayos X de pecho en pacientes pediátricos. Con base en lo anterior, Los principales beneficiarios de este proyecto son las instituciones médicas, hospitales y centros de salud, así como los profesionales médicos, entre ellos radiólogos y pediatras ya que la labor de estos profesionales puede ser apoyada con herramientas precisas y rápidas que les permitan diagnosticar neumonía de manera más eficiente y temprana. Al mismo tiempo, los pacientes pediátricos también se benefician indirectamente, ya que la aplicación del modelo propuesto mejorará el proceso diagnóstico, lo que permite que reciban un tratamiento oportuno y adecuado.

Además, este proyecto se sitúa dentro del dominio de la medicina, más específciamente en las áreas de radiología y atención pediátrica. A su vez, está relacionado con el campo emergente de la inteligencia artificial aplicada a la salud, ya que el uso de deep learning para el análisis de imágenes médicas ha demostrado su capacidad de transformar el proceso de detección de diversas enfermedades.

Asimismo, el proyecto busca abordar varios problemas críticos dentro de este dominio. En primer lugar, busca solucionar la cuestión del diagnóstico tardío o inexacto de la neumonía, una enfermedad que puede tener consecuencias graves, especialmente en niños pequeños, si no se diagnostica a tiempo. Adicionalmente, la automatización del diagnóstico a través de inteligencia artificial promete reducir el margen de error y acortar el tiempo que los profesionales médicos requieren para identificar la condición en los pacientes.

### **1.2. Alcance**
---

- ¿Qué  solución basada en _Deep Learning_ queremos implementar?
- ¿Qué  se hará?
- ¿De qué forma el cliente o beneficiario utilizará el producto del proyecto?

## ¿Qué solución basada en Deep Learning queremos implementar?

Queremos implementar un modelo de deep learning, específicamente basado en redes neuronales convolucionales (CNN), para clasificar y detectar la presencia de neumonía en imágenes de rayos X de tórax en pacientes pediátricos. Esta solución tiene como objetivo:

1. Proporcionar un diagnóstico rápido y preciso de la neumonía.
2. Reducir el margen de error en la detección de esta enfermedad.
3. Servir como herramienta de apoyo para radiólogos y pediatras en su labor diagnóstica.

Aunque inicialmente nos enfocamos en las CNN por su eficacia probada en el procesamiento de imágenes médicas, estamos abiertos a explorar y experimentar con arquitecturas más avanzadas de deep learning, como las redes neuronales residuales (ResNet) o las redes densamente conectadas (DenseNet), que han demostrado un rendimiento superior en tareas similares de clasificación de imágenes médicas.

## ¿Qué se hará?

Se desarrollará un proyecto completo de deep learning que abarcará las siguientes etapas:

1. Recopilación y preprocesamiento de datos:
   - Obtención de un conjunto amplio de imágenes de rayos X de tórax de pacientes pediátricos, tanto con neumonía como sin ella.
   - Limpieza y normalización de las imágenes para asegurar una calidad uniforme.
   - Aumento de datos para incrementar la diversidad del conjunto de entrenamiento.

2. Diseño y construcción del modelo:
   - Selección de la arquitectura de red neuronal más adecuada (por ejemplo, CNN, ResNet, DenseNet).
   - Definición de la estructura de capas, funciones de activación y parámetros del modelo.

3. Entrenamiento y validación:
   - División del conjunto de datos en entrenamiento, validación y prueba.
   - Implementación de técnicas de regularización para prevenir el sobreajuste.
   - Ajuste de hiperparámetros para optimizar el rendimiento del modelo.

4. Evaluación del modelo:
   - Medición de métricas clave como precisión, sensibilidad, especificidad y AUC-ROC.
   - Análisis de falsos positivos y falsos negativos para comprender las limitaciones del modelo.


## ¿De qué forma el cliente o beneficiario utilizará el producto del proyecto?

Los principales beneficiarios (instituciones médicas, hospitales, centros de salud, radiólogos y pediatras, etc) utilizarán el producto del proyecto de la siguiente manera:

1. Como herramienta de apoyo diagnóstico: Los profesionales médicos podrán cargar las imágenes de rayos X de tórax de pacientes pediátricos en el sistema, que proporcionará una evaluación rápida sobre la presencia o ausencia de neumonía.

2. Para priorización de casos: En situaciones de alta demanda, el sistema ayudará a identificar y priorizar los casos más urgentes que requieran atención inmediata.

3. Como segunda opinión: El modelo servirá como una "segunda opinión" automatizada, ayudando a los médicos a confirmar sus diagnósticos o alertándoles sobre posibles casos que podrían haber pasado por alto.

4. Para mejorar la eficiencia: Al automatizar parte del proceso de diagnóstico, los profesionales médicos podrán dedicar más tiempo a la atención directa del paciente y a casos más complejos.


Es importante destacar que este sistema no pretende reemplazar el juicio clínico de los profesionales médicos, sino servir como una herramienta de apoyo que mejore la precisión y la eficiencia en el diagnóstico de la neumonía en pacientes pediátricos. El uso de esta tecnología de IA tiene el potencial de salvar vidas al permitir un diagnóstico más rápido y preciso, especialmente en casos donde cada minuto cuenta.

### **1.3. Plan**
---

Puede agregar una lista de actividades con tiempos estimados, un diagrama de Gantt o integrar alguna herramienta de gestión de proyectos para mostrar la planeación del proyecto.

---**INGRESE SU RESPUESTA**---

La propuesta de planeación para el desarollo de este proyecto, se defino ttomando como base los entregables semanales descritos. Por esto, se definió el siguiente diagrama de Gant con las 5 fases más importantes del proyecto que se tendrán en cuenta a lo largo del modulo.

![timeline](../src/MLDS6_Assets/images/Methodology.PNG)

En este momento se va a cargar el dataset desde el repositorio de Kaggle. El dataset que se usará es público, por lo que no habrán problemas con el acceso a los datos ni se hará un requerimiento de credenciales

### **2.1. Origen**
---

- ¿De dónde vienen los datos?
- ¿Se usa alguna herramienta o proceso para la descarga de la información?
- ¿Qué tipo de datos estamos manejando?

Finalmente, el dataset utilizado para este proyecto proviene del Guangzhou Women and Children’s Medical Center y cuenta con un total de 5,856 imágenes de rayos X de tórax en formato JPEG, organizadas en tres categorías: neumonía viral, neumonía bacterial y normal. Además, estas imágenes se tomaron de pacientes pediátricos de entre uno y cinco años, como parte de su atención clínica rutinaria. El conjunto de datos se divide en carpetas de entrenamiento, prueba y validación, con subcarpetas que clasifican las imágenes según su categoría. Este dataset se encuentra disponible en la librería de Kaggle y es posible acceder al mismo mediante el siguiente enlace https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

La extracción de estos datos se hizo a través de la API de Kaggle