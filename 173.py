import tkinter
from tkinter import ttk
frm=tkinter.Tk()
frm.geometry('400x400')
lbl=tkinter.Label(frm,text='newentry',font=20)
def hide():
    lbl.pack_forget()
def show():
    lbl.pack()
btn1=tkinter.Button(frm,text='show',command=show)
btn2=tkinter.Button(frm,text='hide',command=hide)
btn1.pack()
btn2.pack()
frm.mainloop()