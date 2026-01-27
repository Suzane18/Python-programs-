def count_min_diff(arr,n,d):
    total=sum(arr)
    target=(d+sum(arr))//2
    MOD=10**9+7
    if (d+total)%2!=0 or total<d:
        return 0
    target=(d+total)//2
    dp=[0]*(target+1)
    dp[0]=1
    for num in arr:
        for j in range(target,num-1,-1):
            dp[j]=(dp[j]+dp[j-num])%MOD
    return dp[target]
arr=list(map(int,input().split()))
n=len(arr)
d=int(input())
print(count_min_diff(arr,n,d))
