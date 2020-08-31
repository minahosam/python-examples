import tkinter
frm=tkinter.Tk()
frm.geometry('600x800')
frm.update()
w=frm.winfo_width()
r=frm.winfo_height()
frm.title(str(w)+'*'+ str(r))
frm.mainloop()
