class other:
    pass
class person:
    pass
class employee(person , other):
    pass
import inspect
print(inspect.getmro(employee))
