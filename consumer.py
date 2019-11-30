import pika, os, time

def pdf_process_function(msg):
  print(" PDF processing")
  print(" [x] Received " + str(msg))

  time.sleep(5) # delays for 5 seconds
  print(" PDF processing finished");
  return;

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='testq') # Declare a queue

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  pdf_process_function(body)

# This tells RabbitMQ not to give more than one message to a worker at a time.
# Or, in other words, don't dispatch a new message to a worker until it has processed and acknowledged the previous one. Instead, it will dispatch it to the next worker that is not still busy.
channel.basic_qos(prefetch_count=1)

# set up subscription on the queue
channel.basic_consume('testq',
  callback,
  auto_ack=True)

# start consuming (blocks)
channel.start_consuming()
connection.close()
