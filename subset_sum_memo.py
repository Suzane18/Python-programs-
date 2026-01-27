def subset_sum_memo(arr,n,target,dp):
    if target==0:
        return True 
    if n==0 :
        return False  
    if dp[n][target]!=-1:
        return dp[n][target]
    if arr[n-1]<=target:
        include=subset_sum_memo(arr,n-1,target-arr[n-1],dp)
        exclude=subset_sum_memo(arr,n-1,target,dp)
        dp[n][target]=include or exclude
    else:
        dp[n][target]=subset_sum_memo(arr,n-1,target,dp)
    return dp[n][target]
arr=list(map(int,input().split()))
target=int(input())
n=len(arr)
dp=[[-1 for _ in range(target+1)] for _ in range(n+1)]
print(subset_sum_memo(arr,len(arr),target,dp))
#boolean values are used so we dont use max functions
