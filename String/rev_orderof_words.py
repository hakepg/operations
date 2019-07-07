#Input = Python is very easy language
#output = language easy very is Python

s= 'Python is very easy language'
l=s.split() #always convert given string into list of words
print(l) #['Python', 'is', 'very', 'easy', 'language']
rev_words=l[::-1]
print(rev_words)# but here o/p in list form like= ['language', 'easy', 'very', 'is', 'Python']

outpt=' '.join(rev_words) #join can covert list to string
print(outpt)



