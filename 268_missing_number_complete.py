# 268. Missing Number
def missingNumber(nums):
    for i in range(0, len(nums) + 1):
        if i not in nums: return i

print(missingNumber([9,6,4,2,3,5,7,0,1]))