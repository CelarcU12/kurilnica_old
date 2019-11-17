import time
import paho.mqtt.client as mqtt
from tempSensor import read1

def on_connect(client,userdata,flags,rc):
    print("Connected whit code "+str(rc))
    client.subscribe("Temperatura v sobi/#")

def on_message(client,userdata,msg):
    print(msg.topic + "  " +str(msg.payload))

def getTemp():
    return read1()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("jzqrywks","F0amg0frVoHE") 
client.connect("postman.cloudmqtt.com", 13052, 60 )

client.loop_start()

time.sleep(1)
while True:
    client.publish("Temperatura v sobi ", getTemp())
    time.sleep(30)

client.loop_stop()
client.disconnect()
