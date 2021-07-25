from tkinter import *
from tkinter import ttk
import string
import sys
import time

class app:
    def __init__(self):
        self.root = Tk()
        self.root.title("CREATE YOU PASSWORD")
        self.root.geometry("899x320")
        self.numbs = [0,1,2,3,4,5,6,7,8,9,10]
        

        self.your_password = StringVar()
        #self.length=IntVar()

        Entry(self.root,textvariable=self.your_password,font=('arial 20'),width=58).place(x=10,y=40)
        Label(self.root,text="LENGTH:").place(x=10,y=100)
        Button(self.root,text="CREATE PASSWORD",width=123,height=2).place(x=12,y=190)
        self.len=ttk.Combobox(self.root,width=10)
        self.len.place(x=68,y=100)
        Label(self.root,text="MIN LOWERCASE:").place(x=210,y=100)
        self.min_low=ttk.Combobox(self.root,width=10)
        self.min_low.place(x=313,y=100)
        Label(self.root,text="MIN UPPERCASE:").place(x=468,y=100)
        self.min_upp=ttk.Combobox(self.root,width=10)
        self.min_upp.place(x=570,y=100)
        Label(self.root,text="MIN NUMBERS:").place(x=710,y=100)
        self.min_num=ttk.Combobox(self.root,width=10)
        self.min_num.place(x=802,y=100)
        self.len["values"]=self.numbs
        self.len.set(8)
        self.min_low["values"]=self.numbs
        self.min_low.set(0)
        self.min_upp["values"]=self.numbs
        self.min_upp.set(0)
        self.min_num["values"]=self.numbs
        self.min_num.set(0)

        self.root.mainloop()


if __name__=="__main__":
    app()
