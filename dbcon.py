#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",user="administrator",passwd="geslo4ras", database="doma")
cur = mydb.cursor()

def insert(time,value,user):
    sql = "INSERT INTO kojn (ctime, value, user_id) VALUES (%s, %s, %s)"
    val = (time, value, user)
    cur.execute(sql, val)
    mydb.commit()
    print("Dodan podatek:" + time +"  ; "+str(value))
    
def select():
    sql= "SELECT * FROM kojn"
    cur.execute(sql)
    for x in cur:
        print(x)
