import tkinter
from tkinter import *
frm=tkinter.Tk()
frm.geometry('600x400')
lbl=tkinter.Label(frm,text='enter ur name',font=('arial',25))
btn=tkinter.Button(frm,text='click here',font=('arial',25))
lbl.grid(row=0,column=0)
btn.grid(row=1,column=50)
frm.mainloop()
