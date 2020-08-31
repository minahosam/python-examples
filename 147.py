import tkinter
from tkinter import ttk
frm=tkinter.Tk()
frm.geometry('600x400')
svname=tkinter.StringVar()
txt=ttk.Entry(frm,foreground='blue',textvariable=svname)
svname.set('hello')
def f(word):
    svname.set(word)
btn=ttk.Button(frm,command=lambda:f('hi'))
txt.pack()
btn.pack()
frm.mainloop()
