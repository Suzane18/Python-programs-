'''s=input()
pattern=input()
print(s.find(pattern))'''
#iterative method
text=input()
pattern=input()
def compare(pattern,text):
    m=len(pattern)
    n=len(text)
    for i in range(n-m+1):
        j=0
        while j<m and i+j<n and pattern[j]==text[i+j]:
            j+=1
        if j==m:
            print(i)
compare(pattern,text)
