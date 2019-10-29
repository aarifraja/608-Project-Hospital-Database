# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 00:13:20 2019

@author: arifr
"""



import pydbgen
import random
from pydbgen import pydbgen
db=pydbgen.pydb()
import mysql.connector 
from mysql.connector import Error
import sys

depts=['Angiology','Vascular Medicine','Cardiology','Critical care medicine','Endocrinology','Gastroenterology','Geriatrics','Hematology','Hepatology' ,'Infectious disease','Nephrology','Neurology','Oncology','Pediatrics','Pulmonology','Pneumology','Rheumatology','Sports Medicine','Urology','Cancer Medicine','Dermatopathology','Anesthesiology' ,'Clinical cytogenetics','Clinical genetics','Molecular genetic pathology','Gynecologic oncology','Maternal-fetal medicine','Immunopathology']


print (len(depts));
nameset = db.gen_dataframe(len(depts),['name',])
namelist = [list(x) for x in nameset.values]

subset4=db.gen_dataframe(len(depts),['name','phone'])
phonel = [list(x) for x in subset4.values]
phonelist=[]
for i,j in phonel:
    j=j.split('-')
    x=''.join(j)
    phonelist.append(x)
    


l=[]
i=0
n= len(depts)
while (i<n):
    x=[]
    i+=1
    x.append(depts.pop(0))
    x.append(namelist.pop(0).pop(0).split()[1]+' Buliding')
    x.append(phonelist.pop(0))


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
 
    sql_query = """INSERT INTO raja.med_depts (dept_name, building_name, frontdesk_contact) VALUES (%s, %s, %s)"""
    val= (i[0],i[1],i[2])
    result = cursor.execute(sql_query,val)
    conn.commit()
conn.close()




    


    

