def test():
    print('clicked')
import tkinter
from tkinter import ttk
frm=tkinter.Tk()
frm.geometry('600x400')
frm.config(background='lightblue')
lbl=ttk.Label(frm,text='e y n',font=('arial',20),background='red',foreground='blue')
txt=ttk.Entry(frm)
btn=ttk.Button(frm,text='click here',command=test)
lbl.pack()
txt.pack()
btn.pack()
frm.mainloop()
