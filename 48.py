file=open('file.txt','w+')
names=['mi','ki','si','vi']
for s in names:
    c='hello'+s+'\n'
    file.writelines(c)
file.close()
