import tkinter
form=tkinter.Tk()
w=str(form.winfo_screenwidth())+'x'+str(form.winfo_screenheight())
form.title(w)
form.geometry('500x600')
form.mainloop()
