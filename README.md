# web-scraping-birds
------------
## Descripción
Este proyecto hace uso de web scarping para obtener la información taxonómica de aves de diferentes países de la página web https://avibase.bsc-eoc.org/ y generando un dataset.

Este código se ha realizado para la practica 1 de Tipología y ciclo de vida de los datos. Perteneciente al Máster en Ciencia de Datos de la universidad Oberta de Catalunya.

## Run
```
python src/main.py
```
Parametros opcionales:
|  Parametro Largo |Parametro Corto   |  Descripción | 
| ------------ | ------------ | ------------ | 
|   --region | -r | Establecer la region  | 
|  --filename | -f | Nombre del fichero   |
|  --limit | -l | Numero de registros a extraer  |

```
  python src/main.py --region US --filename US.csv --limit 100
  python src/main.py -r US -f US.csv -limit 100
```
La configuración por defecto es extraer 5 registros de aves de España y generar el fichero en **csv/ES_birds.csv**

## Miembros del equipo

La actividad se ha realizado de manera individual
