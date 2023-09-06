from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
import os
import second_page

class FirstWin1():
    def __init__(self):
        self.root = Tk()

      # self.root.state('zoomed')
        self.root.title('First Window')
        self.root.geometry('1366x768')

        # place the widgets

        self.img = PIL.Image.open(os.path.abspath("images\doctor.jpg"))
        self.imgtk = ImageTk.PhotoImage(self.img)
        self.imgLbl = Label(self.root, image = self.imgtk)
        self.imgLbl.place(x = 0, y = 0)
        self.frame1 = Frame(self.root, width = 600, height= 900, bg = '#ddeaf0')
        self.frame1.place(x = 0, y = 0)

        self.headLbl = Label(self.frame1, text = 'CardioCare', bg = '#7d96f0', fg = 'black', font = ('BankGothic Md BT', 30, 'bold'))
        #self.headLbl.pack()
        self.headLbl.place(x = 160, y = 90)
        # text
        self.lab=Label(self.frame1,text="Are you up to speed on all things related to heart health?\nTake our quiz to gauge your understanding and learn something new along the way.",wraplength=400,justify=LEFT,bg="#ddeaf0",fg="black")
        self.lab.place(x=20,y=150, width="630", height="420",)
        self.lab.config(font=("calibri",14))
        
       # button
        self.btn=Button(self.frame1,text="NEXT",bg="#7d96f0",fg="black",font="15",command=self.next1)
        self.btn.place(x=250,y=600,width="80")
       
        self.root.mainloop()
    
    def next1(self):
        self.root.destroy()
        second_page.FirstWin2()
  
        
if __name__ == '__main__':
  FirstWin1()
