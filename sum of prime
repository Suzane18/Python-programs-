
'''def sum_of(n):
    sum=0
    prime={'2','3','5','7'}
    for i in n:
        if i in prime:
            sum+=int(i)
    return sum
'''

def sum_of_prime(n):
    sum=0
    n=int(n)
    prime={2,3,5,7}
    if n==0:
        return n
    while n>0:
        temp=n%10
        if temp in prime:
            sum+=temp
        n//=10
    '''while n>0:
       temp=n%10
       if temp in prime:
           sum+=temp
        n//=10'''
    return sum
str=input()
print(sum_of_prime(str))
