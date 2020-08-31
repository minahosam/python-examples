import tkinter
from tkinter import ttk
f=tkinter.Tk()
f.geometry('600x400')
s=ttk.Style()
s.configure('TLabel',background='red',foreground='blue',font=('arial',20))
z=ttk.Label(f,text='enter ur name',style='TLabel')
z.pack()
f.mainloop()
