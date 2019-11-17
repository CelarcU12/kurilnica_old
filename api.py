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

app = Flask(__name__)

@app.route('/')
def hello():
    '''dokumentcija '''
    with open(os.path.dirname(app.root_path) + '/project/README.md', 'r') as md_file:
        content = md_file.read()
        return markdown.markdown(content)


@app.route('/devices', methods=['GET','POST'])
def getDevices():
    content = request.json
    print('devices')
    return jsonify({"devices":"t1,t2"})

@app.route('/devices/<device_id>', methods=['GET','POST'])
def getData(device_id):
    content = request.json
    print('device/'+device_id)
    if device_id == 't1':
        return jsonify({device_id:getT1()})
    return jsonify({device_id:random.randint(1,100)})


@app.route('/t1', methods=['GET','POST'])
def getData1():
    content = request.json
    t1 = Temp('Pec',getT1(),'28-0314977974ee', datetime.datetime.now())
    print('t1'+str(t1))

    return jsonify({'name':t1.name,
                    'vrednost':t1.val,
                    'serial num':t1.sn,
                    'cas':t1.date})

@app.route('/t2', methods=['GET','POST'])
def getData2():
    content = request.json
    t2 = Temp('Zalogovnik',getT2(),'28-03189779c4c9', datetime.datetime.now())
    print('t2'+str(t2))

    return jsonify({'name':t2.name,
                    'vrednost':t2.val,
                    'serial num':t2.sn,
                    'cas':t2.date})



@app.route('/<name>/<from_>/<to>', methods=['GET','POST'])
def getData3(name, from_,to):
    print('device/'+str(name))
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
    print('getMax -> device/'+str(name)+' day:'+str(day))
    val= db.getMax(name, day)
    return jsonify({'name':val[0],
                    'vrednost':val[2],
                    'serial num': "neznana",
                    'cas':val[1]})

@app.route('/getMin/<name>/<day>', methods=['GET'])
def getMin(name, day):
    print('getMin -> device/'+str(name)+' day:'+str(day))
    val= db.getMin(name, day)
    return jsonify({'name':val[0],
                    'vrednost':val[2],
                    'serial num': "neznana",
                    'cas':val[1]})

@app.route('/i', methods=['GET'])
def info():
    print('info ')
    t1 = Temp('Peč',getT1(),'28-03189779c4c9', datetime.datetime.now())
    t2 = Temp('Zalogovnik',getT2(),'28-03189779c4c9', datetime.datetime.now())
    relay = Relay('Rele za pumpo',getStatus(), '001', datetime.datetime.now())
    #jsonSez = parseSez(sez)
    return jsonify({'t1':t1.toJson,
                    't2': t2.toJson,
                    'relay': relay.toJson})

@app.route('/today/<name>', methods=['GET','POST'])
def getToday(name):
    print('today/ '+str(name))
    sez= db.getToday(name)
    return Response(json.dumps(sez),  mimetype='application/json')

@app.route('/u/<ure>/<name>', methods=['GET'])
def urNazaj(name, ure):
    print('ur nazaj/ '+str(name))
    sez= db.urNazaj(name,ure)
    return Response(json.dumps(sez),  mimetype='application/json')

@app.route('/d/<n>/<name>', methods=['GET'])
def dniNazaj(name, n):
    print('dni nazaj/ '+str(name))
    sez= db.dniNazaj(name,n)
    return Response(json.dumps(sez),  mimetype='application/json')

@app.route('/c', methods=['GET'])
def pretekliPodatki():
    print(request)
    name= request.args.get('name')
    st_dni= request.args.get('st_dni')
    print(str(st_dni)+' dni nazaj/ '+str(name))
    sez= db.dniNazaj(name,st_dni)
    return Response(json.dumps(sez),  mimetype='application/json')

@app.route('/h', methods=['GET'])
def pretekliPodatki2():
    ime= request.args.get('ime')
    ure= request.args.get('ur')
    print(str(ime)+' termometer - > st ur: '+str(ure))
    sez= db.urNazaj(ime,ure)
    return Response(json.dumps(sez),  mimetype='application/json')

@app.route('/h/<name>', methods=['GET'])
def pretekliPodatki3(name):
    ime= name
    ure= request.args.get('ur')
    print(str(ime)+' termometer - > st ur: '+str(ure))
    sez= db.urNazaj(ime,ure)
    print("Podatki veliki: "+ str(len(sez)))
    return Response(json.dumps(sez),  mimetype='application/json')

@app.route('/relay/<status>', methods=['GET', 'POST'])
def relayOnOff(status):
    chanel=21
    if request.method =='POST':
        if status == 'on':
            relay.motor_on(chanel)
            print("ON")
        else:
            relay.motor_off(chanel)
            print("OFF")
    else:
        if status == 'on':
            on()
            print("ON")
        else:
            off()
            print("OFF")
    return "OK"


if __name__=='__main__':
    app.run(host='0.0.0.0')
