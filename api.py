import markdown
import json

import os
from flask import Flask, escape, request,jsonify,Response
import sys

import random
import datetime

import db

from tempClass import Temp
from relayClass import Relay
from t1 import getT1,getT2

from relay import getStatus, on, off

import logging
logging.basicConfig(filename='~/Documents/project/log/api.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

app = Flask(__name__)

@app.route('/')
def hello():
    '''dokumentcija '''
    logging.info(" domov ")
    with open(os.path.dirname(app.root_path) + '/project/README.md', 'r') as md_file:
        content = md_file.read()
        return markdown.markdown(content)


@app.route('/devices', methods=['GET','POST'])
def getDevices():
    content = request.json
    logging.info(" devices ")
    return jsonify({"devices":"t1,t2"})

@app.route('/devices/<device_id>', methods=['GET','POST'])
def getData(device_id):
    content = request.json
    logging.info('device/'+device_id)
    if device_id == 't1':
        return jsonify({device_id:getT1()})
    return jsonify({device_id:random.randint(1,100)})


@app.route('/t1', methods=['GET','POST'])
def getData1():
    content = request.json
    t1 = Temp('Pec',getT1(),'28-0314977974ee', datetime.datetime.now())
    logging.info('t1'+str(t1))

    return jsonify({'name':t1.name,
                    'vrednost':t1.val,
                    'serial num':t1.sn,
                    'cas':t1.date})

@app.route('/t2', methods=['GET','POST'])
def getData2():
    content = request.json
    t2 = Temp('Zalogovnik',getT2(),'28-03189779c4c9', datetime.datetime.now())
    logging.info('t2'+str(t2))

    return jsonify({'name':t2.name,
                    'vrednost':t2.val,
                    'serial num':t2.sn,
                    'cas':t2.date})



@app.route('/<name>/<from_>/<to>', methods=['GET','POST'])
def getData3(name, from_,to):
    logging.info('device/'+str(name))
    sez= db.getJsonData("temperatura",name,from_,to)
    #jsonSez = parseSez(sez)
    return Response(json.dumps(sez),  mimetype='application/json')
def oneRec(rec):
    return "{'name':'T1','vr':'22'}"
   # return jsonify({'name':rec[4],
    #                'vrednost':rec[3],
    #                'serial num':'neznano',
    #                'cas':rec[1]})
def parseSez(sez):
    jsonSez=[]
    for el in sez:
        jsonSez.append({"name": el[4],
                    "vrednost": str(el[3]),
                    "cas": str(el[1])})
    return jsonSez
@app.route('/getMax/<name>/<day>', methods=['GET'])
def getMax(name, day):
    logging.info('getMax -> device/'+str(name)+' day:'+str(day))
    val= db.getMax(name, day)
    return jsonify({'name':val[0],
                    'vrednost':val[2],
                    'serial num': "neznana",
                    'cas':val[1]})

@app.route('/getMin/<name>/<day>', methods=['GET'])
def getMin(name, day):
    logging.info('getMin -> device/'+str(name)+' day:'+str(day))
    val= db.getMin(name, day)
    return jsonify({'name':val[0],
                    'vrednost':val[2],
                    'serial num': "neznana",
                    'cas':val[1]})

@app.route('/i', methods=['GET'])
def info():
    logging.info('info ')
    t1 = Temp('Peč',getT1(),'28-03189779c4c9', datetime.datetime.now())
    t2 = Temp('Zalogovnik',getT2(),'28-03189779c4c9', datetime.datetime.now())
    relay = Relay('Rele za pumpo',getStatus(), '001', datetime.datetime.now())
    #jsonSez = parseSez(sez)
    return jsonify({'t1':t1.toJson,
                    't2': t2.toJson,
                    'relay': relay.toJson})

@app.route('/today/<name>', methods=['GET','POST'])
def getToday(name):
    logging.info('today/ '+str(name))
    sez= db.getToday(name)
    return Response(json.dumps(sez),  mimetype='application/json')

@app.route('/u/<ure>/<name>', methods=['GET'])
def urNazaj(name, ure):
    logging.info('ur nazaj/ '+str(name))
    sez= db.urNazaj(name,ure)
    return Response(json.dumps(sez),  mimetype='application/json')

@app.route('/d/<n>/<name>', methods=['GET'])
def dniNazaj(name, n):
    logging.info('dni nazaj/ '+str(name))
    sez= db.dniNazaj(name,n)
    return Response(json.dumps(sez),  mimetype='application/json')

@app.route('/c', methods=['GET'])
def pretekliPodatki():
    name= request.args.get('name')
    st_dni= request.args.get('st_dni')
    logging.info(str(st_dni)+' dni nazaj/ '+str(name))
    sez= db.dniNazaj(name,st_dni)
    return Response(json.dumps(sez),  mimetype='application/json')

@app.route('/h', methods=['GET'])
def pretekliPodatki2():
    ime= request.args.get('ime')
    ure= request.args.get('ur')
    logging.info(str(ime)+' termometer - > st ur: '+str(ure))
    sez= db.urNazaj(ime,ure)
    return Response(json.dumps(sez),  mimetype='application/json')

@app.route('/h/<name>', methods=['GET'])
def pretekliPodatki3(name):
    ime= name
    ure= request.args.get('ur')
    logging.info(str(ime)+' termometer - > st ur: '+str(ure))
    sez= db.urNazaj(ime,ure)
    logging.info("Podatki veliki: "+ str(len(sez)))
    return Response(json.dumps(sez),  mimetype='application/json')

@app.route('/relay/<status>', methods=['GET', 'POST'])
def relayOnOff(status):
    chanel=21
    if request.method =='POST':
        if status == 'on':
            relay.motor_on(chanel)
            logging.info("ON")
        else:
            relay.motor_off(chanel)
            logging.info("OFF")
    else:
        if status == 'on':
            on()
            logging.info(" relay ON")
        else:
            off()
            logging.info(" relay OFF")
    return "OK"


if __name__=='__main__':
    app.run(host='0.0.0.0')
