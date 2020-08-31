class person:
    name=''
    id=0
class employee(person):
    pass
class doctor(employee):
    pass
print(employee.__base__)
print(doctor.__base__)
print(person.__base__)
