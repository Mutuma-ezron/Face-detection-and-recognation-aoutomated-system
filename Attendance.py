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
       self.TakeImagepg()

    def TakeImagepg(self):
        self.bg =ImageTk.PhotoImage(file='groundimages/student3.png')
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)
        
        frame1=Frame(self.root, bg="#00aeff")
        frame1.place(relx=0.30, rely=0.17, relwidth=0.38, relheight=0.80)



        head1 = Label(frame1, text="For Already Registered", fg="black",bg="#3ece48" ,font=('times', 17, ' bold ') )
        head1.place(x=0,y=0)

        trackImg = Button(frame1, text="Take Attendance", command=self.TrackImages  ,fg="black"  ,bg="yellow"  ,width=30  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        trackImg.place(x=30,y=50)
        quitWindow = Button(frame1, text="Quit", command=self.root.destroy, fg="black"  ,bg="red"  ,width=30 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        quitWindow.place(x=30, y=400)



    def check_haarcascadefile(self):
        exists = os.path.isfile("haarcascade_frontalface_default.xml")
        if exists:
            pass
        else:
            mess._show(title='Some file missing', message='Please contact us for help')
            self.root.destroy()

    def getImagesAndLabels(path):
    # get the path of all the files in the folder
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
        faces = []
    # create empty ID list
        Ids = []
    # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
        # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
            ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(ID)
        return faces, Ids
        
    def TrackImages(self):
        def assure_path_exists(path):
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                os.makedirs(dir)
        self.check_haarcascadefile()
        assure_path_exists("Attendance/")
        assure_path_exists("StudentDetails/")
        msg = ''
        i = 0
        j = 0
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
        if exists3:
            recognizer.read("TrainingImageLabel\Trainner.yml")
        else:
            mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
            return
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)

        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
        exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
        if exists1:
            df = pd.read_csv("StudentDetails\StudentDetails.csv")
        else:
            mess._show(title='Details Missing', message='Students details are missing, please check!')
            cam.release()
            cv2.destroyAllWindows()
            self.root.destroy()
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                    ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                    ID = str(ID)
                    ID = ID[1:-1]
                    bb = str(aa)
                    bb = bb[2:-2]
                    attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]
                else:
                    Id = 'Unknown'
                    bb = str(Id)
                cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
            cv2.imshow('Taking Attendance', im)
            if (cv2.waitKey(1) == ord('q')):
                break
        cam.release()
        cv2.destroyAllWindows()
        attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
        exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
        if exists:
            with open("Attendance\Attendance_"+ date +".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(attendance)
            csvFile1.close()
            
        else:
            with open("Attendance\Attendance_"+ date +".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(attendance)
                print(attendance)
            csvFile1.close()
        
        cam.release()
        cv2.destroyAllWindows()



root = Tk()
obj = Login(root)
root.mainloop()