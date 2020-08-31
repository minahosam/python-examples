import tkinter
from tkinter import *
frm=tkinter.Tk()
frm.geometry('700x500')
canvas=tkinter.Canvas(frm,width=500,height=500)
canvas.pack()
img=tkinter.PhotoImage(file='giphy.gif')
canvas.create_image(0,0,image=img,anchor=NW)
frm.mainloop()
