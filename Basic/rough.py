# class Student:
#
#     def __init__(self,id,nm,age,sal):
#         self.sid=id
#         self.stname=nm
#         self.stage=age
#         self.stusalary=sal
#
#     def __str__(self):
#         return f'{self.__dict__}'
#
#     def address(self,add1):
#         self.addr= add1
#
#
# s1=Student(id=1,nm='ppp',age=25,sal=5765876)
# s1.address(add1='pune')
# print(s1)

# print('print index wise..')
# string=input('enter some string')
# i=0
# for char in string:
#     print('the character present at {} index is'.format(i),char)
#     i=i+1

# print('display no in descending order')
# for i in range(10,0,-1):
#     print(i)

# print('print sum of num present inside list..')
# # list=eval('[10+20+30]')
# # print(list)
# list=eval(input('enter the list:'))
# sum=0
# for i in list:
#     sum=sum+i
# print(sum)

# brand=input('Enter Your Favourite Brand:')
# if brand=='RC':
#     print('It is children brand')
# elif brand=='JELOUS':
#     print('It is Girls brand')
# elif brand=='LC':
#     print('It is not much kick')
# else:
#     print('other brands not recommended..')

print('biggest of two no.from command prompt..')
a,b,c= [int(x)for x in input('enter the three num.:').split()]
print(a,b,c)
if a>b and a>c:
    print('the biggest no is -->',a)
elif b>c:
    print('the biggest no is -->',b)
elif a==c and a==b:
    print('cannot identify because it is similar')
else:
    print('the biggest no is -->',c)






