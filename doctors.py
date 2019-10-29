# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 00:52:02 2019

@author: arifr
"""

import pydbgen
import random
from pydbgen import pydbgen
db=pydbgen.pydb()
import mysql.connector 
from mysql.connector import Error
import sys


nameset = db.gen_dataframe(200,['name',])
namelist = [list(x) for x in nameset.values]


subset4=db.gen_dataframe(200,['name','phone'])
phonel = [list(x) for x in subset4.values]
phonelist=[]
for i,j in phonel:
    j=j.split('-')
    x=''.join(j)
    phonelist.append(x)
    

depts=['Angiology','Vascular Medicine','Cardiology','Critical care medicine','Endocrinology','Gastroenterology','Geriatrics','Hematology','Hepatology' ,'Infectious disease','Nephrology','Neurology','Oncology','Pediatrics','Pulmonology','Pneumology','Rheumatology','Sports Medicine','Urology','Cancer Medicine','Dermatopathology','Anesthesiology' ,'Clinical cytogenetics','Clinical genetics','Molecular genetic pathology','Gynecologic oncology','Maternal-fetal medicine','Immunopathology']

deptslist=[]
for i in range(200):
    deptslist.append(depts[random.randrange(0,len(depts))])


quals=['MBBS', 'MD', 'DO' , 'MCM','DS','MMSC','MM','PD']
didlist=[]
quallist=[]
for i in range(200):
    quallist.append(quals[random.randrange(0,len(quals))])
    
    
for i in range(200,400):
    didlist.append(i)
    

l=[]
i=0
while (i<200):
    x=[]
    i+=1
    x.append(didlist.pop(0))
    x.append(namelist.pop(0).pop(0))
    x.append(quallist.pop(0))

    x.append(phonelist.pop(0))
    x.append(deptslist.pop(0))

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

    
    sql_query = """INSERT INTO raja.doctors (did, Name, qualifications,Phone,dept_name) VALUES (%s, %s, %s, %s, %s)"""
    val= (i[0],i[1],i[2],i[3],i[4])
    result = cursor.execute(sql_query,val)
    conn.commit()
    
conn.close()


    

