import tkinter
from tkinter import *
import sys
import os
import csv
from PIL import ImageTk, Image 
from tkinter import messagebox
import pymysql
import datetime
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
from cv2 import cv2
import numpy as np
import pandas as pd

#from train import #findEncodings, markAttendance
from functools import partial
class Login:
    def __init__(self, root):
       self.root=root
       self.img=PhotoImage(file='C://Users//Admin//Pictures//Camera Roll//uoemlogo.png')
       self.root.iconphoto(False,self.img)
       self.root.title("UNIVERSITY OF EMBU CLASS ATTENDANCE SYSTEM")
       self.root.geometry('1199x600+50+50')
       self.root.resizable(False, False)
       self.loginform()
    def loginform(self):
        self.bg =ImageTk.PhotoImage(file='groundimages/student3.png')
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1) 
         #Frame_login = Frame(self.root, bg="white")
         #Frame_login.place(x=300, y=200, width=1366, height=700)

        frame_input=Frame(self.root, bg="white")
        frame_input.place(x=320,y=130, height=450, width=350)

        label1=Label(frame_input,text="login here", font=("impact", 25, "bold"), fg = "blue", bg ="white")
        label1.place(x=75, y=20)
           
        label2=Label(frame_input,text="Username", font=("Goudy old style", 25, "bold"), fg = "orangered", bg ="white")
        label2.place(x=30, y=95)
      
        self.username=Entry(frame_input, font=("times new roman", 15, "bold"),bg="lightgray")
        self.username.place(x=30,y=145,width=270,height=35)

        label3=Label(frame_input, text="password", font=("Goudy old style", 20, "bold"), fg = "orangered", bg ="white")
        label3.place(x=30, y=195)

        self.email_txt=Entry(frame_input, font=("times new roman", 15, "bold"),bg="lightgray")
        self.email_txt.place(x=30,y=145,width=270,height=35)
           
        self.password=Entry(frame_input,font=("times new roman", 15, "bold"),bg="lightgray")
        self.password.place(x=30,y=245,width=270,height=35)

        btn1=Button(frame_input, cursor="hand2", text="forgot password?", font=("calibri", 15), fg = "green", bd=0)
        btn1.place(x=30, y=280)

        btn2=Button(frame_input, cursor="hand2", text="Login",command=self.login, font=("new times roman", 15), fg = "white", bg ="orangered", bd=0, width=15, height=1)
        btn2.place(x=50, y=340)

        btn3=Button(frame_input, cursor="hand2", text="Register",command=self.Register, font=("calibri", 15), fg = "white", bg ="blue", bd=0)
        btn3.place(x=110, y=390)

    def login(self):
        if self.email_txt.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","all fields are required", parent=self.root)
        else:
            try:
                con= pymysql.connect(host='localhost', user='root', password='root', database='student')
                cur=con.cursor()
                cur.execute('select * from register where emailid= %s and password= %s', (self.email_txt.get(),self.password.get()))
                row=cur.fetchone()
                if row == None:
                   messagebox.showerror('Error','Invalid user name or password', parent= self.root)
                   self.loginclear()
                   self.email_txt.focus()
                else:
                    self.appscreen()
                    con.close()
            except Exception as es:
                messagebox.showerror("Error",f'Error Due to: {str(es)}', parent=self.root)
    def Register(self):
        Frame_login1 = Frame(self.root, bg="white")
        Frame_login1.place(x=0, y=0, width=1366, height=700)

        #self.bg =ImageTk.PhotoImage(file='groundimages/student3.jpg')
        #self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1) 
        #self.img =ImageTk.PhotoImage(file='sttrain/mutuma .jpg')
        #img=Label(Frame_login, image=self.img).place(x=0, y=0, relwidth=1, relheight=1)

        frame_input2=Frame(self.root, bg="#00aeff")
        frame_input2.place(x=320,y=130, height=450, width=630)

        label1=Label(frame_input2,text="Register Here", font=("impact", 20, "bold"), fg = "black", bg ="white")
        label1.place(x=40, y=20)

        label2=Label(frame_input2,text="username", font=("Goudy old style", 20, "bold"), fg = "orangered", bg ="white")
        label2.place(x=30, y=95)
        
        self.entry=Entry(frame_input2,font=("times new roman", 15, "bold"),bg="lightgray")
        self.entry.place(x=30,y=145,width=270,height=35)

        label4=Label(frame_input2,text="Registration Number", font=("Goudy old style", 20, "bold"), fg = "orangered", bg ="white")
        label4.place(x=330, y=95)
        self.entry2=Entry(frame_input2,font=("times new roman", 15, "bold"),bg="lightgray")
        self.entry2.place(x=330,y=145,width=270,height=35)

        label5=Label(frame_input2,text="Enter password", font=("Goudy old style", 20, "bold"), fg = "orangered", bg ="white")
        label5.place(x=30, y=195)
        self.entry3=Entry(frame_input2,font=("times new roman", 15, "bold"),bg="lightgray")
        self.entry3.place(x=30,y=245,width=270,height=35)

        label5=Label(frame_input2,text="Confirm password", font=("Goudy old style", 20, "bold"), fg = "orangered", bg ="white")
        label5.place(x=330, y=195)
        self.entry4=Entry(frame_input2,font=("times new roman", 15, "bold"),bg="lightgray")
        self.entry4.place(x=330,y=245,width=270,height=35)

        btn2=Button(frame_input2, cursor="hand2", text="Register", command=self.register, font=("new times roman", 15), fg = "white", bg ="orangered", bd=0, width=15, height=1)
        btn2.place(x=90, y=340)
        
        btn3=Button(frame_input2, cursor="hand2", text="Already Registered? Login", command=self.loginform, font=("calibri", 10), fg = "white", bg ="black", bd=0)
        btn3.place(x=110, y=390)
    
    def register(self):
        if self.entry.get()=="" or self.entry2.get()=="" or self.entry3.get()=="" or self.entry4.get()=="":
                   messagebox.showerror("Error","all fields are required", parent=self.root)
        elif self.entry3.get()!=self.entry4.get():
            messagebox.showerror("Error","password and confirm password should be same", parent=self.root)
        else:
            try:
                con= pymysql.connect(host="localhost", user="root", password="root", database="student")
                cur=con.cursor()
                cur.execute('select * from register where emailid= %s ', self.entry2.get())
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","User already exist please try again with another email", parent=self.root)
                    self.regclear()
                    self.entry.focus()
                else:
                    cur.execute('insert into register values(%s, %s, %s, %s)', (self.entry.get(), self.entry2.get(), self.entry3.get(), self.entry4.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","registration succeful", parent=self.root)
                    self.regclear()
            except Exception as es:
                         messagebox.showerror("Error",f'Error Due to: {str(es)}', parent=self.root)
                         

    def appscreen(self):
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1366)

            
        btn2=Button(Frame_login, cursor="hand2", text="Lecture", command=self.Lecture, font=("new times roman", 15), fg = "white", bg ="green", bd=0)
        btn2.place(x=150, y=100) 
            
        btn2=Button(Frame_login, cursor="hand2", text="Class Representative", command=self.ClassRep, font=("new times roman", 15), fg = "white", bg ="green", bd=0)
        btn2.place(x=150, y=160)

        btn2=Button(Frame_login, cursor="hand2", text="Student Attendance Data", command=self.Student, font=("new times roman", 15), fg = "white", bg ="green", bd=0)
        btn2.place(x=150, y=220) 

        btn2=Button(Frame_login, cursor="hand2", text="Student Attendance", command=self.Student1, font=("new times roman", 15), fg = "white", bg ="green", bd=0)
        btn2.place(x=150, y=280)

        btn2=Button(Frame_login, cursor="hand2", text="logout", command=self.loginform, font=("new times roman", 15), fg = "white", bg ="orangered", bd=0)
        btn2.place(x=1000, y=10) 
            
    def Lecture(self):
        Frame_login1 = Frame(self.root, bg="white")
        Frame_login1.place(x=0, y=0, width=1000, height=450)

        ###########lecture to view the Attendance#################
        os.system('python "C://Users//Admin//Desktop//hezytush//lecture.py"')

        btn2=Button(Frame_login1, cursor="hand2", text="EXIT", command=self.appscreen, font=("new times roman", 15), fg = "white", bg ="BLUE", bd=0)
        btn2.place(x=800, y=10) 
    def ClassRep(self):
        Frame_login1 = Frame(self.root, bg="white")
        Frame_login1.place(x=0, y=0, width=1000, height=450)
        
        #################rep to enter class details###########
        os.system('python "C://Users//Admin//Desktop//hezytush//classrep.py"')

        btn2=Button(Frame_login1, cursor="hand2", text="EXIT", command=self.appscreen, font=("new times roman", 15), fg = "white", bg ="BLUE", bd=0)
        btn2.place(x=800, y=10)

    def Student(self):
        Frame_login1 = Frame(self.root, bg="white")
        Frame_login1.place(x=0, y=0, width=1000, height=450)

        #############calling the student registration details.###################

        os.system('python "C://Users//Admin//Desktop//hezytush//TakeImg.py"')

        btn2=Button(Frame_login1, cursor="hand2", text="EXIT", command=self.appscreen, font=("new times roman", 15), fg = "white", bg ="BLUE", bd=0)
        btn2.place(x=800, y=10)

        ####################Attend class here##################################

    def Student1(self):
        Frame_login1 = Frame(self.root, bg="white")
        Frame_login1.place(x=0, y=0, width=1000, height=450)
        os.system('python "C://Users//Admin//Desktop//hezytush//Attendance.py"')

        btn2=Button(Frame_login1, cursor="hand2", text="EXIT", command=self.appscreen, font=("new times roman", 15), fg = "white", bg ="BLUE", bd=0)
        btn2.place(x=800, y=10)

    def regclear(self):
        self.entry.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)
        self.entry4.delete(0,END)

    def loginclear(self): 
        self.email_txt.delete(0,END)
        self.password.delete(0,END)
         


root = Tk()
obj = Login(root)
root.mainloop()
