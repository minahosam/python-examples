import tkinter
from tkinter import ttk
from tkinter import messagebox
frm=tkinter.Tk()
frm.config(background='black')
frm.geometry('400x400')
def f():
    ask=messagebox.askokcancel('','test')
    lbl1['text']=(ask)
lbl1=tkinter.Label(frm,text='test',background='yellow',foreground='red')
txt1=tkinter.Entry(frm)
btn1=tkinter.Button(frm,text='ok',background='yellow',foreground='red',command=f)
lbl1.pack()
btn1.pack()
txt1.pack()
frm.mainloop()