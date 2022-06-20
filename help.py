from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginition System")
        
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman",35,"bold"),bg="white",fg = "darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height = 45)
        
        img_top = Image.open(r"C:/Users/sharm/OneDrive/Desktop/Face Recognition System/College_Images/college_images/1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top = img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top,master=root)
        
        f_lbl = Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        dev_lbl=Label(f_lbl,text="Email:yadav.tanya151002@gmail.com",font=("times new roman",15,"bold"))
        dev_lbl.place(x=550,y=220)
        
        
if __name__=="__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
