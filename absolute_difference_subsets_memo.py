'''Given array arr[] of size n,the task is to divide it into two sets S1 and S2
such that absolute difference between their sums is minimum.
If there is set s with n elements, Subset2 must have n-m
elements and the value of abs(sum(subset1)-sum(subset2) should be min.
'''
#Memorization
def find_min_difference(arr,n,sum_cal,sum_total,memo):
    #base  case: if we have considered all elements
    if n==0:
        return abs((sum_total-sum_cal)-sum_cal)
    #check if result is alredy computed
    if memo[n][sum_cal]!=-1:
        return memo[n][sum_cal]
    #include the current element in the subset
    include=find_min_difference(arr,n-1,sum_cal+arr[n-1],sum_total,memo)
    #exclude the current element from the set
    exclude=find_min_difference(arr,n-1,sum_cal,sum_total,memo)
    #Store the result in memo and return
    memo[n][sum_cal]=min(include,exclude)
    return  memo[n][sum_cal]
def min_difference(arr):
    sum_total=sum(arr)
    memo=[[-1 for _ in range(sum_total+1)] for _ in range(len(arr)+1)]
    #intiated sum_cal as 0
    return find_min_difference(arr,len(arr),0,sum_total,memo)

#user input
arr=list(map(int,input().split()))
print(min_difference(arr))
    
