# hadoop-spark-migration-analysis

🔍 **Análisis de datos de migración utilizando Apache Hadoop, Apache Spark y Kafka**  

Este proyecto incluye **scripts en Python** para el procesamiento de datos con **PySpark**, así como la configuración necesaria para trabajar con **HDFS**.  

## 📥 Descarga del Dataset

Para ejecutar el análisis, descarga el conjunto de datos desde el siguiente enlace:  

Descargar dataset: https://www.datos.gov.co/Estad-sticas-Nacionales/Entrada-de-Venezolanos-a-Colombia-por-a-o-2012-201/p7hq-8vsm 

Si deseas descargarlo directamente desde la terminal de **Linux**, usa el siguiente comando:  

```bash
wget https://www.datos.gov.co/api/views/96sh-4v8d/rows.csv


📂 Cargar el Dataset en HDFS

Una vez descargado, colócalo en HDFS con este comando:
hdfs dfs -put /home/hadoop/rows.csv /Ruta_del_Proyecto

🚀 Ejecución del Script

Puedes ejecutar el análisis con el script tarea3_practica.py o editarlo si prefieres.

Ejecuta el script con PySpark:

¡Listo! Ya puedes analizar los datos en Apache Spark. 🚀🔥

