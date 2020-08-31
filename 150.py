import tkinter
from tkinter import *
frm=tkinter.Tk()
frm.geometry('600x400')
#v=IntVar()
v=StringVar()
v.set(0)
rdbm=tkinter.Radiobutton(frm,text='male',value='male',variable=v)
rdbf=tkinter.Radiobutton(frm,text='female',value='female',variable=v)
def f():
    print(v.get())
btn=tkinter.Button(frm,command=f)
rdbm.pack()
rdbf.pack()
btn.pack()
frm.mainloop()
