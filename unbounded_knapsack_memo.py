def knapsack_memo(i,capacity,val,wt,memo):
    if i==len(val):
        return 0
    #consider current item only if
    #its weight is less than equal
    #to maximum weight
    if memo[i][capacity]!=-1:
        return memo[i][capacity]
    take=0
    if wt[i]<=capacity:
        take=val[i]+knapsack_memo(i,capacity-wt[i],val,wt,memo)
        #skip the curr item
    notake=knapsack_memo(i+1,capacity,val,wt,memo)
    memo[i][capacity]=max(take,notake)
    #return max of the two
    return memo[i][capacity]
def knapsack(capacity,val,wt):
    #2D matrix for memorization
    memo=[[-1 for _ in range(capacity+1)] for _ in range(len(val))]
    return knapsack_memo(0,capacity,val,wt,memo)

val=list(map(int,input().split()))#[1,1]
wt=list(map(int,input().split()))#[2,1]
capacity=int(input())#3
print(knapsack(capacity,val,wt))
