def n_meeting_in_one_room(start,end):
    n= len(start)
    m= []
    for i in range(n):
        m.append((end[i],start[i]))
    m.sort()
    free=-1
    ct=0
    for e,s in m:
        if s>free:
            ct+=1
            free=e
    return ct
start=[1,3,0,5,8,5]
end=[2,4,6,7,9,9]
print(n_meeting_in_one_room(start,end))