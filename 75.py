import csv
m=open('moo.csv')
for index in range(3):
    r=csv.reader(m)
    c=next(r)
    print(index)
    print('coloum')
    
    print(c)
print(m)
