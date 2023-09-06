from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
import sixth_page, forth_page
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class FirstWin5():
    def __init__(self):
        self.type = 'diffwalk'
        self.df = pd.read_csv('heart01.csv')
        self.root = Tk()

      # self.root.state('zoomed')
        self.root.title('5CardioCare')
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
        self.lab=Label(self.frame2,text="Difficult to Walk",fg="#92e0a9",bg='#121236')
        self.lab.place(x=30,y=10)
        self.lab.config(font=("BankGothic Lt BT",30))
        
        self.lab=Label(self.frame3,text="Education(1-6)",fg="#92e0a9",bg='#121236')
        self.lab.place(x=30,y=0)
        self.lab.config(font=("BankGothic Lt BT",30))
        
        self.BMI = StringVar(self.frame2)
 
        # Dictionary to create multiple buttons
        self.difficult= StringVar(self.frame2)
        values = {"Yes" : "1",
                "No" : "2"}
                 
        y = 90
        for (text, value) in values.items():
            Radiobutton(self.frame2, text = text, variable = self.difficult,
                        value = value, indicator = 0, font = ('', 10, 'bold'),
                         width=50, pady=7, padx=100,bg='#9ba5f2',command=lambda :self.heartGraph('diffwalk')).place(x = 30, y = y)
            y += 35
       #3rd frame
        self.education = StringVar(self.frame3)
        values = {"1-Never attened school or any kidergarten" : "1",
                "2-Grade 1 to 8" : "2","3-Grade 9 to 11" : "3","4-Grade 12 or high scool graduate" : "4","5-College 1 yr to 3 yr" : "5","6-College 4 yr or more" : "6"}
                 
        y = 60
        for (text, value) in values.items():
            Radiobutton(self.frame3, text = text, variable = self.education,
                        value = value, indicator = 0, font = ('', 10, 'bold'),
                         width=50, pady=7, padx=100,bg='#9ba5f2',command=lambda :self.heartGraph('education')).place(x = 30, y = y)
            y += 35
        
        self.nextbtn=Button(self.frame3,text="BACK",bg="#7d96f0",fg="black",font="15",command=self.back1)
        self.nextbtn.place(x=250,y=300,width="80")
        self.backbtn=Button(self.frame3,text="NEXT",bg="#7d96f0",fg="black",font="15",command=self.next1)
        self.backbtn.place(x=460,y=300,width="80")
        self.backbtn=Button(self.frame1,text="Diabetes",bg="#7d96f0",fg="black",font="15", command = lambda : self.diabeteGraph())
        self.backbtn.place(x=120,y=20,width="80")
        self.backbtn=Button(self.frame1,text="Heart Attack",bg="#7d96f0",fg="black",font="15", command= lambda : self.heartGraph(self.type))
        self.backbtn.place(x=350,y=20,width="120")
        
    
        
        
        
        self.root.mainloop()
    def back1(self):
        self.root.destroy()
        forth_page.FirstWin4()

    def next1(self):
        self.root.destroy()
        sixth_page.FirstWin6()
    def heartGraph(self, type):
        self.type = type
        print('type is ', type, 'froms is ')
            
       # print(type)
       # self.fig = Figure(figsize = (5, 6),
        #            dpi = 100)
    
    
        if type == 'diffwalk':
            for i in self.frame4.winfo_children():
                i.destroy()
        # list of squares
            mylabels = ['difficult', 'Not difficult']
            y = (self.df[(self.df['DiffWalk'] == 1.0) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0],
            self.df[(self.df['DiffWalk'] == 0.0) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0])

        else:
            for i in self.frame5.winfo_children():
                i.destroy()
            mylabels = ["Never attened school", "Grade 1 to 8", "Grade 9 to 11","Grade 12","College - 1yr-3 yr","College - 4yr or more"]
            y = (self.df[(self.df['Education'] == 1.0) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0],
            self.df[(self.df['Education'] == 2.0) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0], self.df[(self.df['Education'] == 3.0) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0], self.df[(self.df['Education'] == 4.0) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0], self.df[(self.df['Education'] == 5.0) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0], self.df[(self.df['Education'] == 6.0) & (self.df['HeartDiseaseorAttack'] == 1.0)].shape[0])
         # adding the subplot
        self.plotGraph(y, mylabels, 'Risk of heart disease', self.frame4 if self.type == 'diffwalk' else self.frame5)
        
    def diabeteGraph(self):
        print('self.type is ', self.type)
        if self.type == 'diffwalk':
            for i in self.frame4.winfo_children():
                i.destroy()
            
            mylabels = ['difficult', 'Not-difficult']
            y = (self.df[(self.df['DiffWalk'] == 1.0) & (self.df['Diabetes_012'] == 2)].shape[0], 
            self.df[(self.df['DiffWalk'] == 0.0) & (self.df['Diabetes_012'] == 2)].shape[0])
            
        else:
            for i in self.frame5.winfo_children():
                i.destroy()
   
            mylabels = ["Never attened school", "Grade 1 to 8", "Grade 9 to 11","Grade 12","College - 1yr-3 yr","College - 4yr or more"]
            y = (self.df[(self.df['Education'] == 1.0) & (self.df['Diabetes_012'] == 2)].shape[0],
            self.df[(self.df['Education'] == 2.0) & (self.df['Diabetes_012'] == 2)].shape[0], self.df[(self.df['Education'] == 3.0) & (self.df['Diabetes_012'] == 2)].shape[0], self.df[(self.df['Education'] == 4.0) & (self.df['Diabetes_012'] == 2)].shape[0], self.df[(self.df['Education'] == 5.0) & (self.df['Diabetes_012'] == 2)].shape[0], self.df[(self.df['Education'] == 6.0) & (self.df['Diabetes_012'] == 2)].shape[0])       

        self.plotGraph(y, mylabels, 'Risk of diabetes', self.frame4 if self.type == 'diffwalk' else self.frame5)        

    def plotGraph(self, y, mylabels, title, frame):
        self.fig = Figure(figsize = (4.8, 3.5),
                    dpi = 100)
        plot1 = self.fig.add_subplot(111)

        plot1.pie(y, labels = mylabels if self.type == 'diffwalk' else None, startangle = 90, autopct='%.2f%%')
        plot1.legend(labels = mylabels, loc='upper right') 
        plot1.set_title(title)
        self.fig.subplots_adjust(left=0.05, bottom=0.07, right=0.95, top = 0.95, wspace=0, hspace=0)
        self.canvas = FigureCanvasTkAgg(self.fig,
                                master = frame)  
        self.canvas.draw()
    
        # placing the canvas on the Tkinter window
        # self.canvas.get_tk_widget().place(x = 0, y = 0)
        self.canvas.get_tk_widget().grid(row = 0)


    
if __name__ == '__main__':           
    FirstWin5()