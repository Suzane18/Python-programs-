class Solution:
    def findper(self,s):
        def gen(i,s,used,curr,st):
            if i==len(s):
               st.add("".join(curr))
               return
        seen=set()
        for j in range(len(s)):
            if not used[j] and s[j] not in seen:
                seen.add(s[j])
                used[j]=True
                curr.append(s[j])
                gen(i+1,s,used,curr,st)
                used[j]=False
                curr.pop()
     used=[False]*len(s)
     st=set()
     curr=[]
     s=sorted(s)
     gen(0,s,used,curr,st)
     return list(st)
