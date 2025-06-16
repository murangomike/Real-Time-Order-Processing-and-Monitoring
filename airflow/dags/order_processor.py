from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from kafka import KafkaConsumer
import json

def process_orders():
    consumer = KafkaConsumer(
        'orders',
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest',
        group_id='order-group'
    )
    for message in consumer:
        order = json.loads(message.value.decode('utf-8'))
        print(f"Processed order: {order}")
        # Insert into Azure SQL / blob (omitted for brevity)

with DAG('order_processing',
         start_date=datetime(2023, 1, 1),
         schedule_interval='@hourly',
         catchup=False) as dag:

    task = PythonOperator(
        task_id='consume_kafka_orders',
        python_callable=process_orders
    )