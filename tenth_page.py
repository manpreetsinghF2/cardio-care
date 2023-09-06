from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
import nineth_page
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
class FirstWin10():
    def __init__(self):
        self.type = 'MentHlth'
        self.df = pd.read_csv('heart01.csv')
        self.root = Tk()

      # self.root.state('zoomed')
        self.root.title('10CardioCare')
        self.root.geometry('1366x768')
        self.frame1 = Frame(self.root, width = 600, height= 900, bg = 'white')
        self.frame1.place(x = 800, y = 0)
        self.frame4 = Frame(self.frame1, width = 600, height = 900, bg = 'white')
        self.frame4.place(x = 0, y = 70)
        
        #frames
        self.frame2 = Frame(self.root, width = 800, height= 350, bg = '#121236')
        self.frame2.place(x = 0, y = 0)
        self.frame3 = Frame(self.root, width = 800, height= 350, bg = '#121236')
        self.frame3.place(x = 0, y = 350)
        self.frame5 = Frame(self.frame1, width = 600, height = 500, bg = 'pink')
        self.frame5.place(x = 0, y = 470)

        #labels
        self.lab=Label(self.frame2,text="Days of poor mental health last 30 days", wraplength=800,fg="#92e0a9",bg='#121236')
        self.lab.place(x=25,y=10)
        self.lab.config(font=("BankGothic Lt BT",30))
        
        self.lab=Label(self.frame3,text="Physical illness or injury days in last 30 days", wraplength=800,fg="#92e0a9",bg='#121236')
        self.lab.place(x=30,y=10)
        self.lab.config(font=("BankGothic Lt BT",30))
        
        self.stroke = StringVar(self.frame2)
 
        # Dictionary to create multiple buttons
        self.menhealth = StringVar(self.frame2)
        values = {"Less than 10 days": 10, "10-20 days": 20, "20-30 days": 30}
                 
        y = 90
        for (text, value) in values.items():
            Radiobutton(self.frame2, text = text, variable = self.menhealth,
                        value = value, indicator = 0, font = ('', 10, 'bold'),
                         width=50, pady=7, padx=100,bg='#7d96f0',command=lambda:self.heartGraph('MentHlth')).place(x = 30, y = y)
            y += 35
       #3rd frame
        self.phyhealth = StringVar(self.frame3)
        values = {"less than 10 days": 10, "10-20 days": 20, "20-30 days": 30}
                 
        y = 90
        for (text, value) in values.items():
            Radiobutton(self.frame3, text = text, variable = self.phyhealth,
                        value = value, indicator = 0, font = ('', 10, 'bold'),
                         width=50, pady=7, padx=100,bg='#7d96f0',command=lambda:self.heartGraph('PhysHlth')).place(x = 30, y = y)
            y += 35
        
        self.nextbtn=Button(self.frame3,text="BACK",bg="#7d96f0",fg="black",font="15",command=self.back1)
        # self.nextbtn.place(x=250,y=290,width="80")
        self.backbtn=Button(self.frame3,text="EXIT",bg="#7d96f0",fg="black",font="15",command=self.root.destroy)
        self.backbtn.place(x=320,y=290,width="80")
        self.backbtn=Button(self.frame1,text="Diabetes",bg="#7d96f0",fg="black",font="15", command = lambda : self.diabeteGraph())
        self.backbtn.place(x=120,y=20,width="80")
        self.backbtn=Button(self.frame1,text="Heart Attack",bg="#7d96f0",fg="black",font="15", command= lambda : self.heartGraph(self.type,))
        self.backbtn.place(x=350,y=20,width="120")
        
        
        self.root.mainloop()
    def back1(self):
        self.root.destroy()
        nineth_page.FirstWin9()
    def heartGraph(self, type):
        self.type = type
        print('type is ', type, 'froms is ')
            
    
        if type == 'MentHlth':
            for i in self.frame4.winfo_children():
                i.destroy()
        # list of squares
            mylabels = ["Less than 10 days","10-20 days","20-30 days"]
            y = (self.df[(self.df['MentHlth'].between(0, 9)) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0],
            self.df[(self.df['MentHlth'].between(10, 20)) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0], self.df[(self.df['MentHlth'].between(20, 30)) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0])
        
        else:
            for i in self.frame5.winfo_children():
                i.destroy()
            mylabels = ["Less than 10 days","10-20 days","20-30 days"]

            y = (self.df[(self.df['PhysHlth'].between(0, 9)) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0],
            self.df[(self.df['PhysHlth'].between(10, 20)) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0], self.df[(self.df['PhysHlth'].between(20, 30)) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0])

    
        self.plotGraph(y, mylabels, 'Risk of heart disease', self.frame4 if self.type == 'MentHlth'  else self.frame5)
        
    
    def diabeteGraph(self):
        print('self.type is ', self.type)
        if self.type == 'MentHlth':
            for i in self.frame4.winfo_children():
                i.destroy()
            
            mylabels = ["Less than 10 days","10-20 days","20-30 days"]

            y = (self.df[(self.df['MentHlth'].between(0, 9)) & (self.df['Diabetes_012'] == 2)].shape[0], 
            self.df[(self.df['MentHlth'].between(10, 20)) & (self.df['Diabetes_012'] == 2)].shape[0], self.df[(self.df['MentHlth'].between(20, 30)) & (self.df['Diabetes_012'] == 2)].shape[0])
            
        else:
            for i in self.frame5.winfo_children():
                i.destroy()
   
            mylabels = ["Less than 10 days","10-20 days","20-30 days"]

            y = (self.df[(self.df['PhysHlth'].between(0, 9)) & (self.df['Diabetes_012'] == 2)].shape[0],
            self.df[(self.df['PhysHlth'].between(10, 20)) & (self.df['Diabetes_012'] == 2)].shape[0], self.df[(self.df['PhysHlth'].between(20, 30)) & (self.df['Diabetes_012'] == 2)].shape[0])           

        self.plotGraph(y, mylabels, 'Risk of diabetes', self.frame4 if self.type == 'MentHlth' else self.frame5)        

    def plotGraph(self, y, mylabels, title, frame):
        self.fig = Figure(figsize = (4.5, 3.5),
                    dpi = 100)
        plot1 = self.fig.add_subplot(111)

        plot1.pie(y, labels = mylabels, startangle = 90, autopct='%.2f%%')
        plot1.legend()
        plot1.set_title(title)
        self.fig.subplots_adjust(left=0.05, bottom=0.07, right=0.95, top = 0.95, wspace=0, hspace=0)
        self.canvas = FigureCanvasTkAgg(self.fig,
                                master = frame)  
        self.canvas.draw()
    
        # placing the canvas on the Tkinter window
        # self.canvas.get_tk_widget().place(x = 0, y = 0)
        self.canvas.get_tk_widget().grid(row = 0)
        
if __name__ == '__main__':
     FirstWin10()