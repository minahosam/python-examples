import tkinter
from tkinter import ttk
frm=tkinter.Tk()
frm.geometry('600x400')
r=0
def f():
    r=int(txt1.get())+int(txt2.get())
    lbl3['text']=(str(txt1.get())+"+"+str(txt2.get())+'='+str(r))
def x():
    r=int(txt1.get())*int(txt2.get())
    lbl3['text']=(str(txt1.get())+'*'+str(txt2.get())+'='+str(r))
def m():
    r=int(txt1.get())-int(txt2.get())
    lbl3['text']=(str(txt1.get())+'-'+str(txt2.get())+'='+str(r))
def d():
    r=int(txt1.get())/int(txt2.get())
    lbl3['text']=(str(txt1.get())+'/'+str(txt2.get())+'='+str(r))
frame=tkinter.Frame(frm)
lbl1=tkinter.Label(frm,text='Number 1',font='20')
lbl2=tkinter.Label(frm,text='Numbefr 2',font='20')
txt1=tkinter.Entry(frm,font='20')
txt2=tkinter.Entry(frm,font='20')
btn1=tkinter.Button(frame,text='+',width=5,command=f)
btn2=tkinter.Button(frame,text='-',width=5,command=m)
btn3=tkinter.Button(frame,text='*',width=5,command=x)
btn4=tkinter.Button(frame,text='/',width=5,command=d)
frame1=tkinter.Frame(frm)
lbl3=tkinter.Label(frame1,text=r,font='20')
lbl1.grid(row=0,column=0,padx=5,pady=5)
txt1.grid(row=0,column=2)
lbl2.grid(row=1,column=0,padx=5,pady=5)
txt2.grid(row=1,column=2)
frame.grid(row=2,column=0,columnspan=3)
btn1.grid(row=0,column=0,padx=20,pady=10)
btn2.grid(row=0,column=1,padx=20,pady=10)
btn3.grid(row=0,column=3,padx=20,pady=10)
btn4.grid(row=0,column=4,padx=20,pady=10)
frame1.grid(row=3,column=0,columnspan=4)
lbl3.grid(row=0,column=0)
frm.mainloop()