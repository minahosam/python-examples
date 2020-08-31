import os
if os.path.exists('file1.txt'):
    print('yes')
    os.remove('file1.txt')
else:
    print('no')
    open('file1.txt','w')
os.rmdir('m')
os.removedirs('New folder','s')
input('p e t e')
