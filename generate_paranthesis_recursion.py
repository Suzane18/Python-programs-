def generate_paranthesis(n):
    result=[]
    def rec(curr,count1,count2):
        if len(curr)==2*n:
            result.append(curr)
            return
        if count1<n:
            rec(curr+"(",count1+1,count2)
        if count2<count1:   
            rec(curr+")",count1,count2+1)
    rec("",0,0)
    return result   
n=3
print(generate_paranthesis(n))