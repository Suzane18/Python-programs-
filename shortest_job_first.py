def solvesjf(bt):
    wt=et=0
    bt.sort()
    for i in range(len(bt)):
        wt+=et
        et+=bt[i]
    return wt//len(bt)

jobs=[5,7,2,3,1]
for job in jobs:
    print(job,end=" ")
print()
print(solvesjf(jobs))