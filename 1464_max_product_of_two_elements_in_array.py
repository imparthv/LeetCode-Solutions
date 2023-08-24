# 1464. Maximum product of two elements in array
def maxProduct(nums):
    nums = sorted(nums)
    return (nums[-1] - 1) * (nums[-2] - 1)


print(maxProduct([3,4,5,2]))