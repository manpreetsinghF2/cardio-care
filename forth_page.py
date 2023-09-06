from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
import fiveth_page,third_page
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


class FirstWin4():
    def __init__(self):
        self.type = 'BMI'
        self.df = pd.read_csv('heart01.csv')
        self.root = Tk()

      # self.root.state('zoomed')
        self.root.title('4CardioCare')
        self.root.geometry('1366x768')
        self.frame1 = Frame(self.root, width = 600, height= 900, bg = 'white')
        self.frame1.place(x = 800, y = 0)
        self.frame4 = Frame(self.frame1, width = 600, height = 900, bg = 'white')
        self.frame4.place(x = 0, y = 70)
        self.frame5 = Frame(self.frame1, width = 600, height = 500, bg = 'white')
        self.frame5.place(x = 0, y = 470)
        # self.frame5.grid(row = 1, column=0, sticky='nsew')
        #frames
        self.frame2 = Frame(self.root, width = 800, height= 350, bg = '#121236')
        self.frame2.place(x = 0, y = 0)
        self.frame3 = Frame(self.root, width = 800, height= 350, bg = '#121236')
        self.frame3.place(x = 0, y = 350)

        #labels
        self.lab=Label(self.frame2,text="BodyMassIndex",fg="#92e0a9",bg='#121236')
        self.lab.place(x=30,y=10)
        self.lab.config(font=("BankGothic Lt BT",30))
        
        self.lab=Label(self.frame3,text="Check Cholesterol Regularly",fg="#92e0a9",bg='#121236')
        self.lab.place(x=30,y=10)
        self.lab.config(font=("BankGothic Lt BT",30))
        
        self.BMI = StringVar(self.frame2)
 
        # Dictionary to create multiple buttons
       # values = {"Below 18.5(Underweight)" : "1",
       #         "18.5-24.9(Normal weight)" : "2","25.0-29.9(Normal weight)":"3","30.0-34.9(Obesity class|":"4","35.#0-39.9(Obesity class||":'5',"Above 40(Obesity class|||)":'6'}
        values={'below 18.5':"underweight",'18.5-24.9':"normal weight",'25.0-29.9':'overweight','30.0-34.9 or high':'obese range'}         
        y = 90
        for (text, value) in values.items():
            Radiobutton(self.frame2, text = text, variable = self.BMI,
                        value = value, indicator = 0, font = ('', 10, 'bold'),
                         width=50, pady=7, padx=100,bg='#9ba5f2',command=lambda : self.heartGraph('BMI')).place(x = 30, y = y)
            y += 35
       #3rd frame
        self.CheckCholesterol = StringVar(self.frame3)
        values = {"Yes,Within two weeks of every month" : "1",
                "No,If doctor says only" : "2"}
                 
        y = 90
        for (text, value) in values.items():
            Radiobutton(self.frame3, text = text, variable = self.CheckCholesterol,
                        value = value, indicator = 0, font = ('', 10, 'bold'),
                         width=50, pady=7, padx=100,bg="#9ba5f2",command=lambda : self.heartGraph('checkcholesterol')).place(x = 30, y = y)
            y += 35
        
        self.nextbtn=Button(self.frame3,text="BACK",bg="#7d96f0",fg="black",font="15",command=self.back2)
        self.nextbtn.place(x=250,y=260,width="80")
        self.backbtn=Button(self.frame3,text="NEXT",bg="#7d96f0",fg="black",font="15",command=self.next2)
        self.backbtn.place(x=460,y=260,width="80")
        self.backbtn=Button(self.frame1,text="Diabetes",bg="#7d96f0",fg="black",font="15", command = lambda : self.diabeteGraph())
        self.backbtn.place(x=120,y=20,width="80")
        self.backbtn=Button(self.frame1,text="Heart Attack",bg="#7d96f0",fg="black",font="15", command= lambda : self.heartGraph(self.type))
        self.backbtn.place(x=350,y=20,width="120")
        
        
        self.root.mainloop()
    def next2(self):
        self.root.destroy()
        fiveth_page.FirstWin5()

    def back2(self):
        self.root.destroy()
        third_page.FirstWin3()
    def heartGraph(self, type):
        self.type = type
        print('type is ', type, 'froms is ')
            
        print(type)
        self.fig = Figure(figsize = (5, 6),
                    dpi = 100)
        #df[df.BMI < 18.0]
        #df[(df.BMI < 25.0) & (df.BMI >= 18.0) ]
        #df[(df.BMI < 29.9) & (df.BMI >= 25.0) ]
        #df[(df.BMI < 34.9) & (df.BMI >= 30.0) ]
        #df[(df.BMI > 34.9)]
        if type == 'BMI':
            print('bmi graph')
            for i in self.frame4.winfo_children():
                i.destroy()
        # list of squares
            mylabels = ['below 18.5','18.5-24.9','25.0-29.9','30.0-34.9 or high']
            y = ([(self.df[self.df.BMI < 18.0]) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0],
            self.df[((self.df['BMI'] >= 18.5) & (self.df['BMI'] <= 24.9)) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0])
        
        else:
            for i in self.frame5.winfo_children():
                i.destroy()
            mylabels = ['Check Cholesterol regularly', 'Not Check Cholesterol regularly']
            y = (self.df[(self.df['CholCheck'] == 1.0) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0],
            self.df[(self.df['CholCheck'] == 0.0) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0])

        self.plotGraph(y, mylabels, 'Risk of heart disease', self.frame4 if self.type == 'BMI' else self.frame5)
        # adding the subplot
    def diabeteGraph(self):
        print('self.type is ', self.type)
        if self.type == 'BMI':
            for i in self.frame4.winfo_children():
                i.destroy()
            
            mylabels = ['good BMI', 'Non-BMI']
            y = (self.df[(self.df['BMI'] == 1.0) & (self.df['Diabetes_012'] == 2)].shape[0], 
            self.df[(self.df['BMI'] == 0.0) & (self.df['Diabetes_012'] == 2)].shape[0])
            
        else:
            for i in self.frame5.winfo_children():
                i.destroy()
   
            mylabels = ['check chloesterol regularly', 'Not check cholesterol']
            y = (self.df[(self.df['CholCheck'] == 1.0) & (self.df['Diabetes_012'] == 2)].shape[0],
               self.df[(self.df['CholCheck'] == 0.0) & (self.df['Diabetes_012'] == 2)].shape[0])               

        self.plotGraph(y, mylabels, 'Risk of diabetes', self.frame4 if self.type == 'BMI' else self.frame5)        

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
        plot1 = self.fig.add_subplot(111)
    
        # plotting the graph
        plot1.pie(y, labels = mylabels, startangle = 90, autopct='%.2f')
        plot1.legend()
        self.canvas = FigureCanvasTkAgg(self.fig,
                                master = self.frame4)  
        self.canvas.draw()
    
        # placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().place(x = 0, y = 0)
    
            
if __name__ == '__main__':        
    FirstWin4()

    
