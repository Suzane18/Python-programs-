def lcs_memo(x,y):
    m,n=len(x),len(y)
    #intialize
    memo=[[-1 for _ in range(n+1)]for _ in range(m+1)]
    def dp(i,j):
        if i==0 or j==0:
            return 0
        if memo[i][j]!=-1:
            return memo[i][j]
        if x[i-1]==y[j-1]:
            memo[i][j]=1+dp(i-1,j-1)
        else:
            memo[i][j]=max(dp(i-1,j),dp(i,j-1))
        return memo[i][j]
    return dp(m,n)
    
x=input()
y=input()
print(lcs_memo(x,y))
