def count_vowels(str):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    cnt=0
    for i in str:
        if i in vowels:
            cnt+=1
    return cnt
s=input()
print(count_vowels(s))
def count_vowel_substring(str):
    vowels='aeiou'
    count = 0
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            substring = str[i:j]
            if all(char in vowels for char in substring):
                count += 1
    return count
s = input()

print(count_vowel_substring(s))
def count_vowel_substring_optimized(s):
    vowels = set('aeiou')
    count = 0
    current_length = 0
    
    for char in s:
        if char in vowels:
            current_length += 1
            count += current_length
        else:
            current_length = 0
            
    return count