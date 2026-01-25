def ratinmaze(maze):
    n=len(maze)
    res=[]
    path=[]
    def backtrack(r,c):
        
        if r==n-1 and c==n-1:
            res.append("".join(path))
            return 
        
        if r+1<n and maze[r+1][c]==1:
            path.append('D')
            backtrack(r+1,c)
            path.pop()
        maze[r][c]=0
        if c-1>=0 and maze[r][c-1]==1:
            path.append('L')
            backtrack(r,c-1)
            path.pop()
        if c+1<n and maze[r][c+1]==1:
            path.append('R')
            backtrack(r,c+1)
            path.pop()
        if r-1>=0 and maze[r-1][c]==1:
            path.append('U')
            backtrack(r-1,c)
            path.pop()
        maze[r][c]=1
    if maze[0][0]==1 and maze[n-1][n-1]==1:
        backtrack(0,0)
    return res
            
            # 110
            # 101