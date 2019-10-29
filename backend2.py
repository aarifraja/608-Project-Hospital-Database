# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:34:45 2019

@author: arifr
"""




import mysql.connector 
from mysql.connector import Error


def searchallfn(pidval):
    
     conn = mysql.connector.connect(host='localhost',
                               database='raja',
                               user='root',
                               password='raja123')
     x=pidval
     cursor =conn.cursor()
     query= "select pid,name,gender,address,phone,roomnum from patients where name = %s or address =%s or phone= %s or  roomnum= %s"
     cursor.execute(query,(x,x,x,x))
     results= cursor.fetchall()
     print (results)
     conn.close()
     return results

 
def searchbackend(pidval):
    
     conn = mysql.connector.connect(host='localhost',
                               database='raja',
                               user='root',
                               password='raja123')
     x=pidval
     cursor =conn.cursor()
     query= "select medicine,disease, bill, admit_date, discharge_date,bill from medical_records where rec_id = %s or rec_id = %s"
     cursor.execute(query,(x,x))

     results= cursor.fetchall()
     print (results)
     conn.close()
     return results

def searchds_fn(didval):
    
     conn = mysql.connector.connect(host='localhost',
                               database='raja',
                               user='root',
                               password='raja123')
     x=didval
     cursor =conn.cursor()
     query= "select Name, Phone from nurses where nurse_id = %s or nurse_id = %s"
     cursor.execute(query,(x,x))

     results= cursor.fetchall()
     print (results)
     conn.close()
     return results





