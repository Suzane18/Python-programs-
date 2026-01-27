def check(i,n):
    if (n&(1<<i))!=0:
        return True
    return False
i=int(input())
n=int(input())
print(check(i,n))
