#!/usr/bin/env python
import pika
import sys
import fib_pb2
#for localhost
#connection = pika.BlockingConnection(pika.ConnectionParameters(
#        host='localhost'))
#for the specified queue server
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='149.165.158.122')) #149.165.158.122

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

#message = ' '.join(sys.argv[1:]) or "Hello World!"
#channel.basic_publish(exchange='',
#                      routing_key='task_queue',
#                      body=message,
#                      properties=pika.BasicProperties(
#                         delivery_mode = 2, # make message persistent
#                      ))
#print " [x] Sent %r" % (message,)
#connection.close()

while True:
    try:
        n = raw_input("Fib of what number (0 to exit)? > ")
        n = int(n)
    except ValueError:
        print "Enter an integer"
        n = 0
    except EOFError:
        n = 0

    if  n == 0 :
        print "Done, exiting..."
        break

    fiblist = fib_pb2.FibList()
    fib = fiblist.fibs.add()
    try:
        fib.n = n
    except TypeError:
        fib.n = 0
    channel.basic_publish(exchange='',
                           routing_key='task_queue',
                           body=fiblist.SerializeToString(),
                           properties=pika.BasicProperties(delivery_mode = 2))
    print "Sent.."
connection.close()
sys.exit(0)
