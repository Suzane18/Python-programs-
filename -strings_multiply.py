'''def multiply_string(s):
    res=''
    i=0
    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            if i < len(s): 
                res += s[i ]*num
        else:
            res += s[i]
        i += 1
    return res
s="4a3bc"
print(multiply_string(s))
num1="123"
num2="456"
def multiply_strings(num1, num2):
    if num1=="0" or num2=="0":
        return "0"
    def st(num):
        res = 0
        for i in range(len(num)):
            res = res * 10 + ord(num[i]) - ord('0')
        return res
    def ts(s):
        res=''
        while s:
            a=s%10
            s=s//10
            res=chr(a+ord('0'))+res
        return res
    return ts(st(num1) * st(num2))'''
'''def multiply(num1, num2):
        res = 0
        for i in range(len(num2)):
            res += st(num1) * (ord(num2[i]) - ord('0')) * (10 ** (len(num2) - i - 1))
        return res
    result = multiply(num1, num2)
    res_str = ""
    while result > 0:
        res_str = chr(result % 10 + ord('0')) + res_str 
        result //= 10
    return res_str if res_str else "0"'''
#print(multiply_strings(num1, num2))
def isisomorphic(s1,s2):
    if len(s1)!= len(s2):
        return False
    s1={}
    s2={}
    for i in range(len(s1)):
        if s1[i] not in s1:
            s1[s[i]]=i
        if s2[i] not in s2:
            s2[t[i]]=i
        if s1[i]!=s2[i]:
            return False
    return True
s1 = "egg"
s2 = "add"  
print(isisomorphic(s1, s2))  # This will print True if the strings are isomorphic, otherwise False.
def reverse_words_in_string(s):
    words=s.split()
    left=0
    right=len(words)-1
    while left<right:
        words[left],words[right]=words[right],words[left]
        left+=1
        right-=1
    return ' '.join(words)
s = "Hello World"       
print(reverse_words_in_string(s))  # Output: "World Hello"