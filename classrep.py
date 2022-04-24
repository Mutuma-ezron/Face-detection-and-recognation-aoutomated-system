import tkinter
from tkinter import *
import sys
import os
import csv
from PIL import ImageTk, Image 
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time

from functools import partial
class Login:
    def __init__(self, root):
       self.root=root
       self.img=PhotoImage(file='C://Users//Admin//Pictures//Camera Roll//uoemlogo.png')
       self.root.iconphoto(False,self.img)
       self.root.title("UNIVERSITY OF EMBU CLASS ATTENDANCE SYSTEM")
       self.root.geometry('1199x600+50+50')
       self.root.resizable(False, False)
       self.ClassReppg()

    def ClassReppg(self):
        self.bg =ImageTk.PhotoImage(file='groundimages/student3.png')
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)
        
        frame1=Frame(self.root, bg="#00aeff")
        frame1.place(relx=0.30, rely=0.17, relwidth=0.38, relheight=0.80)

        ############class rep to Enter class details####################
        head2 = Label(frame1, text="Enter Class Details", fg="black",bg="#3ece48" ,font=('times', 17, ' bold ') )
        head2.grid(row=0,column=0)

        lbl = Label(frame1, text="Enter Unit Name",width=20  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
        lbl.place(x=80, y=55)

        self.txt = Entry(frame1,width=35 ,fg="black",font=('times', 15, ' bold '))
        self.txt.place(x=30, y=88)

        lbl2 = Label(frame1, text="Enter Unit Code",width=20  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
        lbl2.place(x=80, y=140)

        self.txt2 = Entry(frame1,width=35 ,fg="black",font=('times', 15, ' bold ')  )
        self.txt2.place(x=30, y=173)

        lbl2 = Label(frame1, text="Enter Total Student ",width=20  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
        lbl2.place(x=80, y=225)

        self.txt3 = Entry(frame1,width=35 ,fg="black",font=('times', 15, ' bold ')  )
        self.txt3.place(x=30, y=258)

        lbl2 = Label(frame1, text="Enter Class Venue",width=20  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
        lbl2.place(x=80, y=310)

        self.txt4 = Entry(frame1,width=35 ,fg="black",font=('times', 15, ' bold ')  )
        self.txt4.place(x=30, y=343)

        saveData = tk.Button(frame1, text="Save Profile",fg="white",command=self.dataSave  ,bg="#3ece48"  ,width=15 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        saveData.place(x=30, y=395)
        saveData = tk.Button(frame1, text="clear",fg="white",command=self.dataclear  ,bg="red"  ,width=15 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        saveData.place(x=250, y=395)

    def assure_path_exists(path):
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                os.makedirs(dir)

    def dataSave(self):
        def assure_path_exists(path):
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                os.makedirs(dir)
        columns = ['UNIT NAME.', '', 'UNIT CODE', '', 'TOTAL STUDENT', 'CLASS VENUE']
        columns1=[self.txt.get(),self.txt2.get(),self.txt3.get(),self.txt4.get()]
        assure_path_exists("ClassDetails/")
        serial = 0
        exists = os.path.isfile("ClassDetails\ClassDetails.csv")
        if exists:
            with open("ClassDetails\ClassDetails.csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(columns1)
                serial = 1
            csvFile1.close()
            
        else:
            with open("ClassDetails\ClassDetails.csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    serial = serial + 1
            serial = (serial // 2)
            csvFile1.close()

        Id = (self.txt.get())
        name = (self.txt2.get())
        total = (self.txt3.get())
        venue = (self.txt4.get())

    def dataclear(self):
        self.txt.delete(0,END)
        self.txt2.delete(0,END)
        self.txt3.delete(0,END)
        self.txt4.delete(0,END)

root = Tk()
obj = Login(root)
root.mainloop()