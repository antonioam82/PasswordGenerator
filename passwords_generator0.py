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

        self.your_password = StringVar()
        self.length=IntVar()

        Entry(self.root,textvariable=self.your_password,font=('arial 20'),width=58).place(x=10,y=20)
        Label(self.root,text="LENGTH:").place(x=10,y=100)
        self.len=ttk.Combobox(self.root,width=10).place(x=68,y=100)
        Label(self.root,text="MIN LOWERCASE:").place(x=240,y=100)
        self.min_low=ttk.Combobox(self.root,width=10).place(x=346,y=100)

        self.root.mainloop()


if __name__=="__main__":
    app()
