import pika, sys, os

def sendPlanet(aPlanet):
    """Sends the planet over the cs361planets que"""
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()


    channel.queue_declare(queue='cs361planets')

    channel.basic_publish(exchange='',
                          routing_key='cs361planets',
                          body=aPlanet)
    print(" [x] Sent "+aPlanet)
    connection.close()


sendPlanet('Mars')
    
import pika, sys, os

def main():
    """waits to recieve the gravity over the cs361 gravity queue"""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='cs361gravity')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='cs361gravity', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)