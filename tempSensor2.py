#!/usr/bin/env python
import os
import datetime
import RPi.GPIO as GPIO
import time

channel = 21

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off




def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20

def read(serialNum):
    loc ='/sys/bus/w1/devices/'+serialNum+'/w1_slave'
    tfile= open(loc)
    text= tfile.read()
    secondline= text.split("\n")[1]
    tdata = secondline.split(" ")[9]
    temp = float(tdata[2:])
    cel = temp/1000
    return cel


now=datetime.datetime.now()
print(now)
def loop(serialNum):
    chanel1= 21
    try:
        while True:
            now=datetime.datetime.now()
            if read(serialNum) != None:
                print (now)
                print("Trenutna temperatura je : %0.3f C " % read(serialNum))
                if read(serialNum) > 30:
                    motor_on(chanel1)
                else:
                    motor_off(chanel1)
                    
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
            

def kill():
    quit()


if __name__ == '__main__':
    try:
        serialNum = sensor()
        loop(serialNum)
    except KeyboardInterrupt:
        kill()
