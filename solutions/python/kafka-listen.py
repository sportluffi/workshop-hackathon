from kafka import KafkaConsumer
from config import *
import requests
import json

def main(kafka_server, kafka_topic, rest_endpoint):
    consumer = KafkaConsumer(bootstrap_servers=kafka_server,
                            auto_offset_reset='earliest',
                            value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    consumer.subscribe([kafka_topic])
    for msg in consumer:
        print (msg)
        body = msg[body]
        requests.put(rest_endpoint+'/'+msg[id], json=body)

if __name__ == '__main__':
    main(kafka_server, topic_incident_command, rest_endpoint_for_update)
    
