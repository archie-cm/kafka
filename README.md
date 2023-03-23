# Streaming Data - Confluent Kafka

Ingest data from url API data source and publish it to a Kafka topic for consumer application to subscribe and consume messages.

## Install Confluent Kafka
Using Docker compose, we can install the entire Confluent Platform or individual components.

+ Docker version 1.11 or later is installed and running.
+ Docker Compose is installed. Docker Compose is installed by default with Docker for Mac.
+ Docker memory is allocated minimally at 8 GB. When using Docker Desktop for Mac, the default Docker memory allocation is 2 GB. You can change the default allocation to 8 GB in Docker > Preferences > Advanced.

### Run Docker Compose 
```docker
docker-compose up
```
    
### Confluent Control Center    
Confluent Control Center is a web-based tool for managing and monitoring Apache Kafka®

    Go to http://localhost:9021/ which is the default port that the Webserver will be listening to.

![image](https://user-images.githubusercontent.com/85284506/207524846-179475b7-8bf8-406a-b6ba-4523c5d88304.png)

Confluent Control Center is a web-based user interface that allows developers and operators to manage and monitor Apache Kafka clusters, including checking cluster health, observing and controlling messages, topics, and Schema Registry. It can also be used to develop and run ksqlDB queries.

 + Broker
 + Topics
 + Connect
 + KSQL
 + Consumer
 + Replicator
 + Cluster Settings


## Python Code

### Create Python Virtual Environment
```python
python3 -m venv [env_name]
```

Activate virtual environment with command `source [env_name]/bin/activate`
    

### Creates a record and publishes it to the broker

```python
python[version] kafka_producer.py
```

Example:

```python
python3 kafka_producer.py
```

### Consumes records from the topics

```python
python[version] kafka_consumer.py
```

Example:

```python
python3 kafka_consumer.py
```
Result: data.json

### Create Topic with Partition

1. Klik menu Topic and add a topic
![Screenshot (156)](https://user-images.githubusercontent.com/108534539/227071068-65424f97-48ee-425c-8d45-fbb850eb71c7.png)

2. Fill name of topic and number of partition
![Screenshot (157)](https://user-images.githubusercontent.com/108534539/227071259-6c306d00-82f1-4e7f-a698-7b019606ed80.png)

### Creates a record and publishes it to topic with partitions

1. Fill name of topic in kafka_producer.py
```python
python[version] kafka_producer.py
```

Example:

```python
python3 kafka_producer.py
```
![Screenshot (160)](https://user-images.githubusercontent.com/108534539/227071634-d0c658bf-8fd2-45c3-9aae-aa592e891344.png)

![Screenshot (161)](https://user-images.githubusercontent.com/108534539/227071858-6d232793-9184-4690-ab0e-43f10f0f2ef5.png)


2. Fill name of topic in kafka_consumer_group.py
### Consumes records from the topics

```python
python[version] kafka_consumer_group.py
```

Example:

```python
python3 kafka_consumer_group.py
```
![Screenshot (159)](https://user-images.githubusercontent.com/108534539/227071776-e1f41309-b707-44b0-812f-b7f53ba998e1.png)

Result: msg1.json and msg2.json
