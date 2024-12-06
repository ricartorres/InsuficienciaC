# Diccionario de datos

## Base de datos 1: Flight Delays Raw Data

**Descripción:** Esta base contiene los datos originales relacionados con vuelos y sus posibles retrasos. Se obtienen directamente de los archivos CSV en la carpeta `./flight_delays/raw`.

| Variable                  | Descripción                                                                 | Tipo de dato | Rango/Valores posibles               | Fuente de datos                  |
|---------------------------|-----------------------------------------------------------------------------|-------------|--------------------------------------|----------------------------------|
| `Year`                   | Año en que se realizó el vuelo                                              | Entero      | 2018-2022                            | Kaggle                           |
| `Quarter`                | Trimestre del año del vuelo                                                 | Entero      | 1 (Ene-Mar), 2 (Abr-Jun), etc.       | Kaggle                           |
| `Month`                  | Mes del año del vuelo                                                      | Entero      | 1 (Ene) - 12 (Dic)                   | Kaggle                           |
| `DayofMonth`             | Día del mes del vuelo                                                      | Entero      | 1-31                                 | Kaggle                           |
| `FlightDate`             | Fecha del vuelo                                                            | Fecha       | Formato `YYYY-MM-DD`                 | Kaggle                           |
| `DepartureDelay`         | Retraso en minutos en la salida del vuelo                                  | Flotante    | Valores negativos (adelanto) o >= 0  | Kaggle                           |
| `ArrivalDelay`           | Retraso en minutos en la llegada del vuelo                                 | Flotante    | Valores negativos (adelanto) o >= 0  | Kaggle                           |
| `Marketing_Airline_Network` | Aerolínea que promociona el vuelo                                          | Texto       | Códigos IATA como UA, DL, AA         | Kaggle                           |
| `Tail_Number`            | Número de cola del avión                                                   | Texto       | Alfanumérico                         | Kaggle                           |
| `Departure_Airport`      | Código IATA del aeropuerto de salida                                       | Texto       | Alfanumérico                         | Kaggle                           |
| `Arrival_Airport`        | Código IATA del aeropuerto de llegada                                      | Texto       | Alfanumérico                         | Kaggle                           |
| `Unnamed: 119`           | Columna vacía sin datos útiles (por limpiar)                               | Texto       | Vacío                                | Kaggle                           |

---

