import requests
import json


url= "http://192.168.0.121:5000"


def checkStatus():
    response = requests.get(url+"/i")
    data = response.text
    jsonStr = json.loads(data)
    return jsonStr['relay']['vrednost']
