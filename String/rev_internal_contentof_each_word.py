str='python is very easy'

s=str.split()
s1=[]
print(s)
for item in s:
    s1.append(item[::-1])
print(s1)
outpt=' '.join(s1)
print(outpt)


