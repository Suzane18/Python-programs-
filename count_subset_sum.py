def subset_sum_tab(arr,n,target):
    dp=[[False for _ in range(target+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,target+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]] + dp[i-1][j]
                #include or exclude
            else:
                dp[i][j]=dp[i-1][j]
                #exclude
    return dp[n][target]
arr=[2,3,4,5,6]
target=10
print(subset_sum_tab(arr,len(arr),target))



