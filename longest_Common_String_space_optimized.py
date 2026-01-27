'''space optimazation can often be applied to dp problems
by keeping track of only few prev instead of an entire table'''
#space optimized code
#iterative method
def longestcommonsubstr(s1,s2):
    m=len(s1)
    n=len(s2)
    #create a 1D array to store the previous row's result
    prev=[0]*(n+1)
    res=0
    for i in range(1,m+1):
        #create a temporary array to store the current row
        curr=[0]*(n+1)
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                curr[j]=prev[j-1]+1
                res=max(res,curr[j])
            else:
                curr[j]=0
            #move the current row's data to the previous row
        prev=curr
    return res
s1=input()
s2=input()
print(longestcommonsubstr(s1,s2))   
                
                    
    
