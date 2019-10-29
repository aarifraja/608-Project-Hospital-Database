# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:41:33 2019

@author: arifr
"""

import pydbgen
import random
from pydbgen import pydbgen
db=pydbgen.pydb()
import mysql.connector 
from mysql.connector import Error
import sys



file = open("medfinallist.txt","r")
med=[]
for line in file:
    x=line.strip();
    z=x.split()
    y=" ".join(z[:2])
    med.append(y)
    if y in [""," ", "  "]:
        med.pop()
    
 
n=len(med)
    

file2 = open("diseases.txt","r")
dis=[]
for line in file2:
    x=line.strip();
    z=x.split()
    y=" ".join(z[:2])
    
    dis.append(y)
    if y in [""," ", "  "]:
        dis.pop()
    
m=len(dis)

reclist=[]
for i in range(3000,5500):
    reclist.append(i)
    

medlist=[]
dislist=[]
    
for i in range(2500):
    medlist.append(med[random.randrange(0,n)][:28])
    
for i in range(2500):
    dislist.append(dis[random.randrange(0,m)][:28])


    
billlist=[]

for i in range(2500):
    num=random.randrange(100, 10000) 
  
    billlist.append(num)

day=[i for i in range(1,32)]
month = [i for i in range(1,13) ]
year=[2000+i for i in range(20)]
admit=[]
disc=[]
for i in range (2500):
    yearstring= str(year[random.randrange(0,20)])
    monthindex= random.randrange(0,10)
    dischargeindex= monthindex+random.randrange(0,2)
    addate= random.randrange(1,20)
    datey= yearstring+'-'+str(month[monthindex])+'-'+str(addate)
    
    admit.append(datey)

    datey= yearstring+'-'+str(month[dischargeindex])+'-'+str(addate+random.randrange(0,10))

    disc.append(datey)
    

pidlist=[]
    
for  i in range(2500):
    pidlist.append(random.randrange(1000,2100))


l=[]
i=0


while (i<2500):
    x=[]
    i+=1
    x.append(reclist.pop(0))
    x.append(medlist.pop(0))
    x.append(dislist.pop(0))
    x.append(billlist.pop(0))
    x.append(admit.pop(0))
    x.append(disc.pop(0))
    x.append(pidlist.pop(0))
    l.append(x)
    



conn = None

conn = mysql.connector.connect(host='localhost',
                                   database='raja',
                                   user='root',
                                   password='raja123')
if conn.is_connected():
        print('Connected to MySQL database')

    
    
cursor =conn.cursor()


print (l)


for i in l:
        
    sql_query = """INSERT INTO raja.medical_records (rec_id, medicine,disease, bill, admit_date,discharge_date,pid) VALUES (%s, %s, %s, %s,%s, %s,%s)"""
    val= (i[0],i[1],i[2],i[3],i[4], i[5],i[6])
    result = cursor.execute(sql_query,val)
    conn.commit()
    




