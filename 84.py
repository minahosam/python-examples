def fact(num):
    if num==0:
        r=1
    else:
        sum=1
        for i in range(1,num+1):
            sum=sum*i
        r=sum
    return r
print(fact(4))
