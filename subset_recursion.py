def subset(nums):
    def recursion(index):
        if index==len(nums):
            return [[]]
        curr=recursion(index+1)
        res=[]
        for i in curr:
            res.append([nums[index]]+i)
        return curr+res
    return recursion(0)
nums=[1,2,3]
print(subset(nums)) 