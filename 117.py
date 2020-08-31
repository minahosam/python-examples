class person:
    def print(self):
        print(self.__class__.__name__)
class customer(person):
    pass
p=person()
c=customer()
p.print()
c.print()
