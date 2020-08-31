import tkinter
from tkinter import ttk
frm=tkinter.Tk()
frm.geometry('400x400')
def f():
    frm1=tkinter.Toplevel()
    frm1.grab_set()
btn1=tkinter.Button(frm,text='new frame',command=f)
btn1.pack()
frm.mainloop()