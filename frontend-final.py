# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:02:31 2019

@author: arifr
"""



import os
from tkinter import *
import tkinter.messagebox
import backend_final


class hospital:

    def __init__(self,root):
        root.title("Hospital database")
        
        def insert():
            rows= backend_final.insert_fn(self.entry_ipid.get(), self.entry_iname.get(),self.entry_igender.get(),self.entry_iadd.get(),self.entry_iphone.get(), self.entry_idid.get(),self.entry_iroom.get() )
            display_insert.delete(0,'end')
            
            if rows[0]=="duplicate entry for pid":
                display_insert.insert(END, "Insert Failed: Duplicate PID value ",str(""))
             
            if rows[0]=="pid not num":
                display_insert.insert(END, "Insert Failed: Enter integer PID value ",str("")) 
                
            if rows[0]=="name":
                display_insert.insert(END, "Insert Failed: Invalid name ",str(""))
                
            if rows[0]=="phone":
                print("heree")
                display_insert.insert(END, "Insert Failed: Invalid phone num ",str(""))
                
            if rows[0]=="DID not present in our system":
                display_insert.insert(END, "Insert Failed: Invalid DID ",str(""))
                
            if rows[0]=="Room Num not present in our system":
                display_insert.insert(END, "Insert Failed: Room Num not valid ",str(""))
                
            if rows[0]=="gender":
                display_insert.insert(END, "Insert Failed: Gender should be M or F ",str(""))
            
            if rows[0]=="success":
                display_insert.insert(END, "successfully added ",str(""))
                self.entry_iname.delete(0,'end')
                
                
                
        
        def monthbill():
            rows=backend_final.monthbill_fn(self.entry_mbill.get(),self.entry_ybill.get())
            display_mbillop.delete(0,'end')
            if len(rows):
                for row in rows:
                    display_mbillop.insert(END, row,str(""))
            else:
                display_mbillop.insert(END, "did not in database,enter valid did",str(""))
                
        def freqdisall():
            rows=backend_final.freqdisall_fn()
            display_fredisopall.delete(0,'end')
            if len(rows):
                for row in rows:
                    display_fredisopall.insert(END, row[0],str(""))
            else:
                display_fredisopall.insert(END, "did not in database,enter valid did",str(""))
                
        def freqdis():
            rows=backend_final.freqdis_fn(self.entry_fredis.get())
            display_fredisop.delete(0,'end')
            if len(rows):
                for row in rows:
                    display_fredisop.insert(END, row[0],str(""))
            else:
                display_fredisop.insert(END, "No records for that year",str(""))

        def search():
            rows=backend_final.searchbackend(self.entry1.get())
            display.delete(0,'end')
            arr=['Name', 'Gender', 'Address', 'Phone','Room']
            i=0
            if not len(rows):
                display.insert(END, "Invalid PID,  Plese Enter Valid PID",str(""))
            else:
                for row in rows[0]:
                    display.insert(END,arr[i]+" : "+ str(row),str(""))
                    i+=1
                    
                    
        def searchds():
            rows=backend_final.searchds_fn(self.entryds.get())
            displayds.delete(0,'end')
            arr=['Name', 'Phone','Qualifications','Dept']
            i=0
            if not len(rows):
                displayds.insert(END, "Invalid DID,  Plese Enter Valid DID",str(""))
            else:
                for row in rows[0]:
                    displayds.insert(END,arr[i]+" : "+ str(row),str(""))
                    i+=1
                    
        def searchall():
            rows=backend_final.searchallfn(self.entry2.get())
            display3.delete(0,'end')
            arr=['PID','Name', 'Gender', 'Address', 'Phone','Room']
            i=0
            if not len(rows):
                display3.insert(END, "The entry has no match in database",str(""))
            else:
                display3.insert(END, "There are " +str(len(rows)) +" matching records as listed below:",str(""))
                display3.insert(END, "-------------------------------------------------------------------------------------------",str(""))
                for row in rows:
                    i=0
                    for ele in row:
                        display3.insert(END,arr[i]+" : "+ str(ele),str(""))
                        i+=1
                    display3.insert(END, "-------------------------------------------------------------------------------------------",str(""))


        
        def search2():
            rows=backend_final.searchbackend(self.entry1.get())
            for row in rows:
                display3.insert(END, row,str(""))
        def income():
            rows=backend_final.fn_income(self.entry21.get())
            display21.delete(0,'end')
            if len(rows):
                for row in rows:
                    display21.insert(END, row,str(""))
            else:
                display21.insert(END, "did not in database,enter valid did",str(""))
                
        def clearfreqdisall():
            display_fredisopall.delete(0,'end')
            
        def findept():
            rows=backend_final.findep(self.entry_nh.get())
            displaynh.delete(0,'end')
            if len(rows):
                if rows==["nurse id"]:
                    displaynh.insert(END, "Invalid Nurse ID ",str(""))
                    return 
                if rows==["nurse not presnt"]:
                    displaynh.insert(END, "No patients for nurse ",str(""))
                    return 
                    
                for row in rows:
                    displaynh.insert(END, row,str(""))
            else:
                displaynh.insert(END, "Invaid nurse_id ",str(""))
        
                
        
        def freqmed():
            rows=backend_final.fn_freqmed(self.entry_for_med.get())
            display_med.delete(0,'end')
            if len(rows):
                for row in rows:
                    display_med.insert(END, row,str(""))
            else:
                display_med.insert(END, "Invalid DID",str(""))
                
                
        def dept_patients():
            rows=backend_final.dept_patients(self.entry_for_cases.get())
            display_cases.delete(0,'end')
            if len(rows):
                for row in rows:
                    display_cases.insert(END, row,str(""))
            else:
                display_cases.insert(END, "Dept not in database,enter valid dept",str(""))
                
        

        
        f1 = Frame(root, background="bisque")
        f2 = Frame(root, background="bisque")
        


        f1.grid(row=0, column=0, sticky="nsew")
        f2.grid(row=1, column=0, sticky="nsew")

        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=25)
        
        rootlabel=Label(f1, text="Hospital Database Management System", font='bold', bg='bisque')
        rootlabel.grid(row=0, column=0, sticky="nsew",columnspan=2)
        f1.grid_columnconfigure(0, weight=1)
        
        df1= LabelFrame(f2,bg='bisque')
        df2= LabelFrame(f2,bg='bisque')
        
        df1.grid(row=0, column=0, sticky="nsew")
        df2.grid(row=1, column=0, sticky="nsew")
        
        f2.grid_rowconfigure(0, weight=1)
        f2.grid_rowconfigure(1, weight=1)
        f2.grid_columnconfigure(0, weight=1)
        
        button_x = Button(f1,text='EXIT',command= root.destroy,font='bold',bg= 'tan1')
        button_x.grid(row=0 ,column=4,sticky='e')
        
        label1=Label(df1,text= "Enter PID to get patient details", padx=5,pady=5,bg="bisque")
        label1.grid(row=0,column=0)

        self.entry1=Entry(df1,bg="white")
        self.entry1.grid(row=0,column=1)
        
        searchbutton = Button(df1,text='search',command= search)
        searchbutton.grid(row=1,column=1)
        
        display=Listbox(df1,width='40',height='10')
        display.grid(row =2,column=0, sticky='ns', pady=8,columnspan=2)
        
        labelds=Label(df1,text= "Enter DID to get doctor details", padx=5,pady=5,bg="bisque")
        labelds.grid(row=0,column=4)

        self.entryds=Entry(df1,bg="white")
        self.entryds.grid(row=0,column=5)
        
        searchbuttonds = Button(df1,text='search',command= searchds)
        searchbuttonds.grid(row=1,column=5)
        
        
        displayds=Listbox(df1,width='40',height='10')
        displayds.grid(row =2,column=5, sticky='ns', pady=8,columnspan=2)
        

        label2=Label(df1,text= "Enter Phone/Address/Name/RoomNum",padx=5,bg="bisque")
        label2.grid(row=0,column=2)
        label3=Label(df1,text= " to fetch  matching patients ",padx=5,bg="bisque")
        label3.grid(row=1,column=2)
        
        self.entry2=Entry(df1,bg="white")
        self.entry2.grid(row=0,column=3)
        
        searchbutton2 = Button(df1,text='searchall',command= searchall)
        searchbutton2.grid(row=1,column=3)
        
        scroll2= Scrollbar(df1)
        scroll2.grid(row =2,column=4, sticky='nsw')
        
        display3=Listbox(df1,width='40',heigh='16',yscrollcommand=scroll2.set)
        display3.grid(row =2,column=3 ,sticky='ns')
        
        labelmb=Label(df1,text= "Fill Details below to see the income generated in a given month ",padx=5,pady=10,bg="bisque")
        labelmb.grid(row=4,column=2,columnspan=2)
        
        label_monthbill=Label(df1,text= "Enter Month in MM fromat ",padx=5,bg="bisque")
        label_monthbill.grid(row=5,column=2)
        
        self.entry_mbill=Entry(df1,bg="white")
        self.entry_mbill.grid(row=5,column=3)
        
        label_ybill=Label(df1,text= "Enter Year in YYYY format ",padx=5,bg="bisque")
        label_ybill.grid(row=6,column=2)
        
        self.entry_ybill=Entry(df1,bg="white")
        self.entry_ybill.grid(row=6,column=3)
        
        display_mbillop=Listbox(df1,width='30',heigh='1')
        display_mbillop.grid(row =8,column=3, sticky='ns',pady=8)
        
        label_mbillop=Label(df1,text= "Total Income in entered month-year",padx=5,bg="bisque")
        label_mbillop.grid(row=8,column=2)
        
        
        label_nh=Label(df1,text= "Enter nurse id to get the departments of doctors",padx=5,bg="bisque")
        label_nh.grid(row=9,column=2)
        label_nh2=Label(df1,text= "treating her patients  ",padx=5,bg="bisque")
        label_nh2.grid(row=10,column=2)

        
        self.entry_nh=Entry(df1,bg="white")
        self.entry_nh.grid(row=9,column=3,rowspan=1)
        searchbutton_nh = Button(df1,text='click here ',command= findept)
        searchbutton_nh.grid(row=10,column=3)
        
        scroll3= Scrollbar(df1)
        scroll3.grid(row =11,column=4, sticky='nsww')
        
        displaynh=Listbox(df1,width='20',heigh='2',yscrollcommand=scroll3.set)
        displaynh.grid(row =11,column=3 ,sticky='ns')
        
        
        searchbutton_monthbill = Button(df1,text='click here for income',command= monthbill)
        searchbutton_monthbill.grid(row=7,column=3)
        
        label_fredis=Label(df1,text= "See below for Disease statistics ",padx=5,bg="bisque")
        label_fredis.grid(row=4,column=4,columnspan=2)
        
        
        label_fredis=Label(df1,text= "Enter year in YYYY to get the most frquent ",padx=5,bg="bisque")
        label_fredis.grid(row=5,column=4)
        
        label_fredis2=Label(df1,text= "disease in that year ",padx=5,bg="bisque")
        label_fredis2.grid(row=6,column=4)
        
        self.entry_fredis=Entry(df1,bg="white")
        self.entry_fredis.grid(row=5,column=5,rowspan=2)
        
        buttonfreqdis = Button(df1,text='click here', command = freqdis)
        buttonfreqdis.grid(row=7,column=5)
        
        label_fredisop=Label(df1,text= "Most frequent disease in that year ",padx=5,bg="bisque")
        label_fredisop.grid(row=8,column=4)
        
        display_fredisop=Listbox(df1,width='30',heigh='1')
        display_fredisop.grid(row =8,column=5, sticky='ns',pady=8)
        
        label_fredisall=Label(df1,text= " For the Most frequent disease accross  ",padx=5,bg="bisque")
        label_fredisall.grid(row=9,column=4)
        
        label_fredis2all=Label(df1,text= "all the years, click on right button ",padx=5,pady=0,bg="bisque")
        label_fredis2all.grid(row=10,column=4)
        
        display_fredisopall=Listbox(df1,width='30',heigh='1')
        display_fredisopall.grid(row =9,column=5, sticky='nsw',pady=8,columnspan=2)
        
        buttonfreqdisall = Button(df1,text='click here', command = freqdisall)
        buttonfreqdisall.grid(row=10,column=5,sticky='w')
        buttonfreqdisallclear = Button(df1,text='clear',command=clearfreqdisall)
        buttonfreqdisallclear.grid(row=10,column=6,sticky='w')
        
              
        label4=Label(df1,text= "Fill Details below to create a patient entry ",padx=5,pady=10,bg="bisque")
        label4.grid(row=4,column=0)
        
        label_ipid=Label(df1,text= "Enter a PID ",padx=5,bg="bisque")
        label_ipid.grid(row=5,column=0)
        
        self.entry_ipid=Entry(df1,bg="white")
        self.entry_ipid.grid(row=5,column=1)
        
        label_iname=Label(df1,text= "Enter Name ",padx=5,bg="bisque")
        label_iname.grid(row=6,column=0)
        
        self.entry_iname=Entry(df1,bg="white")
        self.entry_iname.grid(row=6,column=1)
        
        label_igender=Label(df1,text= "Enter Gender (M/F) ",padx=5,bg="bisque")
        label_igender.grid(row=7,column=0)
        
        self.entry_igender=Entry(df1,bg="white")
        self.entry_igender.grid(row=7,column=1)
        
        label_iadd=Label(df1,text= "Enter Address ",padx=5,bg="bisque")
        label_iadd.grid(row=8,column=0)
        
        self.entry_iadd=Entry(df1,bg="white")
        self.entry_iadd.grid(row=8,column=1)
        
        label_iphone=Label(df1,text= "Enter Phone ",padx=5,bg="bisque")
        label_iphone.grid(row=9,column=0)
        
        self.entry_iphone=Entry(df1,bg="white")
        self.entry_iphone.grid(row=9,column=1)
        
        label_idid=Label(df1,text= "Assign a doctor ID ",padx=5,bg="bisque")
        label_idid.grid(row=10,column=0)
        
        self.entry_idid=Entry(df1,bg="white")
        self.entry_idid.grid(row=10,column=1)
        
        label_iroom=Label(df1,text= "Enter room number ",padx=5,bg="bisque")
        label_iroom.grid(row=11,column=0)
        
        self.entry_iroom=Entry(df1,bg="white")
        self.entry_iroom.grid(row=11,column=1)
        
        insertbutton = Button(df1,text='insert',command= insert)
        insertbutton.grid(row=12,column=0)
        
        display_insert=Listbox(df1,width='40',heigh='2')
        display_insert.grid(row =13,column=0, sticky='ns',pady=8)
         
        
        label21=Label(df2,text= "Enter did  of doctor to find out his total income : ",padx=5,bg="bisque")
        label21.grid(row=0,column=0)

        
        self.entry21=Entry(df2,bg="white")
        self.entry21.grid(row=0,column=1)
        button21 = Button(df2,text='confirm DID to get income below', command = income)
        button21.grid(row=1,column=1)
        
        labeltotinc=Label(df2,text= "Total income of requested did : ",bg="bisque")
        labeltotinc.grid(row=2,column=0)
        
        
        display21=Listbox(df2,width='30',heigh='2')
        display21.grid(row =2,column=1, sticky='ns',pady=8)
        
        labelmed=Label(df2,text= " Enter DID to find put his most frequent prescription ",padx=30,pady=2,bg="bisque")
        labelmed.grid(row=0,column=2)
        
        self.entry_for_med=Entry(df2,bg="white")
        self.entry_for_med.grid(row=0,column=3)
        
        buttonmed = Button(df2,text='confirm DID to get answer below', command = freqmed)
        buttonmed.grid(row=1,column=3)
        
        label_to_med=Label(df2,text= " Most frequet presciption of requested did : ",bg="bisque")
        label_to_med.grid(row=2,column=2)
        
        display_med=Listbox(df2,width='30',heigh='2')
        display_med.grid(row =2,column=3, sticky='ns',pady=8)
        
  
        
        #buttonexit = Button(df1,text='EXIT',bg='tan1',command=root.destroy)
        #buttonexit.grid(row=13,column=3)
        
        label_to_cases=Label(df2,text= " Patients trated by entered Department : ",bg="bisque")
        label_to_cases.grid(row=0,column=4)
        
        self.entry_for_cases=Entry(df2,bg="white")
        self.entry_for_cases.grid(row=0,column=5)

        button_deptcases = Button(df2,text='click here after filling above', command = dept_patients)
        button_deptcases.grid(row=1,column=5)
        

        label_to_cases=Label(df2,text= " Total patients handled  by entered Department : ",bg="bisque")
        label_to_cases.grid(row=2,column=4)
        
        
        display_cases=Listbox(df2,width='30',heigh='2')
        display_cases.grid(row =2,column=5, sticky='ns',pady=8)
        
        def newwin():
            cmd= "python second.py"
            os.system(cmd)
            
        button_end = Button(f1,text='For more query oprtions, click here for a new window',command= newwin,font='bold',bg= 'lemon chiffon')
        button_end.grid(row=1 ,column=3, columnspan=2)
        button_end.config( height =1, width = 40)
        

        


if __name__=='__main__':
    root = Tk()
    #root.attributes('-fullscreen', True)
    application = hospital(root)
    root.mainloop()



