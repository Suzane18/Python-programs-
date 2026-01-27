def tsd_dp(distances):
    n=len(distances)
    VISITED_ALL=(1<<n)-1#all cities are visited
    #create a memorization table dp[mask][pos]
    dp=[[-1 for _ in range(n)]for _ in range(1<<n)]
    def visit(mask,pos):
        if mask==VISITED_ALL:
            return distance[pos][0]#return to starting city
        if dp[mask][pos]!=-1:
            return dp[mask][pos]
        min_cost=float('inf')
        for city in range(n):
            if (mask&(1<<city))==0:#if city  not visited
                new_cost=distances[pos][city]+visit((mask)(1<<city),city)
            if new_cost<min_cost:
                min_cost=new_cost
        dp[mask][pos]=min_cost
        return min_cost
    return visit(1,0)#start from city 0,only it is visited
distances=[[0,29,20,21],[29,0,15,17],[20,15,0,28],[21,17,28,0]]
#run the tsp solver
min_cost=tsd_dp(distances)
print("minimum cost:",min_cost)
    
