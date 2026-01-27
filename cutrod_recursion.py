def cutrod(i,price):
    if i==0:
        return 0
    ans=0
    '''find maximum value for each cut
    take value of rod of length j,and recursively
    find value of rod of length(i-j)'''
    for j in range (1,i+1):
        ans=max(ans,price[j-1]+cutrod((i-j),price))
    return ans
price=list(map(int,input().split()))
print(cutrod(len(price),price))
