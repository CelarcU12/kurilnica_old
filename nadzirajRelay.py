from relay import on, off, getStatus
from t1 import getT1,getT2
import time
import db

def nadziraj():
    if (checkTemp() and not getStatus()):
        try:
            on()
            print("VKLOP")
            db.saveRelayStatus("PEČ","ON",getT1(), getT2())
        except:
            raise Exception("Napaka v nadziraj -> relay.on()")
    elif (not checkTemp() and getStatus()):
        try:
            off()
            print("IZKLOP")
            db.saveRelayStatus("PEČ","OFF",getT1(), getT2())
        except:
            raise Exception("Napa ka v nadziraj -> relay.off()")
    else:
        print("Ni sprememb!")

def checkTemp():
    print("Check temp   peč:"+ str(getT1())+"   zalogovnik: "+ str(getT2()))
    try:

        if (getT1() > getT2()):
            print( "T1 > T2")
            return True
        else:
            print("T1 < T2")
            return False
    except:
        print("exception checkTemp()")
        return False
     

while True:
    nadziraj()
    time.sleep(3)