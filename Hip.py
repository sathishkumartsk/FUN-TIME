import random
from tkinter import *
from random import randint
import time
import threading

root = Tk()
root.attributes("-alpha",0)
root.overrideredirect(1)
root.attributes("-topmost",1)

def placewindows():
    while True:
        win=toplevel(root)
        win.geometry("300*60+"+str(randint(0,root.winfo_screenwidth()-300))+"+"+str(randing(0,root.winfo_screenheight()-60)))
        win.overrideredirct(1)
        labe(win,text="Me_T_SK_",fg="black").place(relx=.38,rely=.3)
        win.lift()
        win.attributes("-topmost", true)
        win.attributes("-topmost", false)
        root.lift()
        root.attributes("-topmost",true)
        root.attributes("-topmost",false)
        tim.sleep(.05)

        threading.Thread(targer=plcewwindows).start()

        root.mainloop()

