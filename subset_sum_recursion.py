#Program to find the target sum in the subset if the array
def subset_sum(arr,n,target):
    if target==0:
        return True
    if n==0:
        return False
    if arr[n-1]>target:
        return subset_sum(arr,n-1,target)
        #exclude  function
    return subset_sum(arr,n-1,target) or subset_sum(arr,n-1,target-arr[n-1])
#include function--subset_sum(arr,n-1,target-1)where the target sum -array element is done
arr=list(map(int,input().split()))
target=int(input())
print(subset_sum(arr,len(arr),target))
