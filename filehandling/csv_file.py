import csv

# with open('C:\\Users\\Pratima Hake\\Desktop\\book1.csv','r') as csv_file:
# f = csv_file.readlines()

# reader = csv.reader(csv_file)
# for row in reader:
#     print(row)
# csv.register_dialect('myDialect',delimiter = ',',skipinitialspace=True)
# with open('C:\\Users\\Pratima Hake\\Desktop\\book1.csv','r') as c_file:
#     reader=csv.reader(c_file,dialect='myDialect')
#     for value in reader:
#         print(value[0])
#
# csv.register_dialect('myDialect',delimiter = ',',quoting=csv.QUOTE_ALL,skipinitialspace=True)
# with open('C:\\Users\\Pratima Hake\\Desktop\\book1.csv','r') as c_file:
#     reader=csv.reader(c_file,dialect='myDialect')
#     for value in reader:
#         print(value[0])

csv.register_dialect('myDialect', delimiter = '|')
with open('C:\\Users\\Pratima Hake\\Desktop\\book1.csv', 'r') as file:
    reader = csv.reader(file, dialect='myDiaect')
    for item in reader:
        print(item)
