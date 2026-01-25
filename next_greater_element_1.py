def next_greater_element_1(nums1, nums2):
    """
    Finds the next greater element for each element in nums1 based on their positions in nums2.

    Parameters:
    nums1 (List[int]): A list of integers for which to find the next greater elements.
    nums2 (List[int]): A list of integers where the next greater elements are searched.

    Returns:
    List[int]: A list of integers representing the next greater elements for each element in nums1.
               If no greater element exists, -1 is returned for that position.
    """
    next_greater = {}
    stack = []

    # Traverse nums2 in reverse to find the next greater elements
    for num in reversed(nums2):
        while stack and stack[-1] <= num:
            stack.pop()
        next_greater[num] = stack[-1] if stack else -1
        stack.append(num)

    # Build the result for nums1 based on the next greater mapping
    result = [next_greater[num] for num in nums1]
    
    return result
# example input
print(next_greater_element_1([4,1,2], [1,3,4,2]))
def next_greater_element_2(nums1, nums2):
    """
    Finds the next greater element for each element in nums1 based on their positions in nums2.

    Parameters:
    nums1 (List[int]): A list of integers for which to find the next greater elements.
    nums2 (List[int]): A list of integers where the next greater elements are searched.

    Returns:
    List[int]: A list of integers representing the next greater elements for each element in nums1.
               If no greater element exists, -1 is returned for that position.
    """
    next_greater = {}
    stack = []

    # Traverse nums2 in reverse to find the next greater elements
    for num in reversed(nums2):
        while stack and stack[-1] <= num:
            stack.pop()
        next_greater[num] = stack[-1] if stack else -1
        stack.append(num)

    # Build the result for nums1 based on the next greater mapping
    result = [next_greater[num] for num in nums1]
    
    return result
def next_greater_element(nums1,nums2):
    st=[]
    nge={}
    for num in reversed(nums2):
        while st and st[-1]<=num:
            st.pop()
        if st:
            nge[num]=st[-1]
        else:
            nge[num]=-1 
        st.append(num)
    res=[]
    for n in nums1:
        res.append(nge[n])
    return res
# example input
print(next_greater_element([2,4], [1,2,3,4]))
print(2%3)