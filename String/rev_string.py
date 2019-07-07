#using the slice operATOR
'''
n=input('enter any value')
print(n[::-1])
'''

#using reversed operator

n='pgh'
rev=reversed(n)
ch=''.join(rev)
print(ch)

#using len function
str=input('Enter some string')
output=''
i=len(str)-1
while i>=0:
    output=output+str[i]
    i=i-1
print(output)
