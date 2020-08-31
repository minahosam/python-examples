import tkinter
from tkinter import *
from tkinter import ttk
frm=tkinter.Tk()
frm.geometry('400x400')
def f(text):
    if txt.isdigit(text):
        return True
 #   elif text is '':
  #      return True
    else:
        return False
reg_fun=frm.register(f)
txt=tkinter.Entry(frm,validate='key',validatecommand=(reg_fun,'%P'))
txt.focus()
txt.pack()
frm.mainloop()