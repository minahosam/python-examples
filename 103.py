class test:
    video='aviable'
t1=test()
t1.video='a v'
print(getattr(t1,'video'))
