import pika, os

url = "amqps://wjcfejbo:GkicwopvVNrItsoNk9If0JaUI-w2kAiZ@woodpecker.rmq.cloudamqp.com/wjcfejbo"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='ac5')
channel.basic_publish(exchange='',
                      routing_key='ac5',
                      body='Hello World!')

connection.close()