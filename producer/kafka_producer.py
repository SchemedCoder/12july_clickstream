import json
import time

from kafka import KafkaProducer

from producer.generate_events import generate_event

from configs.config import *

producer = KafkaProducer(

    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,

    value_serializer=lambda v: json.dumps(v).encode("utf-8")

)

print("Starting Clickstream Producer...")

while True:

    event = generate_event()

    producer.send(CLICKSTREAM_TOPIC, event)

    print(event)

    time.sleep(1 / EVENTS_PER_SECOND)
