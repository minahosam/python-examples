import tkinter
from tkinter import messagebox
from tkinter import ttk

frm = tkinter.Tk()
frm.geometry('600x400')


def test():
    tkinter.messagebox.showinfo('', 'new entry')


txt = tkinter.ttk.Entry(frm)
txt.focus()
btn=tkinter.Button(frm,text='ok',command=test)
btn1 = tkinter.ttk.Button(frm, text='ok', command=test)
txt.pack()
txt.bind('<Return>', lambda x: test())
btn.pack()
btn1.pack()
frm.mainloop()
