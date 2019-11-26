import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

kafka_server = os.environ.get('KAFKA_SERVER', 'kafka-cluster-kafka-bootstrap.emergency-response-demo.svc.cluster.local:9092')
topic_incident_event = os.environ.get('TOPIC_INCIDENT_EVENT', 'topic-incident-event')
topic_incident_command = os.environ.get('TOPIC_INCIDENT_COMMAND', 'topic-incident-command')

rest_endpoint_for_update = '/incident/incidents/'