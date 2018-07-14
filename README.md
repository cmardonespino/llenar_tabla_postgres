# Llenado de tablas PostgreSQL
El siguiente miniproyecto escrito en python 2.7 consiste en un script que permite llenar tablas postgreSQL que, copiando las columnas y filas de una planilla excel, los inserta en la base de datos.

Miniproyecto complementario a mi proyecto de título.
## Requisitos
Se necesitan tener instalado python 2.7+ junto al administrador de paquetes pip. Las dependencias instaladas necesarias e instaladas con pip son las siguientes dependencias:
* pandas
* psycopg2

## HOWTO
Modificar los siguentes parámetros del código fuente [llenar_tabla_bonos_fonasa.py](llenar_tabla_bonos_fonasa.py)
* `conn`: Agregar nombre de la base de datos, nombre de usuario, password y el host de la base de datos
* `path_excel`: De acuerdo al excel que se requiera insertar en la base de datos, modificar el nombre con extención .xlsx
* `df`: Modificar sheet_name, que corresponde a la hoja que se quiera insertar del excel seleccionado
* Modificar ciclo for de acuerdo a los datos que se requiera insertar
* Ejecutar `python llenar_tablas_bonos_fonasa.py`