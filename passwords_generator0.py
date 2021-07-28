from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import string
import random
import threading
import sys
import time

class app:
    def __init__(self):
        self.root = Tk()
        self.root.title("CREATE YOU PASSWORD")
        self.activated = True
        self.root.geometry("899x290")
        self.numbs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
                      25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,
                      47,48,49,50]
        
        self.your_password = StringVar()
        #validatecommand = self.root.register(self.valid_entry)

        Label(self.root,text="YOUR PASSWORD").place(x=10,y=20)
        Entry(self.root,textvariable=self.your_password,font=('arial 20'),width=58).place(x=10,y=40)
        Label(self.root,text="LENGTH:").place(x=10,y=100)
        self.stateLabel = Label(self.root,text="",width=127)
        self.stateLabel.place(x=2,y=131)
        self.btnCreate = Button(self.root,text="CREATE PASSWORD",width=123,height=2,command=self.init_task)
        self.btnCreate.place(x=12,y=158)
        Button(self.root,text="SAVE PASSWORD",width=123,height=2).place(x=12,y=208)
        self.len=ttk.Combobox(self.root,width=10,state="readonly")
        self.len.place(x=68,y=100)
        Label(self.root,text="MIN LOWERCASE:").place(x=210,y=100)
        self.min_low=ttk.Combobox(self.root,width=10,state="readonly")#validatecommand=(validatecommand,"%S"))
        self.min_low.place(x=313,y=100)
        Label(self.root,text="MIN UPPERCASE:").place(x=458,y=100)
        self.min_upp=ttk.Combobox(self.root,width=10,state="readonly")
        self.min_upp.place(x=560,y=100)
        Label(self.root,text="MIN NUMBERS:").place(x=710,y=100)
        self.min_num=ttk.Combobox(self.root,width=10,state="readonly")
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

    def genera_password(self):
        characts = string.ascii_letters+string.digits
        self.stateLabel.configure(text="LOOKING FOR YOUR PASSWORD...",fg="red")
        while self.activated == True:
            pswrd=("").join(random.choice(characts) for i in range(int(self.len.get())))
            print(pswrd)
            if(sum(c.islower() for c in pswrd)>=int(self.min_low.get())
                and sum(c.isupper() for c in pswrd)>=int(self.min_upp.get())
                and sum(c.isdigit() for c in pswrd)>=int(self.min_num.get())):
                #break
                self.activated = False
                
        self.stateLabel.configure(text="TASK COMPLETED.",fg="blue")
        if self.activated == False:
            self.btnCreate.configure(text="CREATE PASSWORD",command=self.init_task)
        self.your_password.set(pswrd)
        self.activated = True

    def cancel_process(self):
        self.activated = False

    def init_task(self):
        if int(self.min_low.get()) + int(self.min_upp.get()) + int(self.min_num.get()) <= int(self.len.get()):
            self.btnCreate.configure(text="CANCEL",command=self.cancel_process)
            t = threading.Thread(target=self.genera_password)
            t.start()
        else:
            messagebox.showwarning("ERROR","INVALID LENGHT")

if __name__=="__main__":
    app()
