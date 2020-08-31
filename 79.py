num1=int(input('e f n '))
num2=int(input('e s n '))
ope=str(input(' e o p'))
def calc(num1,num2,ope):
    r=0 
    if ope=='+':
        r=num1+num2
    elif ope=='-':
        r=num1-num2
    elif ope=='*':
        r=num1*num2
    else:
        if num2==0:
            num2 = 1
            r=num1/num2
    return r
r1=calc(num1,num2,ope)
d=r1*10
print(d)
