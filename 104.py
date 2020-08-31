class employee:
    name='m'
emp1=employee()
emp1.name='f'
delattr(emp1,'name')
print(emp1.name)
