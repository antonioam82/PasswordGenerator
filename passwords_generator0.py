from tkinter import *
import string
import sys
import time

class app:
    def __init__(self):
        self.root = Tk()
        self.root.title("CREATE YOU PASSWORD")
        self.root.geometry("899x320")

        self.your_password = StringVar()

        Entry(self.root,textvariable=self.your_password,font=('arial 20'),width=58).place(x=10,y=20)

        self.root.mainloop()


if __name__=="__main__":
    app()
