#cutrod using tabulation
def cutrod(price):
    n=len(price)
    memo=[0]*n+1
    #find maximum value for all
    #rod of length i
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i]=max(dp[i],price[j-1]+dp[i-j])            
    return dp[n]
price=list(map(int,input().split()))
print(cutrod(price))
