'''def reverse_list(lst):
    if len(lst) == 0:
        return []
    '''
def rec(lst,left,right):
    if left >= right:
        return
    lst[left], lst[right] = lst[right], lst[left]
    return rec(lst, left + 1, right - 1)
lst=[1, 2, 3, 4, 5]
rec(lst, 0, len(lst) - 1)
print(lst)  # Output: [5, 4, 3, 2, 1]