'''Mininum Bit Flips to Convert One Integer to Another
You are given two non-negative integers start and goal .In one operation,you can flip a single bit in the binary representation of the integer start.
your task is to determine the min no.of bit flips reqd to convert start into goal 
inp: two integers
start and goal
op: a single integer representing the no.of diff bits btwn start and goal
ex:ip:10 and 7
op:3
Brut force approach : (manual bit conversion)
Bitwise iteration : n&(1<<i)
Optimal approach using n=n&(n-1)
'''
def min_bit_flips(start,goal):
    #optimal solution
    ans=start^goal
    res=bin(ans).count('1')
    return res
#using bitwise
def min(start,goal):
    ans=start^goal
    cnt=0
    for i in range(31):
        if ans&(1<<i):
            cnt+=1
    print(cnt)
#brute force approach
def min_bit(start,goal):
    ans=start^goal
    cnt=0
    while(ans!=0):
        rem=ans%2
        if rem==1:
            cnt+=1
        ans//=2
    return cnt
start=int(input())
goal=int(input())
print(min_bit_flips(start,goal))
min(start,goal)
print(min_bit(start,goal))
