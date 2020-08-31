import tkinter
from tkinter import messagebox
from tkinter import ttk
frm=tkinter.Tk()
frm.geometry('500x400')
def m():
    if txt1.get().strip()=='':
        messagebox.showerror('','enter name')
        txt1.focus()
    elif txt2.get().strip()=='':
        messagebox.showerror('','enter code')
        txt2.focus()
    elif txt3.get().strip()=='':
        messagebox.showerror('','enter adress')
        txt3.focus()
    else:
        filename=txt1.get()+'.txt'
        f=open(filename,'w+')
        f.write('name :'+txt1.get()+'\n')
        f.write('code :',txt2.get()+'\n')
        f.write('address :',txt3.get()+'\n')
        f.close()
        messagebox.showinfo('','created....')
        txt1.focus()
def f():
    exit()
lble=tkinter.Label(frm,text='employee data',font='20')
lbl1=tkinter.Label(frm,text='name',font='20')
txt1=tkinter.Entry(frm,font='20')
lbl2=tkinter.Label(frm,text='code',font='20')
txt2=tkinter.Entry(frm,font='20')
lbl3=tkinter.Label(frm,text='adress',font='20')
txt3=tkinter.Entry(frm,font='20')
frm1=tkinter.Frame(frm)
btn1=tkinter.Button(frm1,text='create employee file now',font='20',command=m)
btn2=tkinter.Button(frm1,text='exit now',font='20',command=f)
lble.grid(row=0,column=1)
lbl1.grid(row=1,column=0)
txt1.grid(row=1,column=1)
lbl2.grid(row=2,column=0)
txt2.grid(row=2,column=1)
lbl3.grid(row=3,column=0)
txt3.grid(row=3,column=1)
frm1.grid(row=4,column=0,columnspan=2)
btn1.grid(row=0,column=1)
btn2.grid(row=1,column=1)
frm.mainloop()