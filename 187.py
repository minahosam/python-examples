import tkinter
from tkinter import *
from tkinter import ttk
frm=tkinter.Tk()
frm.geometry('400x400')
def f():
    f=tkinter.Toplevel()
    f.geometry('200x200')
    lbl1=tkinter.Label(f,text='enter your name',font=20)
    sv=StringVar()
    txt1=tkinter.Entry(f,font=20,textvariable=sv)
    def p():
        txt1.bind('<Return>',lambda my:f.destroy())
        name=sv.get()
        print('hello' + name)
        f.destroy()
    btn2=tkinter.ttk.Button(f,text='ok',command=p)
    lbl1.pack()
    txt1.pack()
    btn2.pack()
    f.grab_set()
    txt1.focus()
    sv.get()
btn1=tkinter.ttk.Button(frm,text='test',command=f)
btn1.pack()
frm.mainloop()