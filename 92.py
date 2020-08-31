class employee:
    empname=[]
    empadress=[]
    empid=[]
    empsalary=[]
    def empinfo(mine):
        return mine.empname , mine.empadress ,mine.empid,mine.empsalary
    def printd(mine):
        print(mine.empinfo())

emp=employee()
for i in range(3):
    emp.empname.extend(input('enter employe name'))
    emp.empadress.extend(input('enter employee address'))
    emp.empid.extend(input('enter employee id'))
    emp.empsalary.extend(input('enter employ salary'))
emp.printd()
input('p e t e')
