'''given a non-negative integer n,your task is to set the k-th bit of n(0-based indexing from the right).
setting a bit means turning it ON(i.e setting it to 1)
regardless of whether its already 0 or 1.
you must perform this operation using the bitwise left shift operator(<<).
input:an integer n,k
output:return the updated integer after the setting the k-th bit
ex:IP:n=10,k=1
   OP:10:'''
def setKthBit(n,i):
    return (n|(1<<i))
n=int(input())
i=int(input())
print(setKthBit(n,i))
'''n=10
i=1
step1:convert n to binary
n=10->00001010
step2:compute 1<<i
1<<1=00000010
step3:perform bitwise OR
00001010(n) | 00000010(1<<i)
00001010(result)'''
