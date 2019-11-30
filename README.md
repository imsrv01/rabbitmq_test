# rabbitmq_test

Pre-requisites:

Get URL for test rabbitMQ instance. Free instance can be created from below website..

https://customer.cloudamqp.com/instance

clone https://github.com/imsrv01/rabbitmq_test.git

cd rabbitmq_test

export CLOUDAMQP_URL='<URL>'

pip3 install pika

python3 producer.py

python3 consumer.py

python3 consumer_2.py


  

