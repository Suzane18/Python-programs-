class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1={}
        t1={}
        for i in range(len(s)):
            if s[i] not in s1:
                s1[s[i]]=i
            if t[i] not in t1:
                t1[t[i]]=i
            if s1[s[i]]!=t1[t[i]]:
                return False 
        return True           