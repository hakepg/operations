#pattern 55
n=5
for row in range(n,0,-1):
    print(' '*(n-row),end=' ')
    for column in range(1,n+1):
        print('*', end=' ')
    print()

