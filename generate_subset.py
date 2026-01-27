def backtrack(start,path,nums,result):
    result.append(path[:])
    for i in range(start,len(nums)):
        path.append(nums[i])
        backtrack(i+1,path,nums,result)
        path.pop()
def subsets(nums):
    result=[]
    backtrack(0,[],nums,result)
    return result
nums=[1,2,3]
print(subsets(nums))
