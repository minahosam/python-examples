import tkinter
from tkinter import messagebox
from tkinter import ttk
frm=tkinter.Tk()
frm.geometry('600x400')
txt1=ttk.Entry(frm,font=('arial',25))
txt2=ttk.Entry(frm,font=('arial',25))
def sum():
    txt1.get()==[1,2,3]
    messagebox.showerror('error','not aviable')
btn=ttk.Button(frm,text='sum',command=sum)
txt1.pack()
txt2.pack()
btn.pack()
frm.mainloop()
