#!/usr/bin/env python  
# -*- coding: <utf-8> -*-                                                                 
import os                                                                               
import datetime    

import RPi.GPIO as GPIO
import time

channel = 21

# GPIO setup^M
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on^M


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off^M
                                                                     


sensors = {'t1': '28-0314977974ee','t2':'28-03189779c4c9'}                                                            
                                                                                        
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
                                                                                        
def read1():                                                                    
    loc ='/sys/bus/w1/devices/28-0314977974ee/w1_slave'
    tfile= open(loc)                                                                    
    text= tfile.read()                                                                  
    secondline= text.split("\n")[1]                                                     
    tdata = secondline.split(" ")[9]                                                    
    temp = float(tdata[2:])                                                             
    cel = temp/1000                                                                     
    return cel                                                                          
def read2():                                                                    
    loc ='/sys/bus/w1/devices/28-03189779c4c9/w1_slave'
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
    while True:                                                                         
        now=datetime.datetime.now()                                                     
        if read(serialNum) != None:                                                     
            print (now)                                                                 
            print("Trenutna temperatura je : %0.3f C " % read(serialNum))               
                                                                                        

def loop2(sensors):                                                                    
    vklop = ""
    while True:                                                                         
        now=datetime.datetime.now()                                            
        if vklopljeno():
            vklop = "Vklopljeno"
        else:
            vklop = "Izklopljeno"
        if read1() != 0:                                                     
            print (now)                                                                 
            print("T1  => "+ str(read1()) + ";  T2 => " +str(read2()) + " C  " +vklop )


def vklopljeno():
    t1 = read1() # peč
    t2 = read2() # zalogovnik
    if (t1 - t2) > 3:
        motor_on(channel)
        return True
    else:
        motor_off(channel)
        return False


def kill():                                                                             
    quit()                                                                              
                                                                                        
                                                                                        
if __name__ == '__main__':                                                              
    try:                                                                                
        #serialNum = sensor()                                                            
        loop2(sensors)                                                                 
    except KeyboardInterrupt:   
        GPIO.cleanup()                                                        
        kill()                                                                          
                                                                                    