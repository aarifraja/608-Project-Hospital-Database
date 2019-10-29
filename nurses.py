# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 00:16:29 2019

@author: arifr
"""

import pydbgen
import random
from pydbgen import pydbgen
db=pydbgen.pydb()
import mysql.connector 
from mysql.connector import Error
import sys


nameset = db.gen_dataframe(1000,['name',])
namelist = [list(x) for x in nameset.values]


subset4=db.gen_dataframe(1000,['name','phone'])
phonel = [list(x) for x in subset4.values]
phonelist=[]
for i,j in phonel:
    j=j.split('-')
    x=''.join(j)
    phonelist.append(x)
    

        

nurseidlist=[]
for i in range(5000,6000):
    nurseidlist.append(i)



l=[]
i=0
while (i<1000):
    x=[]
    i+=1
    x.append(nurseidlist.pop(0))
    x.append(namelist.pop(0).pop(0))
    x.append(phonelist.pop(0))
    l.append(x)
    


print (l)

conn = None

conn = mysql.connector.connect(host='localhost',
                                   database='raja',
                                   user='root',
                                   password='raja123')
if conn.is_connected():
        print('Connected to MySQL database')

    
    
cursor =conn.cursor()


print(l)


for i in l:
    
    sql_query = """INSERT INTO raja.nurses (nurse_id, Name,Phone) VALUES (%s, %s, %s)"""
    val= (i[0],i[1],i[2])
    result = cursor.execute(sql_query,val)
    conn.commit()
    

    

    

