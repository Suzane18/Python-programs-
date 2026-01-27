def maxCommonSuf(s1,s2):
    m=len(s1)
    n=len(s2)
    #creste a table
    #common siffixes of substring
    lcsuf=[[0]*(n+1) for _ in range(m+1)]
    res=0
    #Build lcs[m+1][n+1} in bottom up fashion
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                lcsuf[i][j]=lcsuf[i-1][j-1]+1
                res=max(res,lcsuf[i][j])
            else:
                lcsuf[i][j]=0
    return res
s1=input()#abcdxyz
s2=input()#xyzabcd
print(maxCommonStr(s1,s2))#4
