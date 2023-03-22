from confluent_kafka import Consumer, KafkaError
import json

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
}

# Inisialisasi 2 consumer
consumer1 = Consumer({
    **conf,
    'auto.offset.reset': 'earliest'
})
consumer2 = Consumer({
    **conf,
    'auto.offset.reset': 'earliest'
})

# Subscribe ke topik yang memiliki 2 partisi
consumer1.subscribe(['coba'])
consumer2.subscribe(['coba'])

try:
    while True:
        # 
        msg1 = consumer1.poll(1.0)
        msg2 = consumer2.poll(1.0)

        # Displays messages received by each consumer
        if msg1 is not None:
            print('Consumer 1: {}'.format(msg1.value().decode('utf-8')))
            print('\n')
            with open("msg1.json", "a") as json_file1:
               json.dump(msg1.value().decode('utf-8'), json_file1)
               json_file1.write('\n')
        if msg2 is not None:
            print('Consumer 2: {}'.format(msg2.value().decode('utf-8')))
            print('\n')
            with open("msg2.json", "a") as json_file2:
                json.dump(msg2.value().decode('utf-8'), json_file2)
                json_file2.write('\n')
except KeyboardInterrupt:
    pass

# Menutup koneksi consumer
consumer1.close()
consumer2.close()
