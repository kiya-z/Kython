#coding:utf-8
# def log(f):
#     def wrapper(*argv,**kw):
#         print 'start'
#         a = f(*argv,**kw)
#         print 'end'
#         return a
#     return wrapper


class A(object):
    def __init__(self):
        self._name = 'a'

    #@log
    def getname(self):
        print(self._name)
        #return self._name

    #name = log(log(getname))

class B(A):

    def getname(self):
        print('child-get-name :')
        super().getname()

#a = A()
#print a.getname()
#a.name()
b = B()
b.getname()
