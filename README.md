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
