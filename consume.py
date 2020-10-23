import pika, os

url = "amqps://wjcfejbo:GkicwopvVNrItsoNk9If0JaUI-w2kAiZ@woodpecker.rmq.cloudamqp.com/wjcfejbo"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue="ac5")

def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))

channel.basic_consume("ac5", callback, auto_ack=True)

print(" [*] Waiting for messages:")
channel.start_consuming()
connection.close()