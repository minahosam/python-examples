import tkinter
from tkinter import ttk
from tkinter import *
frm=tkinter.Tk()
frm.geometry('400x400')
menu=tkinter.Menu(frm)
filemenu=tkinter.Menu(menu,tearoff=0)
filemenu.add_command(label='new',command=lambda :print('new'))
filemenu.add_separator()
filemenu.add_command(label='save',command=lambda :print('save'))
menu.add_cascade(label='file',menu=filemenu)
frm.config(menu=menu)
frm.mainloop()