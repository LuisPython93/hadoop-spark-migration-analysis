import csv
import json
import time
from kafka import KafkaProducer

# Ruta al archivo original
csv_file_path = '/home/vboxuser/rows.csv'

# Inicializa el productor
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Limpieza de datos
        if 'Indefinido' in row:
            del row['Indefinido']

        # Convertir columnas numéricas eliminando comas y convirtiendo a enteros
        for col in ['Femenino', 'Masculino', 'Total']:
            row[col] = int(row[col].replace(',', '')) if row[col] else 0

        # Separa latitud y longitud
        if 'Latitud - Longitud' in row and row['Latitud - Longitud']:
            try:
                lat, lon = row['Latitud - Longitud'].split(',')
                row['Latitud'] = float(lat.strip())
                row['Longitud'] = float(lon.strip())
            except ValueError:
                row['Latitud'] = None
                row['Longitud'] = None
        
        # Eliminar la columna original 'Latitud - Longitud'
        row.pop('Latitud - Longitud', None)

        # Enviar mensaje limpio a Kafka
        producer.send('sensor_data_analisis', value=row)
        print(f"Enviado a Kafka: {row}")
        time.sleep(0.5)  # Ajusta la velocidad de envío

producer.flush()

