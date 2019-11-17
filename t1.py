#!/usr/bin/env python



def getT1():
    loc ='/sys/bus/w1/devices/28-0314977974ee/w1_slave'
    tfile= open(loc)
    text= tfile.read()
    secondline= text.split("\n")[1]
    tdata = secondline.split(" ")[9]
    temp = float(tdata[2:])
    cel = temp/1000
    return cel

def getT2():                                                                    
    loc ='/sys/bus/w1/devices/28-03189779c4c9/w1_slave'
    tfile= open(loc)                                                                    
    text= tfile.read()                                                                  
    secondline= text.split("\n")[1]                                                     
    tdata = secondline.split(" ")[9]                                                    
    temp = float(tdata[2:])                                                             
    cel = temp/1000                                                                     
    return cel
