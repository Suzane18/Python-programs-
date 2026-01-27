def canPartition(nums):
    totalsum=sum(nums)
    if totalsum%2!=0:
        return False
    targetsum=totalsum//2
    dp=[False]*(targetsum+1)
    dp[0]=True
    for num in nums:
        for currsum in range(targetsum,num-1,-1):
            dp[currsum]=dp[currsum-num] + dp[currsum]
    return dp[targetsum]
nums=list(map(int,input().split()))
print(canPartition(nums))
