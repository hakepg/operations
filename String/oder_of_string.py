# s1 = 'a5f8d2g5f1'
# # s1 = input('enter some string')
# opt=''
#
# for ch in s1:
#     if ch.isalpha():
#         x=ch
#     else:
#         a=int(ch)
#         opt=opt+x*a
# print(opt)


# s ='a3b2a3c2b2z3'
# output = 'aaabbcczzz'
# opt = ''
#
# for ch in s:
#     if ch.isalpha():
#         char = ch
#     else:
#         digit = int(ch)
#         opt = opt + char*digit
# newop = ' '.join(sorted(opt))
# print(newop)


s1 = 'aabbbcc'
opt = '2a3b2c'
count= 0
list = s1.split()

for ch in s1:
    print(ch)
    if count<len(s1):
        print(s1[count])


# print(s1.count('a'))
