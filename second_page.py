from tkinter import *
from PIL import Image, ImageTk
import os
import PIL.Image
from tkinter import messagebox
import first_page,third_page


class FirstWin2():
    def __init__(self):
        self.root = Tk()

      # self.root.state('zoomed')
        self.root.title('2nd window')
        self.root.geometry('1366x768')
        self.img = PIL.Image.open(os.path.abspath("images\pic.jpg"))
        self.imgtk = ImageTk.PhotoImage(self.img)
        self.imgLbl = Label(self.root, image = self.imgtk)
        self.imgLbl.place(x = 0, y = 0)
        #self.frame1 = Frame(self.root, width = 600, height= 900, bg = '#ddeaf0')
        #self.frame1.place(x = 0, y = 0)
        self.lab=Label(self.root,text="You're never too young—or too old—to take care of your heart.Congratulations on taking an important step toward heart health today.",wraplength=400,fg="black",bg='#fbfbfb')
        self.lab.place(x=80,y=70)
        self.lab.config(font=("calibri",14))
        self.root.config(bg = '#fbfbfb')
        self.lab=Label(self.root,text="Quiz Instructions: \n1.This quiz consists of seven multiple-choice questions.\n2.Choose the best option for each question.\n3.After selecting an option, you'll receive immediate feedback as visualised form.\n4.Have fun and enjoy the quiz!Let's begin. ",wraplength=400,fg="black",bg='#fbfbfb')
        self.lab.place(x=80,y=250)
        self.lab.config(font=("calibri",14))
         #button
        self.btn=Button(self.root,text="BACK",bg="#7d96f0",fg="black",font="15",command=self.back1)
        self.btn.place(x=150,y=560,width="80")
        
        self.btn=Button(self.root,text="NEXT",bg="#7d96f0",fg="black",font="15",command=self.next1)
        self.btn.place(x=350,y=560,width="80")
        self.root.config(bg = '#fbfbfb')
        self.root.mainloop()


        #labels
    ''' self.lab=Label(self.root,text="Age",anchor=E,fg="black",bg='#fbfbfb')
        self.lab.place(x=440,y=150, width="70", height="45")
        self.lab.config(font=("BankGothic Lt BT",25,"bold"))
        self.lab=Label(self.root,text="Sex",anchor=E,fg="black",bg='#fbfbfb')
        self.lab.place(x=435,y=220, width="70", height="45")
        self.lab.config(font=("BankGothic Lt BT",25,"bold"))
        self.lab=Label(self.root,text="Height",anchor=E,fg="black",bg='#fbfbfb')
        self.lab.place(x=421,y=290, width="130", height="45")
        self.lab.config(font=("BankGothic Lt BT",25,"bold"))
        self.lab=Label(self.root,text="Weight",anchor=E,fg="black",bg='#fbfbfb')
        self.lab.place(x=431,y=360, width="130", height="45")
        self.lab.config(font=("BankGothic Lt BT",25,"bold"))
        self.lab=Label(self.root,text="Name",anchor=E,fg="black",bg='#fbfbfb')
        self.lab.place(x=440,y=430, width="100", height="45")
        self.lab.config(font=("BankGothic Lt BT",25,"bold"))
        #entries
        self.Age=StringVar()
        self.Age=Entry(self.root,textvariable=self.Age)
        self.Age.place(x=660,y=150,width=260,height=30)
        
        self.Sex=StringVar()
        self.Sex=Entry(self.root,textvariable=self.Sex)
        self.Sex.place(x=660,y=220,width=260,height=30)
        
        self.Height=StringVar()
        self.Height=Entry(self.root,textvariable=self.Height)
        self.Height.place(x=660,y=290,width=260,height=30)
        self.Weight=StringVar()
        self.Weight=Entry(self.root,textvariable=self.Weight)
        self.Weight.place(x=660,y=360,width=260,height=30)
        
        self.Name=StringVar()
        self.Name=Entry(self.root,textvariable=self.Name)
        self.Name.place(x=660,y=430,width=260,height=30)
        
        #button
        self.btn=Button(self.root,text="BACK",bg="#7d96f0",fg="black",font="15",command=self.back1)
        self.btn.place(x=500,y=560,width="80")
        
        self.btn=Button(self.root,text="NEXT",bg="#7d96f0",fg="black",font="15",command=self.bacl)
        self.btn.place(x=700,y=560,width="80")
        
        
        self.root.config(bg = '#fbfbfb')
        self.root.mainloop()
    def bacl(self):
      data=(self.Age.get(),
            self.Sex.get(),
            self.Weight.get(),
            self.Height.get(),
            self.Name.get()
            )
      if self.Age.get()=='' and type(self.Age.get()):
        messagebox.showinfo('Alert','please enter youre age')
      if self.Sex.get()=='':
        messagebox.showinfo('Alert','please enter youre sex')
      if self.Height.get()=='':
        messagebox.showinfo('Alert','please enter youre height')
      else:
          messagebox.showinfo('enter data successfully') 
          self.root.destroy()
          third_page.FirstWin3() '''
        
    def next1(self):
       self.root.destroy()
       third_page.FirstWin3()
    def back1(self):
      self.root.destroy()
      first_page.FirstWin1()
    
        
if __name__ == '__main__':        
    FirstWin2()
