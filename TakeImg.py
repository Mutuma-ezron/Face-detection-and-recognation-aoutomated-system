import tkinter
from tkinter import *
import sys
import os
import csv
from PIL import ImageTk, Image 
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
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
        
        frame2=Frame(self.root, bg="#00aeff")
        frame2.place(relx=0.30, rely=0.17, relwidth=0.38, relheight=0.80)

        head2 = Label(frame2, text="For New Registrations", fg="black",bg="#3ece48" ,font=('times', 17, ' bold ') )
        head2.grid(row=0,column=0)

        lbl = Label(frame2, text="Enter ID",width=20  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
        lbl.place(x=80, y=55)

        self.txt = Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold '))
        self.txt.place(x=30, y=88)

        lbl2 = Label(frame2, text="Enter Name",width=20  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
        lbl2.place(x=80, y=140)

        self.txt2 = Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
        self.txt2.place(x=30, y=173)

        self.message1 = Label(frame2, text="1)Take Images  >>>  2)Save Profile" ,bg="#00aeff" ,fg="black"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
        self.message1.place(x=7, y=230)

        self.message = Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
        self.message.place(x=7, y=450)

        res=0
        exists = os.path.isfile("StudentDetails\StudentDetails.csv")
        if exists:
            with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                 res = res + 1
            res = (res // 2) - 1
            csvFile1.close()
        else:
            res = 0
        self.message.configure(text='Total Registrations till now  : '+str(res))



###################### BUTTONS ##################################  
        takeImg = Button(frame2, text="Take Images", command=self.TakeImages, fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        takeImg.place(x=30, y=300)
        quitWindow = Button(frame2, text="Quit", command=self.root.destroy, fg="black"  ,bg="red"  ,width=34, height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        quitWindow.place(x=30, y=350)



##################################################################################

    def tick(self):
        time_string = time.strftime('%H:%M:%S')
        clock.config(text=time_string)
        clock.after(200,tick)

###################################################################################

    def contact(self):
        mess._show(title='Contact us', message="Please contact us on : 'shubhamkumar8180323@gmail.com' ")

###################################################################################

    def check_haarcascadefile(self):
        exists = os.path.isfile("haarcascade_frontalface_default.xml")
        if exists:
            pass
        else:
            mess._show(title='Some file missing', message='Please contact us for help')
            root.destroy()

#######################################################################################

    def TakeImages(self):
        def assure_path_exists(path):
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                os.makedirs(dir)
        self.check_haarcascadefile()
        columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
        assure_path_exists("StudentDetails/")
        assure_path_exists("TrainingImage/")
        serial = 0
        exists = os.path.isfile("StudentDetails\StudentDetails.csv")
        if exists:
            with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    serial = serial + 1
            serial = (serial // 2)
            csvFile1.close()
        else:
            with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(columns)
                serial = 1
            csvFile1.close()
        Id = (self.txt.get())
        name = (self.txt2.get())
        if ((name.isalpha()) or (' ' in name)):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sampleNum = 0
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                    sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                # display the frame
                    cv2.imshow('Taking Images', img)
            # wait for 100 miliseconds
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
            # break if the sample number is morethan 100
                elif sampleNum > 9:
                    break
            cam.release()
            cv2.destroyAllWindows()
            res = "Images Taken for ID : " + Id
            row = [serial, '', Id, '', name]
            with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            self.message1.configure(text=res)
        else:
            if (name.isalpha() == False):
                res = "Enter Correct name"
                self.message.configure(text=res)

########################################################################################

    def TrainImages():
        self.check_haarcascadefile()
        assure_path_exists("TrainingImageLabel/")
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        faces, ID = getImagesAndLabels("TrainingImage")
        try:
            recognizer.train(faces, np.array(ID))
        except:
            mess._show(title='No Registrations', message='Please Register someone first!!!')
            return
        recognizer.save("TrainingImageLabel\Trainner.yml")
        res = "Profile Saved Successfully"
        self.message1.configure(text=res)
        self.message.configure(text='Total Registrations till now  : ' + str(ID[0]))

############################################################################################3

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


root = Tk()
obj = Login(root)
root.mainloop()