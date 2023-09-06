from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
import nineth_page, seventh_page
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


class FirstWin8():
    def __init__(self):
        self.type = 'alcohol'
        self.df = pd.read_csv('heart01.csv')
        self.root = Tk()

      # self.root.state('zoomed')
        self.root.title('8CardioCare')
        self.root.geometry('1366x768')
        self.frame1 = Frame(self.root, width = 600, height= 900, bg = 'white')
        self.frame1.place(x = 800, y = 0)
        self.frame4 = Frame(self.frame1, width = 600, height = 900, bg = 'white')
        self.frame4.place(x = 0, y = 70)
        self.frame5 = Frame(self.frame1, width = 600, height = 500, bg = 'white')
        self.frame5.place(x = 0, y = 470)
        #frames
        self.frame2 = Frame(self.root, width = 800, height= 350, bg = '#121236')
        self.frame2.place(x = 0, y = 0)
        self.frame3 = Frame(self.root, width = 800, height= 350, bg = '#121236')
        self.frame3.place(x = 0, y = 350)

        #labels
        self.lab=Label(self.frame2,text="Heavy Alcohol Consume",fg="#92e0a9",bg='#121236')
        self.lab.place(x=25,y=10)
        self.lab.config(font=("BankGothic Lt BT",30))
        
        self.lab=Label(self.frame3,text="Any Health Care",fg="#92e0a9",bg='#121236')
        self.lab.place(x=30,y=10)
        self.lab.config(font=("BankGothic Lt BT",30))
        
        self.stroke = StringVar(self.frame2)
 
        # Dictionary to create multiple buttons
        self.hvyalco = StringVar(self.frame2)
        values = {"Yes" : "1",
                "No" : "2"}
                 
        y = 90
        for (text, value) in values.items():
            Radiobutton(self.frame2, text = text, variable = self.hvyalco,
                        value = value, indicator = 0, font = ('', 10, 'bold'),
                         width=50, pady=7, padx=100,bg='#7d96f0',command=lambda:self.heartGraph('alcohol')).place(x = 30, y = y)
            y += 35
       #3rd frame
        self.anyhlt = StringVar(self.frame3)
        values = {"Yes" : "1",
                "No" : "2"}
                 
        y = 90
        for (text, value) in values.items():
            Radiobutton(self.frame3, text = text, variable = self.anyhlt,
                        value = value, indicator = 0, font = ('', 10, 'bold'),
                         width=50, pady=7, padx=100,bg="#7d96f0",command=lambda:self.heartGraph('AnyHealthcare')).place(x = 30, y = y)
            y += 35
        
        self.nextbtn=Button(self.frame3,text="BACK",bg="#7d96f0",fg="black",font="15",command=self.back1)
        self.nextbtn.place(x=250,y=260,width="80")
        self.backbtn=Button(self.frame3,text="NEXT",bg="#7d96f0",fg="black",font="15",command=self.next1)
        self.backbtn.place(x=460,y=260,width="80")
        self.backbtn=Button(self.frame1,text="Diabetes",bg="#7d96f0",fg="black",font="15", command = lambda : self.diabeteGraph())
        self.backbtn.place(x=120,y=20,width="80")
        self.backbtn=Button(self.frame1,text="Heart Attack",bg="#7d96f0",fg="black",font="15", command= lambda : self.heartGraph(self.type,))
        self.backbtn.place(x=350,y=20,width="120")
        
        
        
        self.root.mainloop()
    def next1(self):
        self.root.destroy()
        nineth_page.FirstWin9()
    def back1(self):
        self.root.destroy()
        seventh_page.FirstWin7()
    def heartGraph(self, type):
        self.type = type
        print('type is ', type, 'froms is ')
            
    
        if type == 'alcohol':
            for i in self.frame4.winfo_children():
                i.destroy()
        # list of squares
            mylabels = ['Heavy consumption', 'Non-heavy consumption']
            y = (self.df[(self.df['HvyAlcoholConsump'] == 1.0) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0],
            self.df[(self.df['HvyAlcoholConsump'] == 0.0) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0])
        
        else:
            for i in self.frame5.winfo_children():
                i.destroy()
            mylabels = ['AnyHealthcare', 'Not having Anyhealthcare']
            y = (self.df[(self.df['AnyHealthcare'] == 1.0) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0],
            self.df[(self.df['AnyHealthcare'] == 0.0) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0])

    
        self.plotGraph(y, mylabels, 'Risk of heart disease', self.frame4 if self.type == 'alcohol' else self.frame5)
        
    
    def diabeteGraph(self):
        print('self.type is ', self.type)
        if self.type == 'alcohol':
            for i in self.frame4.winfo_children():
                i.destroy()
            
            mylabels = ['Heavy consumption', 'Non-heavy consumption']
            y = (self.df[(self.df['HvyAlcoholConsump'] == 1.0) & (self.df['Diabetes_012'] == 2)].shape[0], 
            self.df[(self.df['HvyAlcoholConsump'] == 0.0) & (self.df['Diabetes_012'] == 2)].shape[0])
            
        else:
            for i in self.frame5.winfo_children():
                i.destroy()
   
            mylabels = ['AnyHealthCare', 'Not AnyHealthCare']
            y = (self.df[(self.df['AnyHealthcare'] == 1.0) & (self.df['Diabetes_012'] == 2)].shape[0],
               self.df[(self.df['AnyHealthcare'] == 0.0) & (self.df['Diabetes_012'] == 2)].shape[0])               

        self.plotGraph(y, mylabels, 'Risk of diabetes', self.frame4 if self.type == 'alcohol' else self.frame5)        

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
    FirstWin8()