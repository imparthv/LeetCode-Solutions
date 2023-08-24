# 2441. Largest Positive Integer That Exists With Its Negative
def findMaxK(nums):
    min = 0
    for num in nums:
        if num < min and abs(num) in nums:
            min = num
    if abs(min) in nums: return abs(min)
    else: return -1

print(findMaxK([-10,8,6,7,-2,-3]))