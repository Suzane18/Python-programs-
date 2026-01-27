#using recursion
def Lcs(s1,s2,m,n):
    if m==0 or n==0 or s1[m-1]!=s2[n-1]:
        return 0
    return 1+Lcs(s1,s2,m-1,n-1)
def maxstr(s1,s2):
    res=0
    m=len(s1)
    n=len(s2)
    for i in range(1,m+1):
        for j in range(1,n+1):
            res=max(res,Lcs(s1,s2,i,j))
    return res
s1=input()
s2=input()
m=len(s1)
n=len(s2)
print(maxstr(s1,s2))
