# encoding:utf-8
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
print '[*] Waiting for message. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print body

channel.basic_consume(callback, queue='hello', no_ack=True)
channel.start_consuming()
