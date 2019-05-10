#!/usr/bin/env python
import pika
import time
import fib_pb2

def fib_calculate(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_calculate(n-1) + fib_calculate(n-2)
#for localhost
#connection = pika.BlockingConnection(pika.ConnectionParameters(
#        host='localhost'))

#for the specified server
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='149.165.158.122'))#host='queueserver')) #149.165.158.122

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    #print " [x] Received %r" % (body,)
    #time.sleep( body.count('.') )
    #print " [x] Done"
    fiblist = fib_pb2.FibList()
    fiblist.ParseFromString(body)
    for fib  in fiblist.fibs:
        number=int(fib.n)
        #print number
        value=fib_calculate(number)
        print "fib(%s):\t %s\n" %(number,value)
        ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()

