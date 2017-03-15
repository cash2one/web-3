#encoding:utf-8
import sys
import pika
#help(pika)
#print type(pika)
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.queue_declare(queue='hello')
if len(sys.argv)<2:
	print 'message is empty!'
	sys.exit(0)
message=sys.argv[1]
channel.basic_publish(exchange='',routing_key='hello',body=message)
print '[x] sent:"'+message+'"\n'
connection.close()