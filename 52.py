l1=open('l1.txt','w')
l1.write('mina')
l1.close()
l2=open('l2.txt','w+')
l2.write('koko')
l2.seek(0)
r2=l2.read()
print(r2)
l3=open('l1.txt')
r3=l3.read()
print(r3)
input('p e t e')
