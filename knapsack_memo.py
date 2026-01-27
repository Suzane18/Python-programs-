def knapsack_memo(wt,val,W,n,dp):
    
    if n==0 or W==0:
        return 0
    if dp[n][W]!=-1:
        return dp[n][W]
    if wt[n-1]<=W:
        include=val[n-1]+knapsack_memo(wt,val,W-wt[n-1],n-1,dp)
        exclude=knapsack_memo(wt,val,W,n-1,dp)
        dp[n][W]=max(include,exclude)
    else:
        dp[n][W]=knapsack_memo(wt,val,W,n-1,dp)
    return dp[n][W]
wt=list(map(int,input().split()))#wt=3 4 6 5
val=list(map(int,input().split()))#2 3 1 4
W=int(input())#8
n=int(input())#len(weights)
dp=[[-1 for _ in range(W+1)] for _ in range(n+1)]
print(knapsack_memo(wt,val,W,n,dp))
