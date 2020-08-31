emp={'name':'mina',"salary":5000,'dept':'it'}
for x,y in emp.items():
    if x=="salary":
        y*=10
    print (x,y)
