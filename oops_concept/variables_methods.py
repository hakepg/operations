class Employee:
    cname = 'walchand' #Static variable or class level variable declared at class level outside method and constructor
    def __init__(self, id, name, age, salary): # this is constructor call at object created level

        self.empid = id # self.anyname is a instance variable
        self.empname = name
        self.empage = age
        self.empsal = salary

    def display(self):
        # age = 40
        print('employe name :', self.empname)
        # print('employee age: ', age)
        print('employee age: ', self.empage)
        print('emp salary:', self.empsal)

    @classmethod         # class method can access the class variable here for class method methodname with cls keyword and decorator @classmethod
    def getCollegeName(cls):   #class method methodname with cls keyword
        print('college name:', cls.cname) #access the class variable

    @staticmethod  #if we are not used this decorator then it should be work with the classname.methodname only not with the referenec bcz bydefault classname consider its a static. in instace method we can give self keyword with always reference variable
    def show(x,y):
        print('addition is :', (x+y))

E1 = Employee(id=1, name='pgh', age=25, salary=45795)
E2 = Employee(id=2, name='gfjhgh', age=27, salary=4585795)

# print(E1)
# print(Employee.display(E1))
# Employee.getCollegeName()
Employee.show(2,3)
