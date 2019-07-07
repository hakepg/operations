class Student:

    def __init__(self,idd,nm):
        self.set_studid(idd)
        self.set_studnm(nm)


    def set_studid(self,idd):
        if idd>0:
            self._studid=idd
        else:
            print('invalid id',idd)


    def set_studnm(self,nm):
        if len(nm)>4 and len(nm)<=10:
            self._studnm=nm
        else:
            print('invalid name',nm)


    def get_studid(self):
        return self._studid


    def get_studnm(self):
        return self._studnm

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)

    StudentName=property(get_studnm,set_studnm)
    StudentId=property(get_studid,set_studid)

stu1=Student(idd=20,nm='Pratima')
stu1.set_studnm('pratima1')
stu1.set_studid(-89)
stu1.StudentId=-201
stu1.StudentId=-52
# stu1.StudentName='Atulhake'
stu1.StudentName='Atul'

print(stu1)


