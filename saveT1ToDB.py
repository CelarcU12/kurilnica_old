import db
import getT1

import time
import datetime

def saveEverySecond():
    while True:
        t1= getT1.getT1()
        t2 = getT1.getT2()
        db.saveTempToDB("T1", t1)
        db.saveTempToDB("T2", t2)
        time.sleep(60)
        print("Save success!!")
saveEverySecond()