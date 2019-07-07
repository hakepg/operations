from filehandling.data_operations_file.data_persist_operation import EmpOperation
from filehandling.data_operations_file.data_util import *
from filehandling.data_operations_file.data_persist_empinfo import *
class EmpOperImpl(EmpOperation):


    # def write_into_text(self,data):
    #     pass
    #
    # def read_from_text(self):
    #     pass

    def write_into_file(self,data):
        sheet,wb = get_excel_sheet()
        actualrow=0
        for index,emp in enumerate(data):

            sheet.cell(actualrow+2,1,emp.empId)
            sheet.cell(actualrow+2,2,emp.empName)
            sheet.cell(actualrow+2,3,emp.empAge)
            sheet.cell(actualrow+2,4,emp.empSalary)
            for index,address in enumerate(emp.empAddress):
                sheet.cell(actualrow+2,5,address.emppin)
                sheet.cell(actualrow+2,6,address.empcity)
                actualrow+=1
        wb.save(file_path+'pratima.xlsx')


    def read_from_file(self):
        sheet,wb= get_excel_sheet()
        emp=0
        listOfEmps=[]
        for row in range(2,sheet.max_row+2):
            # print('--------------------------------------------------------------------------------------------')
            if sheet.cell(row,1).value:
                emp = Employee(eid=sheet.cell(row,1).value,
                               enm=sheet.cell(row,2).value,
                               eage=sheet.cell(row,3).value,
                               esal=sheet.cell(row,4).value,
                               eaddr=Address(sheet.cell(row,5).value, sheet.cell(row,6).value))
                listOfEmps.append(emp)
            elif emp:
                addr=Address(sheet.cell(row,5).value,sheet.cell(row,6).value)
                listOfEmps.append(addr)

        print(listOfEmps)




ad1 = Address(pin=54515, city='Pune1')
ad2 = Address(pin=44325, city='Pune2')
ad3 = Address(pin=34235, city='Pune3')

e1 = Employee(eid=1, enm='pgh', eage=24, esal=545254, eaddr=[ad1, ad2, ad1])
e2 = Employee(eid=2, enm='pgh123', eage=26, esal=445254, eaddr=[ad3, ad2, ad2, ad3, ad1])
e3 = Employee(eid=3, enm='agh12', eage=28, esal=345254, eaddr=[ad1])
# e4 = Employee(eid=3, enm='sneha', eage=29, esal=245254, eaddr=['Sangli', 22478])

ab=EmpOperImpl()
# ab.write_into_file([e1,e2,e3])
ab.read_from_file()





    #

    # def write_into_db(self,data):
    #     pass
    #
    # def read_from_db(self):
    #     pass