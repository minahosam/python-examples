import tkinter
import mysql.connector
from tkinter import ttk
from tkinter import *
from tkinter import _setit
from tkinter import messagebox
frm=tkinter.Tk()
frm.geometry('600x600')
frm.update()
conn = mysql.connector.connect(host='localhost',user='userpython',passwd='123456')
cur = conn.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS mynewcompany DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci')
def createtable():
    conn=mysql.connector.connect(host='localhost',user='userpython',passwd='123456',database='mynewcompany')
    cur1=conn.cursor()
    is_created =cur1.execute('CREATE TABLE IF NOT EXISTS employee (empno int PRIMARY KEY,empname varchar(100),empaddress varchar(100),empsalary int)')
    print(is_created)
    if  is_created== None :
        tkinter.messagebox.showinfo('detail','created')
        #return True
pady=5
btn1=tkinter.ttk.Button(frm,text='create table',command=createtable,padding=pady)
btn1.config(width=20)
empno_var=IntVar()
empname_var=StringVar()
empaddress_var=StringVar()
empsalary_var=IntVar()
lbl1=tkinter.ttk.Label(frm,text='empno')
lbl1.config(justify='center')
txt1=tkinter.ttk.Entry(frm,textvariable=empno_var)
def number_only(txt1):
    if str.isdigit(txt1): return True
    elif txt1 == '':return True0
    else:return  False
reg_fun=frm.register(number_only)
def autonum(column,table):
    if 'conn' in globals():
        cur5=conn.cursor()
        cur5.execute("SELECT MAX(%s)+1 FROM (%s)"%(column,table))
        row=cur5.fetchone()
        if row[0]==None : return '1'
        else: return row[0]
    else:return ""
if createtable:empno_var.set(autonum('empno','mynewcompany.employee'))
txt1.configure(justify='center',validate='key',validatecommand=(reg_fun,'%P'),state='readonly')
lbl2=tkinter.ttk.Label(frm,text='emp name')
lbl2.configure(justify='center')
txt2=tkinter.ttk.Entry(frm,textvariable=empname_var)
txt2.configure(justify='center')
lbl3=tkinter.ttk.Label(frm,text='emp address')
lbl3.configure(justify='center')
txt3=tkinter.ttk.Entry(frm,textvariable=empaddress_var)
txt3.configure(justify='center')
lbl4=tkinter.ttk.Label(frm,text='emp salary')
lbl4.configure(justify='center')
txt4=tkinter.ttk.Entry(frm,textvariable=empsalary_var)
def validate_number(text):
    if str.isdigit(text): return True
    elif text == '':return True
    else:return False
reg_text=frm.register(validate_number)
txt4.configure(justify='center',validate='key',validatecommand=(reg_text,'%P'))
def clear_field():
    empno_var.set(autonum('empno','mynewcompany.employee'))
    empname_var.set('')
    empaddress_var.set('')
    empsalary_var.set('')
    txt2.focus()
    conn.commit()
    btn2.config(state='enable')
    btn4.config(state='disable')
    btn5.config(state='disable')
def add_employee():
    #if 'conn' in globals():
        #cur4=conn.cursor()
    if str(txt1.get()).strip()=='':
        tkinter.messagebox.showinfo('','empno is empty')
        txt1.focus()
        return False
    elif txt2.get().strip()=='':
        tkinter.messagebox.showinfo('','empname is empty')
        txt2.focus()
        return False
    elif txt3.get().strip()=='':
        tkinter.messagebox.showinfo('','empaddress is empty')
        txt3.focus()
        return False
    elif str(txt4.get()).strip()=='':
        tkinter.messagebox.showinfo('','empsalary is empty')
        txt4.focus()
        return False
    else:
        conn=mysql.connector.connect(host='localhost',user='userpython',passwd='123456',database='mynewcompany')
        cur1=conn.cursor()
        is_added=cur1.execute("insert into mynewcompany.employee values("+str(empno_var.get())+",'"+empname_var.get()+"','"+empaddress_var.get()+"',"+str(empsalary_var.get())+")")
        print(empname_var.get())
        if  is_added==None :
            tkinter.messagebox.showinfo('','added')
            conn.commit()
            #return True
            clear_field()
def find_empployee():
    frm1=tkinter.Toplevel()
    frm1.geometry('100x100')
    lb=tkinter.ttk.Label(frm1,text='enter employee no')
    tx=tkinter.ttk.Entry(frm1)
    tx.focus()
    def done():
        cur15=conn.cursor()
        cur15.execute("select * from mynewcompany.employee where empno = '"+tx.get()+"'")
        row=cur15.fetchall()
        if len(row)<1:
            tkinter.messagebox.showinfo('','not found')
        else:
            rows=row[0]
            empname_var.set(rows[1])
            empno_var.set(rows[0])
            empaddress_var.set(rows[2])
            empsalary_var.set(rows[3])
            print(row)
    bn=tkinter.ttk.Button(frm1,text='ok',command=done)
    btn2.config(state='disable')
    btn4.config(state='enable')
    btn5.config(state='enable')
    lb.pack()
    tx.pack()
    bn.pack()
    frm1.mainloop()
    #inbox=input()
    #enum1=input('',True)
def edit_employee():
    cur1=conn.cursor()
    is_edited=cur1.execute("update mynewcompany.employee set empname='"+empname_var.get()+"',empaddress='"+empaddress_var.get()+"',empsalary="+str(empsalary_var.get())+" where empno="+str(empno_var.get())+"")
    if is_edited==None:tkinter.messagebox.showinfo('','edited')
    conn.commit()
    clear_field()
def del_employee():
    if tkinter.messagebox.askyesno('attention','do you want to delete'):
        cur1=conn.cursor()
        is_del=cur1.execute("delete from mynewcompany.employee where empno="+str(empno_var.get())+"")
        if is_del==None:
            tkinter.messagebox.showinfo('','deleted')
    clear_field()
btn2=tkinter.ttk.Button(frm,text='add employee',command=add_employee)
btn2.config(width=20)
btn3=tkinter.ttk.Button(frm,text='find employee',command=find_empployee)
btn3.config(width=20)
btn4=tkinter.ttk.Button(frm,text='edit employee',command=edit_employee)
btn4.config(width=20)
btn5=tkinter.ttk.Button(frm,text='delete employee',command=del_employee)
btn5.config(width=20)
btn6=tkinter.ttk.Button(frm,text='clear fields',command=clear_field)
btn6.config(width=20)
btn7=tkinter.ttk.Button(frm,text='exit',command=lambda :frm.destroy())
btn7.config(width=20)
clear_field()
btn1.pack(pady=pady)
lbl1.pack(pady=pady)
txt1.pack(pady=pady)
lbl2.pack(pady=pady)
txt2.pack(pady=pady)
lbl3.pack(pady=pady)
txt3.pack(pady=pady)
lbl4.pack(pady=pady)
txt4.pack(pady=pady)
btn2.pack(pady=pady)
btn3.pack(pady=pady)
btn4.pack(pady=pady)
btn5.pack(pady=pady)
btn6.pack(pady=pady)
btn7.pack(pady=pady)
frm.mainloop()