## cs361microservice
Contains the code for my microservices as well as for a test program to show it works.
My microservice is a webscaper that scrapes the web to find the graviation constant of the different planets in our solar system, plus the sun. 

# Comunication Contract
The microservice uses rabbitMq and pika in order to comunicate. In order to receive the gravitational constant of a planet, you must send the name of the planet as a string('Mars', 
'Pluto', etc,) over the queue 'cs361planets'. After scraping the web the microservice will return the gravitational constant as a string over the the queue 'cs361gravity'. Below is an example call to contact my microservice. Below that is a SML sequence diagram.

<img width="401" alt="image" src="https://user-images.githubusercontent.com/91440373/199132489-345fde7a-0196-46a7-821b-38cb9c30cbba.png">

![image](https://user-images.githubusercontent.com/91440373/199131584-12f1ee9f-e50e-42eb-8caf-7bc7f6dff0d1.png)

