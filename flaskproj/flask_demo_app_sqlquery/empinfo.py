class Employee:

    def __init__(self,eid,ename,eage,esal):
        self.empId = eid
        self.empName = ename
        self.empAge = eage
        self.empSal = esal

    def __str__(self):
        return f'\n {self.__dict__}'

    def __repr__(self):
        return str(self)

#
# e1=Employee(eid=1,ename='pgh1',eage=26,esal=566565)
# e2=Employee(eid=2,ename='pfgh',eage=25,esal=766565)
# e3=Employee(eid=3,ename='apgh',eage=23,esal=7866565)
# e4=Employee(eid=4,ename='ppgh',eage=24,esal=966565)

# print(e1,e2,e3,e4)