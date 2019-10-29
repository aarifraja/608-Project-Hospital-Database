# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 01:35:27 2019

@author: arifr
"""


import pydbgen
import random
from pydbgen import pydbgen
db=pydbgen.pydb()
import mysql.connector 
from mysql.connector import Error
import sys



nameset = db.gen_dataframe(1100,['name',])
namelist = [list(x) for x in nameset.values]

subset4=db.gen_dataframe(1100,['name','phone'])
phonel = [list(x) for x in subset4.values]
phonelist=[]
for i,j in phonel:
    j=j.split('-')
    x=''.join(j)
    phonelist.append(x)

    
genderlist=[]

for i in range(1000,2100):
    num=random.randrange(20, 50) 
    if num%2:
        genderlist.append('M')
    else:
        genderlist.append('F')
  

        
subset2=db.gen_dataframe(1100,['name','phone'])

list2 = [list(x) for x in subset2.values]

I=1
addresslist=[]
for city, phone in list2:
    city= str(i)+" "+str(city.split()[1])+" drive,"
    i+=1
    phone =phone.split('-')
    phone = "".join(phone)
    phone=phone[:6]

    addresslist.append(city+" "+phone)
    

pidlist=[]
for i in range(1000,2100):

    pidlist.append(i)
    

#DID
didlist=[]
for i in range(1100):

    didlist.append(random.randrange(200, 400))
    

roomlist=[]
for i in range(1100):

    roomlist.append(random.randrange(500, 1000))
    



l=[]
i=0
while (i<1100):
    x=[]
    i+=1
    x.append(pidlist.pop(0))
    x.append(namelist.pop(0).pop(0))
    x.append(genderlist.pop(0))
    x.append(addresslist.pop(0))
    x.append(phonelist.pop(0))
    x.append(didlist.pop(0))
    x.append(roomlist.pop(0))
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
    

    
    sql_query = """INSERT INTO raja.patients (pid, Name, Address, Gender,Phone,did,roomnum) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    val= (i[0],i[1],i[3],i[2],i[4],i[5],i[6])

    
  
    result = cursor.execute(sql_query,val)
    conn.commit()
    

    


    

