def ToggleKthBit(n,i):
    return (n^(1<<i))
n=int(input())
i=int(input())
print(ToggleKthBit(n,i))
'''n=10
i=1
10->1010
1<<1->0010
1010^0010=0010'''
