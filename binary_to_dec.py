def binary_decimal(n):
    deci=0
    base=1
    while(n>0):
        temp=n%10
        n//=10
        if temp==1:
            deci+=temp*(base)
        base*=2
    return deci
def binary_to_decimal(n):
    p2=1
    res=0
    for i in range(len(n)-1,-1,-1):
        if n[i]=='1':
            res+=p2
        p2*=2
    return res
#n=input()
str=int(input())
print(binary_decimal(str))
#print(binary_to_decimal(n))
print(2**0)
