# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:07:22 2019

@author: arifr
"""


import pydbgen
import random
from pydbgen import pydbgen
db=pydbgen.pydb()
import mysql.connector 
from mysql.connector import Error
import sys


nurseidlist=[]
for i in range(5000,6000):
    nurseidlist.append(random.randrange(5000,6000))
    
    
pidlist=[]
for i in range(5000,6000):

    pidlist.append(random.randrange(1000,2100))


l=[]
i=0
while (i<1000):
    x=[]
    i+=1
    x.append(nurseidlist.pop(0))
    x.append(pidlist.pop(0))
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

for i in l:
    
    sql_query = """INSERT INTO raja.cares (nurse_id,pid) VALUES (%s, %s)"""
    val= (i[0],i[1])
    result = cursor.execute(sql_query,val)
    conn.commit()
    


    

