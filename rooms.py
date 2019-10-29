# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 01:28:43 2019

@author: arifr
"""


import pydbgen
import random
from pydbgen import pydbgen
db=pydbgen.pydb()
import mysql.connector 
from mysql.connector import Error
import sys



types=['Premium', 'Small', 'Large' , 'Luxury','General Ward']
roomlist=[]
typelist=[]
for i in range(500):
    typelist.append(types[random.randrange(0,len(types))])
    
    
for i in range(500,1000):
    roomlist.append(i)
    

l=[]
i=0
while (i<500):
    x=[]
    i+=1
    x.append(roomlist.pop(0))
    x.append(typelist.pop(0))
    l.append(x)
    


    

conn = None

conn = mysql.connector.connect(host='localhost',
                                   database='raja',
                                   user='root',
                                   password='raja123')
if conn.is_connected():
        print('Connected to MySQL database')
   
cursor =conn.cursor()



for i in l:

    
    sql_query = """INSERT INTO raja.rooms (room_num, room_type) VALUES (%s, %s)"""
    val= (i[0],i[1])

    result = cursor.execute(sql_query,val)
    conn.commit()
    
conn.close()



    

