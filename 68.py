import re
l1=input ('ms')
l2='^[A-Z][a-z]+\s[A-Z][a-z]*$'
v=re.match(l2,l1)
print(v.group())
input('p e t e')
