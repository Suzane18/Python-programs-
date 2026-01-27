'''Given array arr[] of size n,the task is to divide it into two sets S1 and S2
such that absolute difference between their sums is minimum.
If there is set s with n elements, Subset2 must have n-m
elements and the value of abs(sum(subset1)-sum(subset2) should be min.
'''
#Tabulation
def min_difference(arr):
    sum_total=sum(arr)
    n=len(arr)
    #Create a DP table where dp[i[j] represents if a subset
    #sum 'j' is achievable using the first i elements
    dp=[[False for _ in range(sum_total+1)] for _ in range(len(arr)+1)]
    #a sum of 0 is always achievable (empty set)
    dp[0][0]=True
    #fill the dp table
    for i in range(1,n+1):
        for sum_val in range(0,sum_total+1):
            #Exclude the current element
            dp[i][sum_val]=dp[i-1][sum_val]
            #include the current element
            if sum_val>=arr[i-1]:
                dp[i][sum_val]=dp[i][sum_val]\
                                or dp[i-1][sum_val-arr[i-1]]
    #find the min difference
    min_diff=float('inf')
    #iterate over all possible subset sums and
    #find the min difference
    for sum_val in range(0,sum_total//2+1):
        if dp[n][sum_val]:
            min_diff=min(min_diff,\
                         abs((sum_total-sum_val)-sum_val))
    return min_diff       
    #intiated sum_cal as 0
#user input
arr=list(map(int,input().split()))
print(min_difference(arr))
    
