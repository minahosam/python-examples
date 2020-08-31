import tkinter
from tkinter import ttk
frm=tkinter.Tk()
frm.geometry('600x600')
lbl1=ttk.Label(frm,text='label1')
lbl2=ttk.Label(frm,text='label2',background='red')
lbl1.pack()
lbl2.pack()
frm.mainloop()
