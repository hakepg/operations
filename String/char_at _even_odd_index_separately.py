print('program to print characters present at even and odd index separatly')

# s = 'Durgasoft'
# # print(s[0])
# # print(s.split())
#
# for index, i in enumerate(s):
#     if index % 2 == 0:
#         print(i, 'in even position')


# s = 'Durgasoft'
# i = 0
# print('characters at even index')
# while i < len(s):
#     print(s[i])
#     i = i + 2
# print('characters at odd index')
# i=1
# while i < len(s):
#     print(s[i])
#     i = i + 2

print('program using slice operator')
s = 'durgasoft'
print('charcter at even indexes:', s[::2])

print('charactr at odd indexes:', s[1::2])