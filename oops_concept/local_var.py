# class student:
#     def m1(self):
#         a=10 # local variable inside method
#         print(a)
#
#     def m2(self):
#         a=10
#         b=20
#         print(a)
#         print(b)
#
# s1 = student()
# s1.m1()
# s1.m2()

class student:
    def average(self,list):
        result=sum(list)/len(list)
        print(result)

# s1 = student()
# s1.average([10,20,10,25,35])


x=5 #if we not declraed gobal as x then it can use this value o/p will be 5

class example:
    def m1(self):
        global x # if we declred global in clss then it can access that clas var instead of outside clss var.o/p is 10
        x=10
        print(x)

    def m2(self):
        global x
        x=12
        print(x)


e1 = example() #create the object of that class after clssmane '()' necessary
e1.m1() #method calling
e1.m2()
print(x)






