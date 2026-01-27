def lcs(x,y,m,n):
    if m==0 or n==0:
        return 0
    if x[m-1]==y[n-1]:
        return 1+lcs(x,y,m-1,n-1)
    else:
        return max(lcs(x,y,m,n-1),lcs(x,y,m-1,n))'''
def lcs(x,y):
    m=len(pattern)
    n=len(text)
    res=""
    for i in range(n-m+1):
        j=0
        while j<m and i+j<n and pattern[j]==text[i+j]:
            j+=1
        if j==m:
           res.append(i) 
lcs(pattern,text)'''

    
