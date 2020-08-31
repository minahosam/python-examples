class test:
    def __init__(self):
        print(' object was created')
    def __del__(self):
        print('object was deleted')
t1=test()
del t1
