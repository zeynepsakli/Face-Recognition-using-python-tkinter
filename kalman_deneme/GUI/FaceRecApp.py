#### 2020 May #####
#### Prepared by Zeynep SAKLI #####
#### Contact: zeysaklii@gmail.com #####

import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
import xlwt
import numpy as np
import os
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter.messagebox
from tkinter.messagebox import showerror
from tkinter import *
from tkinter import messagebox, Label, Button, FALSE, Tk, Entry




class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title('Face Recogniser')
        self.window.configure(background='grey')
        self.window.bind('<Escape>', lambda e: window.quit())
        message = tkinter.Label(
            window, text="Face Recognition System by Zeynep SAKLI \n zeysaklii@gmail.com",
            bg="gray", fg="black", width=40,
            height=2, font=('Ariel', 20, 'bold'))
        message.place(x=400, y=550)
        #For display clock
        self.clock_label = tkinter.Label(window, font='ariel 20', bg='black', fg='red')
        self.clock_label.grid(row=0, column=0)
        self.display_time()
        self.clock_label.pack()
       #######################################################################################
        self.video_source = video_source
        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()
        #####################################################################################
        #For exit app
        self.quitWindow = tkinter.Button(window, text="Quit",
                                         command=self.cikis, fg="black", bg="gray",
                                         width=20, height=3, activebackground="Red",
                                         font=('Ariel', 15, ' bold '))
        self.quitWindow.place(x=1200, y=400)
        ######################################################################################
        #For get excel data
        self.getdata = tkinter.Button(window, text="Get Excel Data",
                                      command=self.openwindow, fg="black", bg="gray",
                                      width=20, height=3, activebackground="Red",
                                      font=('Ariel', 15, ' bold '))
        self.getdata.place(x=1200, y=200)
        #######################################################################################
        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 10
        self.update()
        self.window.mainloop()

    password = '1234'    #First password, used for changed if forgot
    #For multiple tkinter window
    def openwindow(self):
        self.top = Toplevel()
        self.top.title("Login Panel")
        self.top.geometry("300x300+120+120")
        self.top.resizable(width=FALSE, height=FALSE)
        username_text = Label(self.top, text="Username:").grid(row=10)
        self.username_guess = Entry(self.top)  #Get username to login
        self.username_guess.grid(row=10,column=1)
        password_text = Label(self.top, text="Password:").grid(row=15)
        #self.password_guess = Entry(self.top, show="*")
        self.e1 = Entry(self.top, show="")     #Get password to login
        self.e1.grid(row=15, column=1)

        button1 = Button(self.top, width=7, height=1, text="Show", command=self.Show) #Show password
        button1.grid(row=20, column=5, padx=3, pady=3)
        button2 = Button(self.top, width=7, height=1, text="Hide", command=self.Hide) #Hide password
        button2.grid(row=23, column=5, padx=3, pady=3)

        button3=Button(self.top, text="Forgot Password", command=self.cpass) #Forgot password button
        button3.grid(row=100, column=5, padx=3, pady=3)


        excel = Button(self.top, text="Excel",
                       command=self.excelfile, fg="black", bg="gray",
                       width=5, height=1, activebackground="Red",
                       font=('times', 9, ' bold '))
        excel.place(x=120, y=150)
        self.top.mainloop()
    #Show password and Hide Password functions
    def Show(self):
        e1 = Entry(self.top, show='')
        e1.grid(row=15, column=1)

    def Hide(self):
        e1 =Entry(self.top, show='*')
        e1.grid(row=15, column=1)
    ####################################################

    #Change password funcitons if Forgot

    def cpass(self):

        self.top.destroy()
        self.top = Toplevel()
        Label(self.top, text="Enter new password:").pack()
        passn = Entry(self.top, width=15)
        passn.pack()
        Button(self.top, text="OK", command=lambda: self.chgpass(passn.get())).pack()
        self.top.mainloop()

    def chgpass(self,newpass):

        self.password = newpass
        self.top.destroy()
        self.openwindow()
    #######################################################

    #Check match is okey and open excel file
    def excelfile(self):

        username = 'Zeynep'
        if self.username_guess.get() == username and self.e1.get() == self.password:
            message2 = tkinter.Label(
                self.top, text="Matching is correct",
                fg="green", width=15,
                height=3, font=('times', 10,))
            message2.place(x=100, y=100)

            filename = filedialog.askopenfilename(initialdir="D:/kalman_deneme/GUI/", title="select file")
            os.system(filename)


        else:

            message2 = tkinter.Label(
                self.top, text="Wrong Information",
                fg="red", width=15,
                height=3, font=('times', 10,))
            message2.place(x=100, y=100)
            messagebox.showinfo("--ERROR--", "--Username or Password is WRONG / Please try again", icon="warning")

    ###############################################################################################################
    def display_time(self):
        current_time = time.strftime('%Y-%m-%d %I:%M:%S:%p') #show with PM and AM
        self.clock_label['text'] = current_time
        self.window.after(1000, self.display_time)
    ############################################################################################
    #Quit app
    def cikis(self):
        quitask = tkinter.messagebox.askquestion("Quit", "Are you sure you want to quit?")
        if quitask == "yes":
            self.window.destroy()
    ############################################################################################
    #Part of Face recognition  functions
    def videotoimg(self):

        cap = cv2.VideoCapture(0)

        count = 0
        while True:
            ret, test_img = cap.read()
            if not ret:
                continue
            cv2.imwrite("frame%d.jpg" % count, test_img)  # save frame as JPG file
            count += 1
            resized_img = cv2.resize(test_img, (800, 600))
            # cv2.imshow('face detection Tutorial ', resized_img)
            # if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
            #   break

        cap.release()
        cv2.destroyAllWindows()

    def fr(self):
        def faceDetection(test_img):
            gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)  # convert color image to grayscale
            face_haar_cascade = cv2.CascadeClassifier(
                'HaarCascade/haarcascade_frontalface_default.xml')  # Load haar classifier
            faces = face_haar_cascade.detectMultiScale(gray_img, scaleFactor=1.32,
                                                       minNeighbors=5)  # detectMultiScale returns rectangles

            return faces, gray_img

        def labels_for_training_data(directory):
            faces = []
            faceID = []

            for path, subdirnames, filenames in os.walk(directory):
                for filename in filenames:
                    if filename.startswith("."):
                        print("Skipping system file")  # Skipping files that startwith .
                        continue

                    id = os.path.basename(path)  # fetching subdirectory names
                    img_path = os.path.join(path, filename)  # fetching image path
                    print("img_path:", img_path)
                    print("id:", id)
                    test_img = cv2.imread(img_path)  # loading each image one by one
                    if test_img is None:
                        print("Image not loaded properly")
                        continue
                    faces_rect, gray_img = faceDetection(
                        test_img)  # Calling faceDetection function to return faces detected in particular image

                    if len(faces_rect) != 1:
                        continue  # Since we are assuming only single person images are being fed to classifier
                    (x, y, w, h) = faces_rect[0]
                    roi_gray = gray_img[y:y + w,
                               x:x + h]  # cropping region of interest i.e. face area from grayscale image
                    faces.append(roi_gray)
                    faceID.append(int(id))
            return faces, faceID

        # Below function trains haar classifier and takes faces,faceID returned by previous function as its arguments
        def train_classifier(faces, faceID):
            face_recognizer = cv2.face.LBPHFaceRecognizer_create()
            face_recognizer.train(faces, np.array(faceID))
            return face_recognizer

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        self.window.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)

        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.workbook = xlwt.Workbook()
        self.sheet = self.workbook.add_sheet("Yoklama.xls", cell_overwrite_ok=True)
        self.style = xlwt.easyxf('font: bold 1, color red;')

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            face_recognizer = cv2.face.LBPHFaceRecognizer_create()
            face_recognizer.read('trainingData.yml')  # Load saved training data

            self.name = {0: "Tarkan", 1: "Zeynep Sakli"}
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face_haar_cascade = cv2.CascadeClassifier(
                    'HaarCascade/haarcascade_frontalface_default.xml')  # Load haar classifier

                faces = face_haar_cascade.detectMultiScale(gray_img, scaleFactor=1.32, minNeighbors=5)

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=5)

                resized_img = cv2.resize(frame, (1000, 700))
                # cv2.imshow('face detection Tutorial ',resized_img)
                # cv2.waitKey(10)

                for face in faces:
                    (x, y, w, h) = face
                    roi_gray = gray_img[y:y + w, x:x + h]
                    label, confidence = face_recognizer.predict(roi_gray)  # predicting the label of given image
                    print("confidence:", confidence)
                    print("label:", label)
                    (x, y, w, h) = face
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=5)
                    self.predicted_name = self.name[label]
                    if confidence < 1000:  # If confidence less than 37 then don't print predicted face text on screen
                        cv2.putText(frame, self.predicted_name, (x, y), cv2.QT_FONT_NORMAL, 1, (0, 0, 255), 2)
                    current2_time = time.strftime('%Y-%m-%d %H:%M:%S')
                    self.sheet.write(label, 1, current2_time, self.style)
                    self.sheet.write(label, 0, self.predicted_name, self.style)
                    self.workbook.save("Yoklama.xls")

                self.resized_img = cv2.resize(frame, (800, 600))

                return (ret, cv2.cvtColor(self.resized_img, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")
##################################################################################################################
