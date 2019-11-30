import pika, os, logging
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)
# URL - '<protocol>://<user>:<password>@<Rabbit MQ host URL>/<virtualHost>'
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')
print(url)
params = pika.URLParameters(url)
params.socket_timeout = 15

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='testq', durable=True) # Declare a queue, creates queue if does not exists.

# send a message
for i in range(10):
    channel.basic_publish(exchange='', routing_key='testq', body='HELLO')
    print ("[x] Message sent to consumer")

connection.close()
