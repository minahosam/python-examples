import tkinter
from tkinter import ttk
from tkinter import *
frm = tkinter.Tk()
frm.geometry('400x400')
lbl1=tkinter.ttk.Entry(frm)
def f(event):
    print(event)
lbl1.bind('<Key>',f)
lbl1.pack()
frm.mainloop()