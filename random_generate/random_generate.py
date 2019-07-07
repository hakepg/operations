import random
import numpy

#
# random.seed()
#
# print(random.random()) #0.9560342718892494
# print(random.random())
# print(random.random())
# print(random.random())

# print('python program to print random integer'  )
#
# print(random.randint(0,10))
# print(random.randrange(1,20,3))


print('4 * 4 array in range of 10 to 50 ')


new_array=numpy.random.randint(10,50,size=(4,4))
print(new_array)

