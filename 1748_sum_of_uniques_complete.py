# 1748. Sum of Unique Elements
from functools import reduce
def sumOfUnique(nums):
    '''
    copy_nums = nums.copy()
    for item in nums:
        if nums.count(item) > 1: copy_nums.remove(item)
    return sum(copy_nums)
    '''
    #Optimised solution
    return sum([item for item in nums if nums.count(item) == 1])

print(sumOfUnique([1,1,1,1,1]))