def clearKthBit(n,i):
    return (n&~(1<<i))
n=int(input())
i=int(input())
print(clearKthBit(n,i))
'''n=14
i=2
14->1110
1<<2=0100
~(1<<2)=1011
1110&1011=1010->10'''
