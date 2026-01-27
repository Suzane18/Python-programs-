#unbounded knapsck using recursion
def knapsackrecur(i,capacity,val,wt):
    if i==len(val):
        return 0
    #consider current item only if
    #its weight is less than equal
    #to maximum weight
    take=0
    if wt[i]<=capacity:
        take=val[i]+knapsackrecur(i,capacity-wt[i],val,wt)
    notake=knapsackrecur(i+1,capacity,val,wt)
    return max(take,notake)
def knapsack(capacity,val,wt):
    return knapsackrecur(0,capacity,val,wt)

val=list(map(int,input().split()))#[1,1]
wt=list(map(int,input().split()))#[2,1]
capacity=int(input())#3
print(knapsack(capacity,val,wt))
