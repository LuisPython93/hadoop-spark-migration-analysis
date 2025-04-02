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

Ejecuta el script con PySpark con el siguiente comando:

exec(open("tarea3_practica.py").read())

¡Listo! Ya puedes analizar los datos en Apache Spark. 🚀🔥

Requisitos
Antes de ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos:

1. Configuración del Entorno

    Una máquina virtual configurada con Hadoop y Spark.

    Acceso a la máquina virtual mediante SSH (por ejemplo, con PuTTY).

    Usuario y contraseña de la máquina virtual:

        Usuario: vboxuser

        Contraseña: bigdata

    Configurar el usuario hadoop:

sudo useradd -m -d /home/hadoop -s /bin/bash hadoop
sudo passwd hadoop  # Asigna una contraseña al usuario
Luego, cambiar a este usuario antes de ejecutar comandos relacionados con Hadoop:
su - hadoop

2. Instalación de Dependencias
   Python 3 y pip instalados en la máquina virtual.
   Instalación de la librería de Kafka para Python:

pip install kafka-python

   Descargar y configurar Apache Kafka:

wget https://downloads.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz
tar -xzf kafka_2.13-3.9.0.tgz
sudo mv kafka_2.13-3.9.0 /opt/Kafka

   Iniciar los servicios de ZooKeeper y Kafka:

sudo /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties &
sudo /opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties &

   Crear un topic en Kafka:

    /opt/Kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic sensor_data

3. Ejecución del Proyecto

   Productor Kafka:
   Crear y ejecutar el script kafka_producer.py en Python para enviar datos simulados al topic de Kafka.

    Consumidor con Spark Streaming:
    Ejecutar el script spark_streaming_consumer.py con spark-submit, asegurándose de incluir las dependencias de Kafka:

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.9.0 spark_streaming_consumer.py

En caso de error, probar con:

    spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 spark_streaming_consumer.py

4. Visualización de Resultados

   Consola de Spark UI:
   Para monitorear los procesos en ejecución, acceder a:

    http://your-server-ip:4040

    (Reemplazar your-server-ip con la IP de la máquina virtual).

5. Finalización del Proyecto

    Detener la ejecución de los scripts con CTRL+C en la terminal.


