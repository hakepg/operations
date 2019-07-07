# print("how to open file in python")
''' 
always give \\ in path
just using open() function to open a file
'''
# f=open('C:\\Users\\Pratima Hake\\Desktop\\ppp.txt')

print('write the text into file')
with open('C:\\Users\\Pratima Hake\\Desktop\\ppp.txt','w') as file:
    file.write('Hi I am pratima hake..\n\n')
    file.write('I am python Developer..\n\n')
    file.write('Also Data scientist..\n\n')
    file.write('Ready to learn new things..\n\n')
with open('C:\\Users\\Pratima Hake\\Desktop\\ppp.txt', 'a') as file:
    file.write('ppppppppppppppppppppppppppppppppp\n\n')
    file.write('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n\n')

with open('C:\\Users\\Pratima Hake\\Desktop\\ppp.txt', 'r') as file:
    f=file.read(6)
    f1=file.read(12)
    print(f1)
    print(f)
    pos=file.tell() #(to tell position of the current word)
    print('current file position is {}'.format(pos),)
    f1=file.read()
    print(f1)
    for line in file: #(used to read file line by line)
        print(line,end=' ')
    f=file.readline()
    f1 = file.readline()
    print(f)
    print(f1)

with open('C:\\Users\\Pratima Hake\\Desktop\\ppp.txt','r+') as file:
    file.write('ppppppppppppppppppppppppppppppppp\n\n')
    file.write('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n\n')

# import os
# os.remove('C:\\Users\\Pratima Hake\\Desktop\\ppp.txt')






