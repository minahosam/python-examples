import tkinter
from tkinter import ttk
frm=tkinter.Tk()
frm.geometry('600x400')
txt1=ttk.Entry(frm,font=('arial',25))
txt2=ttk.Entry(frm,font=('arial',25))
def sum():
    x=int(txt1.get())+int(txt2.get())
    print(x)
btn=ttk.Button(frm,text='sum',command=sum)
txt1.pack()
txt2.pack()
btn.pack()
frm.mainloop()
