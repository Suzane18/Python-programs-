#recursive approach
def knapsack(wt,val,W,n):
    if n==0 or W==0:
        return 0
    if wt[n-1]>W:
        return knapsack(wt,val,W,n-1)
    else:
        return max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))


wt=list(map(int,input().split()))
val=list(map(int,input().split()))
W=int(input())
n=int(input())
print(knapsack(wt,val,W,n))
'''
knap(8,4)
|
|--wt[3]=5<=8->we can include or exclude
|
|--include item 4:value=4+knapsack(8-5=3,3)
|  |--knap(3,3)
|  |--wt[2]=6>3->skip->knap(3,2)
|  |--wt[1]=4>3->skip->knap(3,1)
|  |--wt[0]=3<=3->choose max(include,exclude)
|       |--include:2+knapsack(0,0)=2
|       |--exclude:knap(3,0)=0
|       |max=2
|   |--Total if we included the item 4=4+2=6
|
|--exclude item 4:knap(8,3)
|   |--wt[2]=6<=8->choosemax(include,exclude)
|   |--include:1+knap(2,2)
|   |  |--wt[1]=4>2->skip->knap(2,1)
|   |  |--wt[0]=3>2->skip->knap92,0)=0
|   |--include=1+0=1
|   |--exclude:knap(8,2)
|   |  |--wt[1]=4<=8->choose max(include,exclude)
|   |  |--includee:3+knap(4,1)
|   |  |--wt[0]=3<=3->choose max(include,exclude)
|   |  |   |--include:2+knap(1,0)=2
|   |  |   |--exclude:knap(4,0)=0
|   |  |   |--max=2
|   |  |--total=3+2=5
|   |  |--excludeknap(8,1)
|   |  |   |--wt[0]=3<=8->max(2+knap(5,0),knap(8,0))->2
|   |  |--max=5
|   |--max of include/exclude=max(1,5)=5
|--max if weexcludeitem 4=5
