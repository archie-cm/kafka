from confluent_kafka import Producer
from faker import Faker
import json
import time
import logging
import random
import requests

url = 'https://dummyjson.com/users'
response = requests.get(url)
data = response.json()

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

####################
p=Producer({'bootstrap.servers':'localhost:9092'})
print('Kafka Producer has been initiated...')
#####################
def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)
        
#####################
topic = 'user'
def main():
    for user in data['users']:
        p.produce(topic, json.dumps(user).encode('utf-8'), callback=receipt)

        p.poll(1)
        p.flush()
        time.sleep(3)
        
if __name__ == '__main__':
    main()