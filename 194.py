import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

frm = tkinter.Tk()
frm.geometry('400x400')


def f():
    num1 = inbox('enter number 1:', True)
    num2 = inbox('enter number 2 :', True)
    r = int(num1) + int(num2)
    messagebox.showinfo('addition', str(r))


btn = tkinter.ttk.Button(frm, text='add', command=f)
btn.pack()
frm.mainloop()
