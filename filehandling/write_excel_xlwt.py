import xlwt
#
path='E:\\python_my_practice\\filehandling\\addfile.xls'
# #
# import xlwt
# from xlwt import Workbook
#
# # Workbook is created
# wb = xlwt.Workbook(path)
#
#
# # add_sheet is used to create sheet.
# sheet = wb.active_sheet
#
# cell=wb.set_use_cell_values(1, 0, 'ISBT DEHRADUN')
# sheet.write(2, 0, 'SHASTRADHARA')

# wb.save('xlwt example.xls')
from xlwt import Workbook
exel_file=Workbook()
sheet=exel_file.add_sheet('empinfo')
style=xlwt.easyxf('font : bold 1, color red;')
row = 0
sheet.write(row,0,'empid',style)
sheet.write(row,1,'empnm',style)
sheet.write(row,2,'empage',style)
sheet.write(row,3,'empaddr',style)
sheet.write(row,4,'empsal',style)

exel_file.save(path)
print('write into excel file')


