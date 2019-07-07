from Basic.Exception_handling import m1

m1()

a = 'durga\nsoftware' #new line
b = 'durga\tSoftware' #tab
c = 'durga\rSoftware\rpratima' #carraige means last here if take pratima the it will print only this otherwise print software
d = 'durgaa\bSoftware' #it will used as backspace, remove one last character
e = 'Durga\fSoftware' #form feed..give the arraow in upward direction
f = 'durga\vSoftware' # vertical tab..give space in box
g = 'durga\'Software' # print the singleqoute
h = 'durga\"Software' #print the doublequote
i = 'durga\\Software' #print one slash
print(i)

a='string'
b='string'
print(id(a))
print(id(b))
print('a>b is {}'.format(a>b))
print('a<b is {}'.format(a<b))
print('a=b is {}'.format(a==b))
print('a>=b is {}'.format(a>=b))
print('a<=b is {}'.format(a<=b))

print(True>True)
print(True<True)
print(True>False)
print(10>True)

# print(math.ceil(15))