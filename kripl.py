#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import requests
import json
import time

################################################

#kratice kovancev
kovanci = ['BTC', 'ETH']

#API naslov, na katerem dobiš podatke
url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,BCH&tsyms=EUR'


#funkcija na url dobi json podatke
def getData(url):
             ''' getData(url) --> vrne JSON podatke in podanega URL-ja '''
             return json.loads(requests.get(url).text)

def procent(v1, v2):
             return (v2-v1)/v1*100


def izpisiPodatke():
             prvaVr = getData(url)['BTC']['EUR']
             staraVr = prvaVr
             mini = prvaVr
             maksi = prvaVr
             while True:
                          pod = getData(url)
                          novaVr = pod['BTC']['EUR']
                          if novaVr> maksi:
                                       maksi=novaVr
                          elif novaVr < mini:
                                       mini = novaVr
                          
                          print(kovanci[0]+':  ' +str(pod[kovanci[0]]['EUR']) +'   ' + str(round(procent(staraVr,novaVr),5))+'%          '+ 'Začetek: ' + str(prvaVr)+ '    ' +str(round(procent(prvaVr, novaVr),4))+'%'+ ' Mini: '+str(mini)+' Maks: '+str(maksi))
                          staraVr = novaVr
                          time.sleep(5)


izpisiPodatke()

A
A
A
A
A
A
A
A
A
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B

