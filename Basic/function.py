# group of lines of code#reusability of code#if a group of stmnt is repeatedly req.then
# it is not recommended to write these stmnt everytime seperately, we have to define these stmnt as a
# single unit and we can call thet unit any no of times based on our req without rewriting. this unit is
# nothing but functions.

'''
def show():
    print('my name is Pratima')

def show(x):
    print('my name is :', x)

def show():
    print('my name is Pratima')

show() # here function overloading is not possible
# show(12) # suupose give agrgument as show in 2nd funct but it will not accept for 2nd func bcz
# it always perform operation on last function..n there is no argument
# show()
'''
'''
def sqrefun(num):
    print('the squareroot of {} is :'.format(num),(num*num))
sqrefun(25)
'''


print('***************************************************RETURN STATEMENT***********************************************************')

# funct can take input values as a parameter and execute business logic ,
# and returns o/p to the caller with retun stmnt

# def sum(x,y):
#     return x*y # here retun the busines logic if not give business logic then by default it will print None

# result = sum(10,20)
# print('the sum is :', result)

# def f1():
    # print('hello')
# f1()

def f1():
    return #if return value not there then it will give none
f1()
# print(f1())

# num = int(input('enter the no'))
# def even_odd(num):
#     if num%2==0:
#         print('num is even')
#     else:
#         print('num is odd')
# even_odd(num)

# def fact(num):
#     res=1
#     while num>=1:
#         res = res*num
#         num = num-1
#     return res
# print('the fact of 5 is',fact(5))
# for i in range(1,5):
#     print('the fact of {} is'.format(i),fact(i))


print('************************************Returning multiple values from a function******************************************')

def sum(a,b):
    sum = a+b
    sub = a-b
    return sum,sub
result = sum(2,5)
for i in result:
    print(i)
# print('the sum is',x)
# print('the sub is',y)

def calc(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return sum,sub,mul,div
t = calc(10,6)
print(t)
# for i in t:
#     print(i)

# types of argument
# 1.positional
# 2.keyword
# 3.default
# 4.variable length

# def wish(name,msg):
#     print('hello', name, msg)
# wish(name='good', msg='morning')
# wish('good', 'morning')
# wish('good', msg= 'morning')
# wish(name= 'good','morning')

# def f1(*n):
#     total = 0
#     for n1 in n:
#         total = total+n1
#     print('the sum = ',total)
#
# f1()
# f1(10)
# f1(10,12,25)
#
# def f1(n1,*s):
#     print(n1)
#     for s1 in s:
#         print(s1)
# f1(10)
# f1(10,12,20,24)
# f1(10,'a',30,'b')















