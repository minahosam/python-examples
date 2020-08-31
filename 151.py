import tkinter
from tkinter import *
frm=tkinter.Tk()
frm.geometry('600x400')
#v=StringVar()
#v.set(0)
v=BooleanVar()
cb=tkinter.Checkbutton(frm,text='agree',variable=v)
cb.pack()
def f():
    print(v.get())
btn=tkinter.Button(frm,text='ok',command=f)
btn.pack()
frm.mainloop()
