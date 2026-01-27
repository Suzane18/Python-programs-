'''Given array arr[] of size n,the task is to divide it into two sets S1 and S2
such that absolute difference between their sums is minimum.
If there is set s with n elements, Subset2 must have n-m
elements and the value of abs(sum(subset1)-sum(subset2) should be min.
'''
#recursive approach
def find_min_difference(arr,n,sum_cal,sum_total):
    if n==0:
        return abs((sum_total-sum_cal)-sum_cal)
    include=find_min_difference(arr,n-1,sum_cal+arr[n-1],sum_total)
    exclude=find_min_difference(arr,n-1,sum_cal,sum_total)
    return  min(include,exclude)
def min_difference(arr):
    sum_total=0
    for num in arr:
        sum_total+=num
    return find_min_difference(arr,len(arr),0,sum_total)
arr=list(map(int,input().split()))
print(min_difference(arr))
    
