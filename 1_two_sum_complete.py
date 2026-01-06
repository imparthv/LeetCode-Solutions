# 1. Two Sum
def twoSum(nums, target):
    ans_list = []
    for index_val in range(0,  len(nums)):
        target_val = target - nums[index_val]
        if target_val in nums[index_val+1:]:
            ans_list.append(index_val)
            ans_list.append(nums.index(target_val, index_val+1))
            break
    return ans_list

print(twoSum([3,4,5,6], 10))
