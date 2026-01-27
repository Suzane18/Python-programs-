def knapsack_tab(capacity,val,wt):
    #2D matrix for tabulation
    dp=[[0 for _ in range(capacity+1)] for _ in range(len(val)+1)]
    #calculate maximum profit for each item in index and knapsack weight
    for i in range(len(val)-1,-1,-1):
        for j in range(1,capacity+1):
            take=0
            if j-wt[i]>=0:
                take=val[i]+dp[i][j-wt[i]]
                notake=dp[i+1][j]
                dp[i][j]=max(take,notake)
    return dp[0][capacity]
val=list(map(int,input().split()))#[1,1]
wt=list(map(int,input().split()))#[2,1]
capacity=int(input())#3
print(knapsack_tab(capacity,val,wt))
