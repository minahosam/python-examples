import tkinter
from  tkinter import *
frm=tkinter.Tk()
frm.geometry('600x400')
lbx=tkinter.Listbox(frm)
txt=tkinter.Entry(frm)
def f():
    x=lbx.get(ACTIVE)
    txt=print(x)
btn=tkinter.Button(frm,text='ok',command = f )
lbx.insert(0,'cairo')
lbx.insert(1,'alex')
lbx.insert(2,'giza')
#lbx.delete('giza')
lbx.pack()
txt.pack()
btn.pack()
frm.mainloop()
