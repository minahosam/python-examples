import os
files=os.listdir('New folder')
for file in files:
    zk=os.path.isdir('New folder\\'+file)
    print(zk)
    if os.path.isfile('New folder//'+file):
        print(file)
input('p e t e')
