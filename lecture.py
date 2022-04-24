import tkinter
from tkinter import *
import sys
import os
import csv
import win32api
from tkinter import ttk
from PIL import ImageTk, Image 
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
from tkinter import filedialog, messagebox, ttk
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
       self.TakeImagepg()

    def TakeImagepg(self):
        self.bg =ImageTk.PhotoImage(file='groundimages/student3.png')
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)

        #frame1=Frame(self.root, bg="#00aeff")
        #frame1.place(relx=0.05, rely=0.05, relwidth=0.80, relheight=0.90)

        frame1 = tk.LabelFrame(self.root, text="Excel Data",bg="skyblue")
        frame1.place(relx=0.05, rely=0.05, relwidth=0.80, relheight=0.65)

        # Frame for open file dialog
        file_frame = tk.LabelFrame(self.root, text="Open File",bg="skyblue")
        file_frame.place(relwidth=0.80, relheight=0.20, rely=0.70, relx=0.05)

# Buttons
        button1 = tk.Button(file_frame, text="Browse A File", command=lambda: self.File_dialog(),bg="#3ece48"  ,width=10,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        button1.place(rely=0.60, relx=0.15)

        button2 = tk.Button(file_frame, text="Load File", command=lambda: self.Load_excel_data(),bg="skyblue"  ,width=10,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        button2.place(rely=0.60, relx=0.35)

        button3 = tk.Button(file_frame, text="Print", command=lambda: self.print_file().grid(),bg="violet"  ,width=10,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        button3.place(rely=0.60, relx=0.55)
        

        #saveData = tk.Button(frame1, text="Save Profile",fg="white",command=self.dataSave  ,bg="#3ece48"  ,width=15 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        #saveData.place(x=30, y=395)
        #saveData = tk.Button(frame1, text="clear",fg="white",command=self.dataclear  ,bg="red"  ,width=15 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        #saveData.place(x=250, y=395)

# The file/file path text
        self.label_file = ttk.Label(file_frame, text="No File Selected")
        self.label_file.place(rely=0, relx=0)


## Treeview Widget
        self.tv1 = ttk.Treeview(frame1)
        self.tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

        treescrolly = tk.Scrollbar(frame1, orient="vertical", command=self.tv1.yview) # command means update the yaxis view of the widget
        treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=self.tv1.xview) # command means update the xaxis view of the widget
        self.tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
        treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
        treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget


    def File_dialog(self):
        """This Function will open the file explorer andassign the chosen file path to label_file"""
        filename = filedialog.askopenfilename(initialdir="/",title="Select A File",filetype=(("text files", "*.csv"),("All Files", "*.*")))
        self.label_file["text"] = filename 
        return None
    def print_file(self):
	
	# Ask for file (Which you want to print)
	    file_to_print = filedialog.askopenfilename(
	    initialdir="/", title="Select file",
	    filetypes=(("Text files", "*.csv"), ("all files", "*.*")))
	
	    if file_to_print:
		
		# Print Hard Copy of File
		    win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)

# Make Button


    def Load_excel_data(self):
        """If the file selected is valid this will load the file into the Treeview"""
        file_path =self.label_file["text"]
        try:
            excel_filename = r"{}".format(file_path)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)

        except ValueError:
            tk.messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        self.clear_data()
        self.tv1["column"] = list(df.columns)
        self.tv1["show"] = "headings"
        for column in self.tv1["columns"]:
            self.tv1.heading(column, text=column) # let the column heading = column name

        df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
        for row in df_rows:
            self.tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        return None


    def clear_data(self):
        self.tv1.delete()
        return None
        #*tv1.get_children()

root = Tk()
obj = Login(root)
root.mainloop()