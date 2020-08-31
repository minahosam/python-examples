import tkinter
from tkinter import ttk
frm=tkinter.Tk()
frm.geometry('600x400')
lbl1=ttk.Label(frm,text='label 1',background='red',foreground='blue',font=('arial',20),padding=(20,50,10,10))
lbl1.pack()
frm.mainloop()
