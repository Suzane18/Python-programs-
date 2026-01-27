'''Given a non-negative integern, write a program to count the
number of bits that are set to 1 in its binary representation.
You must implement this using bitwise operations.
input: Asinglr integer n (0<=n<=10**9)
Output: An integer denoting the number of set bits in n.
Exam[le:
input: 13
output: 3
'''
'''def count_set_bits(n):
    n=bin(n)
    count=0
    st=str(n)
    st=st[2:]
    while (st):
        if st=='1':
            count+=1
    print(count)'''
def count_set_bits(n):
    # brute force
    cnt = 0
    while n > 0:
        rem = n % 2
        if rem == 1:
            cnt += 1
        n = n // 2  # Fixed from n // 1
    return cnt

def count_set_using_bits_bits(n):
    cnt = 0
    while n > 0:
        cnt += (n & 1)  # Directly use bitwise AND
        n = n >> 1
    return cnt

n=int(input())
print(count_set_bits(n))
print(count_set_using_bits_bits(n))
