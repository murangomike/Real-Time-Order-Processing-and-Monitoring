from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_order():
    order = {"id": 1, "item": "Laptop", "quantity": 1}
    producer.send('orders', json.dumps(order).encode('utf-8'))

if __name__ == "__main__":
    while True:
        send_order()
        time.sleep(5)