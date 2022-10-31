import requests
from bs4 import BeautifulSoup
import pika

def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    #declare que to recieve messages
    channel.queue_declare(queue='cs361planets')



    def callback(ch, method, properties, body):
        print(" [x] Received " + body.decode())
        gravities = getPlanetDict()
        planet = body.decode()
        
        sendGravity(str(gravities[planet]))



    channel.basic_consume(queue='cs361planets',
                          auto_ack=True,
                          on_message_callback=callback)

    channel.basic_consume(queue='cs361planets', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

def getPlanetDict():
    soup = getPlanetHTML()

    gravs = {}
    i = 2
    while i < 13:
        if i < 10:
            theInt = '0' + str(i)
        else:
            theInt = str(i)

        aPlanet = soup.find(id="ctl00_ctl00_Content_gvInfos_ctl"+theInt+"_Label2")
        aGravity = soup.find(id="ctl00_ctl00_Content_gvInfos_ctl"+theInt+"_Label3") 
        gravs[aPlanet.text] = aGravity.text
        i += 1
    return gravs

def getPlanetHTML():
    URL = "https://www.smartconversion.com/otherInfo/gravity_of_planets_and_the_sun.aspx"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def sendGravity(aGravity):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()



    channel.queue_declare(queue='cs361gravity')

    channel.basic_publish(exchange='',
                          routing_key='cs361gravity',
                          body=aGravity)
    print(" [x] Sent "+aGravity)
    connection.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)