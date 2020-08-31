def wel(name):
    print('welcome'+name)
wel('mina')
n1=int(input('1'))
n2=int(input('2'))
def calc(n1,n2,ope):
    if ope=='+':
        print(n1+n2)
    elif ope=='-':
        print(n1-n2)
    elif ope=='*':
        print(n1*n2)
calc(n1,n2,'+')
