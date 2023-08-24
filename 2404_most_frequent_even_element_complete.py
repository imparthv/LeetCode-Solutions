# 2404. Most Frequent Even Element
'''
'''
def mostFrequentEven(nums):
    min_val = -1
    max_count = 0
    for item in nums:
        if item % 2 == 0 and max_count < nums.count(item):
            max_count = nums.count(item)
            min_val = item
        elif item % 2== 0 and max_count == nums.count(item) and item < min_val:
            max_count = nums.count(item)
            min_val = item
    if min_val > -1: return min_val
    else: return -1

print(mostFrequentEven([0,0,0,0]))