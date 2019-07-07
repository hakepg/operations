# Sorting give class details

class Emp :

    def __init__(self,id,nm,age,sal,addr):
        self.empId=id
        self.empName=nm
        self.empAge=age
        self.empSalary=sal
        self.empAddress=addr


    def __str__(self):
        return '\n Id {} Name {} Age {} Salary {} Address {}'.format(self.empId)

    def __repr__(self):
        return str

