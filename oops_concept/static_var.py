
class student:
    a = 20
    def __init__(self):
        student.b=20

    def display(self):
        student.c=30

    @staticmethod
    def static():
        student.d=40

    @classmethod
    def classvar(cls):
        student.e=50

'''
s1=student() #print constructor level var
s1.display()# print instance method var
student.static() #print Static varible
student.classvar()#print class level var
student.f=60

print(student.__dict__)#here bydefault display class level vars i.e var a and f which is declared outside methods and constructor
'''

class sample:
    a=20
    def __init__(self):
        print('inside constructor') #access static var in constructor using self and clssname
        print(self.a)
        print(sample.a)

    def disply(self):  #in instance method access satic var using using self and clssname
        print('inside instance method')
        print(self.a)
        print(sample.a)

    @staticmethod
    def stamethod(): #in static method acces static var only using clssname
        print('inside static method')
        print(sample.a)

    @classmethod
    def clsmethod(cls):  # in clssmethod access static var using cls keyword and clssname
        print('inside clss method')
        print(cls.a)
        print(sample.a)


# s=sample()
# s.disply()
# s.stamethod()
# s.clsmethod()

#here we can access static variable everywhre

print('using constructor how to modify static variable..')
class stud:
    a=10

    def __init__(self): # here bcoz of constructor the new object get created
        self.b=20

s1=stud()
s2=stud()
s1.a=100
s1.b=200

print(s1.a,s1.b)
print(s2.a,s2.b) #using method su


print('using method how to modify static method without constructor..')
class stud:
    a=10
    def method(self):
        self.b=20


s1=stud()
s2=stud()
s1.a=100
s1.b=200

print(s1.a,s1.b)
print(s2.a,s2.b) #in method the object is not created so that it will give error...here b attibute is not there bcoz s2 cannot access mthod



