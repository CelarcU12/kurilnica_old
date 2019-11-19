from relay import on, off, getStatus
from t1 import getT1,getT2
import time
import requests
import db

from checkRelayStatus import checkStatus

import logging
logging.basicConfig(filename='Documents/project/log/nadzirajRelayApi.log', format='%(asctime)s  - %(name)s  - %(levelname)s  - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


url= "http://192.168.0.121:5000"
urlOn=url+"/relay/on"
urlOff=url+"/relay/off"
def nadziraj():
    if (checkTemp() and not checkStatus()):
        try:
            response = requests.get(urlOn)
            logging.info("VKLOP")
            db.saveRelayStatus("PEČ","ON",getT1(), getT2())
        except:
            raise Exception("Napaka v nadziraj -> relay.on()")
    elif (not checkTemp() and checkStatus()):
        try:
            response = requests.get(urlOff)
            logging.info("IZKLOP")
            db.saveRelayStatus("PEČ","OFF",getT1(), getT2())
        except:
            raise Exception("Napa ka v nadziraj -> relay.off()")
    else:
        logging.info("Ni sprememb!")

def checkTemp():
    logging.info("Check temp   peč:"+ str(getT1())+"   zalogovnik: "+ str(getT2()))
    try:

        if (getT1() > getT2()):
            logging.info( "T1 > T2")
            return True
        else:
            logging.info("T1 < T2")
            return False
    except:
        logging.info("exception checkTemp()")
        return False

     

while True:
    if checkStatus():
        logging.info("Status ON")
    else:
        logging.info("Status OFF")
    nadziraj()
    time.sleep(3)


