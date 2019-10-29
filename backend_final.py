# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 01:26:48 2019

@author: arifr
"""




import mysql.connector 
from mysql.connector import Error


def insert_fn(pidval,nameval,gval, addval,phoneval, didval, roomval):
    
     conn = mysql.connector.connect(host='localhost',
                               database='raja',
                               user='root',
                               password='raja123')
     cursor =conn.cursor()
     if  not pidval.isdigit():
         return ["pid not num"]
     query=  " select count(*) from  patients where pid=%s or pid =%s"
     cursor.execute(query,(pidval,pidval))
     results= cursor.fetchall()

     if results[0][0]!=0:
         return ["duplicate entry for pid"]
     
     if (not nameval.isalpha() or (len(nameval)==0)):
         return ["name"]
     query=  " select count(*) from  patients where pid=%s or pid =%s"
     cursor.execute(query,(pidval,pidval))
     results= cursor.fetchall()
     print(results)
     print(results[0][0])
     if results[0][0]!=0:
         return ["duplicate entry for pid"]
     
     
     if gval not in ['F','M']:
         return ["gender"]
     if  (not phoneval.isdigit()) or  (not len(phoneval)==10):
         return ["phone"]
     
     query=  " select count(*) from  doctors where did=%s or did =%s"
     cursor.execute(query,(didval,didval))
     results= cursor.fetchall()

     if results[0][0]==0:
         return ["DID not present in our system"]
     
     query=  " select count(*) from  rooms  where room_num=%s or room_num =%s"
     cursor.execute(query,(roomval,roomval))
     results= cursor.fetchall()

     if results[0][0]==0:
         return ["Room Num not present in our system"]



     query=  " INSERT INTO patients (pid,name,gender,address,phone,did,roomnum) values (%s,%s,%s,%s,%s,%s,%s) ";
     cursor.execute(query, (pidval,nameval,gval, addval,phoneval, didval, roomval) )
     conn.commit()
     conn.close()
     
     return ["success"]
     
     

def freqdisall_fn():
    
     conn = mysql.connector.connect(host='localhost',
                               database='raja',
                               user='root',
                               password='raja123')
     cursor =conn.cursor()

     query=" select disease , count(disease)  as freq from medical_records group by disease order by freq desc  limit 1" ;
     cursor.execute(query)
   
     results= cursor.fetchall()         
     conn.close()
     return results


def dept_patients(dept):
    
     conn = mysql.connector.connect(host='localhost',
                               database='raja',
                               user='root',
                               password='raja123')
     cursor =conn.cursor()

     query=" select count(*) from (patients join doctors  on doctors.did = patients.did) where dept_name = %s or dept_name=%s" ;
     cursor.execute(query,(dept,dept))
   

     results= cursor.fetchall()
     ans=results[0][0]
     if ans==0:
         query=" SELECT COUNT(*) FROM med_depts WHERE dept_name=%s or dept_name=%s";
         cursor.execute(query,(dept,dept))
         res=cursor.fetchall()
         if res[0][0]==0:
             conn.close()
             return []
         

     conn.close()
     return results


def findep(nid):
    
     conn = mysql.connector.connect(host='localhost',
                               database='raja',
                               user='root',
                               password='raja123')
     cursor =conn.cursor()
     
     query=  " select count(*) from nurses where nurse_id=%s or nurse_id =%s"
     cursor.execute(query,(nid,nid))
     results= cursor.fetchall()
     print(results)
     print(results[0][0])
     if results[0][0]==0:
         return ["nurse id"]
     
     query=  " select count(*) from  cares where nurse_id=%s or nurse_id =%s"
     cursor.execute(query,(nid,nid))
     results= cursor.fetchall()
     print(results)
     print(results[0][0])
     if results[0][0]==0:
         return ["nurse not presnt"]
     
     query="select dept_name from (select t1.pid,t1.nurse_id,patients.did  from (select * from  cares where nurse_id = %s or nurse_id= %s) as t1 join patients on t1.pid= patients.pid) as t2 join doctors where t2.did=doctors.did";
     cursor.execute(query,(nid,nid))
   
     results= cursor.fetchall()
     conn.close()
     return results

def fn_freqmed(did_val):
    
     conn = mysql.connector.connect(host='localhost',
                               database='raja',
                               user='root',
                               password='raja123')
     cursor =conn.cursor()

  
     query=  "select medicine  from ( patients join medical_records on medical_records.pid  = patients.pid and did = %s and did= %s) group by medicine order by count(*) DESC limit 1 ";
     cursor.execute(query,(did_val,did_val))
   
     results= cursor.fetchall()

     conn.close()
     return results
 
def freqdis_fn(year):
    
     conn = mysql.connector.connect(host='localhost',
                               database='raja',
                               user='root',
                               password='raja123')
     cursor =conn.cursor()

     
     lb= str(year)+'-'+'1'+'-'+'1'
     ub= str(int(year)+1)+'-'+'1'+'-'+'1'

     query= " select disease   as freq from (select * from medical_records where admit_date>= %s and  discharge_date < %s) as t2 group by disease order by freq desc  limit 1; "
     cursor.execute(query,(lb,ub))
     
     results= cursor.fetchall()

     conn.close()
     return results
 
    
def monthbill_fn(month,year):
    
     conn = mysql.connector.connect(host='localhost',
                               database='raja',
                               user='root',
                               password='raja123')
     cursor =conn.cursor()

     
     lb= str(year)+'-'+str(month)+'-'+'1'
     ub= str(year)+'-'+str(int(month)+1)+'-'+'1'

  
     query= "select sum(bill) from medical_records where discharge_date>= %s and  discharge_date < %s "
     cursor.execute(query,(lb,ub))

     results= cursor.fetchall()

     conn.close()
     return results


def fn_income(pidval):
    
     conn = mysql.connector.connect(host='localhost',
                               database='raja',
                               user='root',
                               password='raja123')
     x=pidval
     cursor =conn.cursor()

     query= "select income from (select did,SUM(bill) as income from patients join medical_records on medical_records.pid = patients.pid group by did ) as t1 where did = %s or did=%s "
     cursor.execute(query,(x,x))

     results= cursor.fetchall()

     conn.close()
     return results
 
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
     conn.close()
     return results

 
def searchbackend(pidval):
    
     conn = mysql.connector.connect(host='localhost',
                               database='raja',
                               user='root',
                               password='raja123')
     x=pidval
     cursor =conn.cursor()
     query= "select name,gender,address,phone,roomnum from patients where pid = %s or pid = %s"
     cursor.execute(query,(x,x))

     results= cursor.fetchall()
     conn.close()
     return results

def searchds_fn(didval):
    
     conn = mysql.connector.connect(host='localhost',
                               database='raja',
                               user='root',
                               password='raja123')
     x=didval
     cursor =conn.cursor()
     query= "select Name, Phone,Qualifications,Dept_name from doctors where did = %s or did = %s"
     cursor.execute(query,(x,x))

     results= cursor.fetchall()
     conn.close()
     return results




def searchbackendorig(pidval):
    
     conn = mysql.connector.connect(host='localhost',
                               database='raja',
                               user='root',
                               password='raja123')
     x=pidval
     cursor =conn.cursor()

     
     query= "select Name from patient where Phone = %s or Name =  %s or pid = %s "
     cursor.execute(query,(x,x,x))

     results= cursor.fetchall()
     conn.close()
     return results