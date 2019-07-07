class Student:

    '''This is all about the oops concept includes class, object and reference variable'''

    def __init__(self, rollno, age, address, contno):

        self.StudRoll = rollno
        self.StudAge = age
        self.StudAddress = address
        self.StudContact = contno

    def method(self):
        print('roll no :', self.StudRoll)
        print('student age :', self.StudAge)
        print('student addr :', self.StudAddress)
        print('student contact no :', self.StudContact)


    def __str__(self):
        return f'\n {self.__dict__}'

    def __repr(self):
        return str(self)

s1 = Student(rollno=101, age='20', address='pune1', contno=7887465625)
s2 = Student(rollno=102, age='21', address='pune2', contno=8887465625)
s3 = Student(rollno=103, age='23', address='pune3', contno=9887465625)
print(s1)



s1.method()
# s1.method()
# s1.method()
print(Student.__doc__)
