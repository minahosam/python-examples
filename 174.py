import tkinter
frm=tkinter.Tk()
frm.geometry('400x400')
lbl1=tkinter.Label(frm,text='ppppppppp')
controls=frm.winfo_children()
for f in controls:
    print(f)
frm.mainloop()