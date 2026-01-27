def knapsack_dp_tab(wt,val,W,n):
    dp=[[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,W+1):
            if wt[i-1]<=w:
                dp[i][w]=max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][W]
wt=list(map(int,input().split()))#wt=3 4 6 5
val=list(map(int,input().split()))#2 3 1 4
W=int(input())#8
n=int(input())#len(weights)
print(knapsack_dp_tab(wt,val,W,n))
#i-1,wt[i]+profit of previous item value+profit of i




