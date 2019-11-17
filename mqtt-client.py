import time
import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
    print("Connected whit code "+str(rc))
    client.subscribe("Temperatura v sobi/#")

def on_message(client,userdata,msg):
    if msg.payload == "ON":
        print("Lučka prižgi se")
    print("ON")
    print(msg.topic + "  " +str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("jzqrywks","F0amg0frVoHE") 
client.connect("postman.cloudmqtt.com", 13052, 60 )

client.loop_forever()
