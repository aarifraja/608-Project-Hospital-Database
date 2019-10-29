# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:02:31 2019

@author: arifr
"""



import os

from tkinter import *
import tkinter.messagebox
import backend2


class hospital:

    def __init__(self,root):
        
        root.title("Hospital database")
        

                
                

        def search():
            rows=backend2.searchbackend(self.entry1.get())
            print (rows)
            display.delete(0,'end')
            arr=['medicine','disease', 'bill', 'admit_date', 'discharge_date','bill']
            i=0
            if not len(rows):
                display.insert(END, "Invalid Rec_ID",str(""))
            else:
                for row in rows[0]:
                    display.insert(END,arr[i]+" : "+ str(row),str(""))
                    i+=1
                    
        def searchds():
            rows=backend2.searchds_fn(self.entryds.get())
            print (rows)
            displayds.delete(0,'end')
            arr=['Name', 'Phone']
            i=0
            if not len(rows):
                displayds.insert(END, "Invalid nurse_id",str(""))
            else:
                for row in rows[0]:
                    displayds.insert(END,arr[i]+" : "+ str(row),str(""))
                    i+=1
                    
        def searchall():
            rows=backend_final.searchallfn(self.entry2.get())
            print (rows)
            display3.delete(0,'end')
            arr=['PID','Name', 'Gender', 'Address', 'Phone','Room']
            i=0
            if not len(rows):
                #display.delete(0,'end')
                display3.insert(END, "The entry doesn't match any reccord in database",str(""))
            else:
                display3.insert(END, "There are " +str(len(rows)) +" matching records as listed below:",str(""))
                display3.insert(END, "-------------------------------------------------------------------------------------------",str(""))
                #display.delete(0,'end')
                for row in rows:
                    i=0
                    for ele in row:
                        display3.insert(END,arr[i]+" : "+ str(ele),str(""))
                        i+=1
                    display3.insert(END, "-------------------------------------------------------------------------------------------",str(""))


        
        def search2():
            rows=backend_final.searchbackend(self.entry1.get())
            print (rows)
            for row in rows:
                display3.insert(END, row,str(""))

                
        
        f1 = Frame(root, background="bisque")
        f2 = Frame(root, background="bisque")
        

        f1.grid(row=0, column=0, sticky="nsew")
        f2.grid(row=1, column=0, sticky="nsew")
        root.grid_columnconfigure(0, weight=1)
       
        
        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=25)
        
        rootlabel=Label(f1, text="Hospital database ManagementSystem",font='bold',bg='bisque')
        rootlabel.grid(row=0, column=0, sticky="nsew")
        f1.grid_columnconfigure(0, weight=1)
        
        button_x = Button(f1,text='Back to Home Page',command= root.destroy,font='bold',bg= 'tan1')
        button_x.grid(row=0 ,column=4,sticky='e')
        
        df1= LabelFrame(f2,bg='bisque')
        df2= LabelFrame(f2,bg='bisque')
        
        df1.grid(row=0, column=0, sticky="nsew")
        df2.grid(row=1, column=0, sticky="nsew")
        
        f2.grid_rowconfigure(0, weight=1)
        f2.grid_rowconfigure(1, weight=1)
        f2.grid_columnconfigure(0, weight=1)
        
        
        label1=Label(df1,text= "Enter rec_id to get record details", padx=5,pady=5,bg="bisque")
        label1.grid(row=0,column=0)
        
        self.entry1=Entry(df1,bg="white")
        self.entry1.grid(row=0,column=1)
        
        searchbutton = Button(df1,text='search',command= search)
        searchbutton.grid(row=1,column=1)

        
        display=Listbox(df1,width='40',height='10')
        display.grid(row =2,column=0, sticky='ns', pady=8,columnspan=2)
        
        
        labelds=Label(df1,text= "Enter nurse_id to get nurse details", padx=5,pady=5,bg="bisque")
        labelds.grid(row=0,column=4)
       

        self.entryds=Entry(df1,bg="white")
        self.entryds.grid(row=0,column=5)
        
        searchbuttonds = Button(df1,text='search',command= searchds)
        searchbuttonds.grid(row=1,column=5)
        
        
        displayds=Listbox(df1,width='40',height='10')
        displayds.grid(row =2,column=5, sticky='ns', pady=8,columnspan=2)
        
        #buttonexit = Button(df1,text='EXIT',bg='tan1',command=root.destroy)
        #buttonexit.grid(row=15,column=5)
        

        
        


if __name__=='__main__':
    root = Tk()
    root.attributes('-fullscreen', True)
    application = hospital(root)
    root.mainloop()



