class person:
    def print(self):
        print('55')
class customer(person):
    def print(self):
        print('66')
p=person()
c=customer()
p.print()
c.print()
