def removelastBit(n):
    return (n&(n-1))
n=int(input())
#i=int(input())
print(removelastBit(n))
'''n=12
12->1100
11->1011
1100&1011=1000
1000->8'''
