def longestcommonsubstring(s1,s2):
    m=len(s1)
    n=len(s2)
    res=0
    for i in range(m):
        for j in range(n):
            curr=0
            while (i+curr)<m and (j+curr)<n and s1[i+curr]==s2[j+curr]:
                curr+=1
                res=max(res,curr)
    return res
s1=input()
s2=input()
print(longestcommonsubstring(s1,s2))  