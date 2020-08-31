import tkinter
from tkinter import ttk
frm=tkinter.Tk()
frm.geometry('600x400')
txt=tkinter.Entry(frm,background='blue')
ctb=ttk.Combobox(frm,values=('cairo','alex','aswan'),state='readonly')
def copy():
    x=ctb.get()
    x=txt
btn=tkinter.Button(frm,text='print',command=copy)
ctb.pack()
txt.pack()
btn.pack()
frm.mainloop()
