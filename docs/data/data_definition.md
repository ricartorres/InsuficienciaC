# Definición de los datos

## Origen de los datos

### Especificación de la fuente
- **Fuente:** Los datos provienen del dataset público alojado en la plataforma **Kaggle** bajo el título *Flight Delay Dataset 2018-2022*.
- **URL:** [Flight Delay Dataset 2018-2022](https://www.kaggle.com/datasets/robikscube/flight-delay-dataset-20182022)
- **Método de obtención:** Descargado mediante la API de Kaggle utilizando el comando `kaggle datasets download`.

---

## Especificación de los scripts para la carga de datos

### Script principal
- **Archivo:** `main.py`
- **Descripción:**
  - Configura las credenciales de la API de Kaggle (`kaggle.json`).
  - Descarga y descomprime el dataset desde Kaggle en la carpeta `./flight_delays`.
  - Lee las primeras filas de los archivos CSV en la subcarpeta `raw` del dataset descargado.

### Funciones incluidas
1. **`show_first_rows_of_files`**
   - **Entrada:**
     - `base_path`: Ruta base donde se encuentran los datos.
     - `subfolder`: Subcarpeta dentro de `base_path` que contiene los archivos.
     - `num_files`: Número máximo de archivos a leer.
     - `num_rows`: Número de filas a mostrar por archivo.
   - **Propósito:** Lee y muestra las primeras filas de los archivos CSV.
   - **Salida:** Datos impresos en consola.

---

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

#### Ubicación de los archivos de origen
- **Ruta:** `./flight_delays/raw`
- **Estructura:** 
  La carpeta contiene múltiples archivos CSV organizados por años y meses, como `Flights_2020_10.csv`.

#### Estructura de los archivos de origen
- **Formato:** CSV (Comma Separated Values).
- **Columnas principales:**
  - Información temporal: `Year`, `Quarter`, `Month`, `DayofMonth`, `DayOfWeek`, `FlightDate`.
  - Datos del vuelo: `Marketing_Airline_Network`, `Tail_Number`, `Departure_Airport`, `Arrival_Airport`.
  - Indicadores de retrasos: `DepartureDelay`, `ArrivalDelay`.
  - Información adicional: Más de 100 columnas relacionadas con divisiones de vuelos y tiempos de operación.

#### Procedimientos de transformación y limpieza
1. **Identificación de valores nulos:** Muchas columnas contienen valores nulos (`NaN`) que requieren procesamiento.
2. **Filtrado inicial:** Mostrar únicamente las primeras filas como exploración preliminar.
3. **Futuro procesamiento:** Los datos pueden necesitar agregación, filtrado o normalización dependiendo del análisis.

---

### Base de datos de destino

#### Base de datos de destino para los datos
- **Ruta inicial:** `./flight_delays/processed` (a definir en implementaciones futuras).
- **Formato:** CSV procesados o una base de datos relacional como SQLite, PostgreSQL o MySQL, dependiendo de las necesidades analíticas.

#### Estructura de la base de datos de destino
- **Tabla principal:** `Flight_Delays`
  - **Columnas principales:**
    - Identificadores: `FlightID`, `Airline`, `FlightDate`.
    - Retrasos: `DepartureDelay`, `ArrivalDelay`.
    - Tiempos de operación: `GateDepartureTime`, `GateArrivalTime`.

#### Procedimientos de carga y transformación
1. **Carga inicial:** Los archivos CSV se leerán y procesarán con librerías como `pandas` para consolidación en la base de datos.
2. **Transformaciones:** 
   - Limpieza de valores nulos.
   - Normalización de fechas y horas.
   - Generación de métricas como tiempo total de retraso.
3. **Exportación:** Los datos transformados se almacenarán en la base de datos de destino o exportarán nuevamente a CSV procesados.

---

Esta estructura garantiza un flujo claro desde la adquisición hasta la transformación y almacenamiento de los datos.