'''given a rod of length n inches and an array price[].price[i] denotes the value of a piece of length i.The task is to determine the max val obtainable by cutting up the rod and selling the pieces.
Note:price[] is 1 indexed array
ip:price[]=[1,5,8,9,10,17,17,20]
op:22
exp:the max obtainable value is 22 by cutting in two peices of lengths 2 and 6 , i.e.5+17=22
ip:price[]=[3,5,8,9,10,17,17,20]
op:24
exp:the max obtainable value is 24 by cutting in 8 peices of length1 ,i.e.8*price[1]=8*3=24'''
def cutRod_memo(i,price,memo):
    #Base case
    if i==0:
        return 0
        #if value is memoized
    if memo[i-1]!=-1:
        return memo[i-1]
    ans=0
    #find the max val for each cut take value of length j,and recursively find value of rod of length(i-j)
    for j in range(1,i+1):
        ans=max(ans,price[j-1]+cutRod_memo(i-j,price,memo))
    memo[i-1]=ans   
    return ans
def cutRod(price):
    n=len(price)
    memo=[-1]*n
    return cutRod_memo(n,price,memo)
price=[1,5,8,9,10,17,17,20]
print(cutRod(price))
