class emp:
    name = 'Atul'
    age = 45

    def __init__(self,id,name):
        self.empid = id
        self.empname=name

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)

    @classmethod
    def sample(cls):
        print(cls.age)
        print(cls.name)


# e1 = emp(id=1,name='pratima')
# print(emp.sample())

print('***************************************************del instance var**********************************************************')

class stud:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30

    def delete(self):
        del self

s1=stud()
print(s1.__dict__)
del s1.b,s1.a
print(s1.__dict__)
s1.delete()
print(s1.__dict__)
