from confluent_kafka import Producer
from client import read_config, topic
import requests
import time
import os
from dotenv import load_dotenv


load_dotenv()
config = read_config()
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')


cities = [
    ("Amsterdam", "NL"),
    ("Seoul", "KR"),
    ("Rio de Janeiro", "BR"),
    ("Nairobi", "KE"),
    ("Vancouver", "CA"),
    ("Bangkok", "TH"),
    ("Reykjavik", "IS")
]

def produce_weather(city, code):
  producer = Producer(config)

  key = "key2"
  value = "value2"
  producer.produce(topic, key=key, value=value)
  print(f"Produced message to topic {topic}: key = {key:12} value = {value:12}")

  producer.flush()

while True:
  for city, code in cities:
    weather = produce_weather(city, code)