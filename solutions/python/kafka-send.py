from kafka import KafkaProducer
import json
from datetime import datetime

def send_to_kafka(kafka_server, kafka_topic, incident):
    producer = KafkaProducer(bootstrap_servers=kafka_server)
    producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    msg = {'id': incident[id],
           'body': incident,
           'messageType': 'IncidentReportedEvent',
           'invokingService': 'IncidentProcessService',
           'timestamp': datetime.now().timestamp(),
           
           }
    producer.send(kafka_topic, msg)
