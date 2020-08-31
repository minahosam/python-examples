class person:
    name='person'
    address='giza'
    id=0
    def printdata(self):
        print(self.name+ ' ' +self.address+' '+str(self.id))
class employee(person):
    pass
emp1=employee()
emp1.printdata()
