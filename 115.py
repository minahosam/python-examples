class other:
    pass
class person:
    pass
class employee(person,other):
    pass
print(employee.__bases__)
