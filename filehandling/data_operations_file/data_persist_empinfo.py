class Employee:

    def  __init__(self,eid,enm,eage,esal,eaddr):
        self.empId=eid
        self.empName=enm
        self.empAge=eage
        self.empSalary=esal
        self.empAddress=[]

        if type(eaddr)==Address:
            self.empAddress=[eaddr]# adress-[pin,city]
        elif type(eaddr)==list:
            self.empAddress.extend(eaddr)


    def __str__(self):
        return f' \n {self.__dict__}'

    def __repr__(self):
        return str(self)

class Address:

    def __init__(self,pin,city):
        self.emppin=pin
        self.empcity=city

    def __str__(self):
        return f'\n {self.__dict__}'

    def __repr__(self):
        return str(self)

# ad1=Address(pin=54515,city='Pune1')
# ad2=Address(pin=44325,city='Pune2')
# ad3=Address(pin=34235,city='Pune3')
#
# e1=Employee(eid=1,enm='pgh',eage=24,esal=545254,eaddr=[ad1,ad2,ad1])
# e2=Employee(eid=2,enm='pgh123',eage=26,esal=445254,eaddr=[ad3,ad2,ad2,ad3,ad1])
# e3=Employee(eid=3,enm='agh12',eage=28,esal=345254,eaddr=[ad1])
# e4=Employee(eid=3,enm='sneha',eage=29,esal=245254,eaddr=['Sangli',22478])
#
# print(e1)
# print(e2)
# print(e3)
# print(e4)
#
