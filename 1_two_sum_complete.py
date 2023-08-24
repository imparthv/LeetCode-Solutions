# 1. Two Sum
def twoSum(nums, target):
    ans_list = []
    for val1 in range(0, len(nums)):
        for val2 in range(1, len(nums)):
            if val1 != val2 and nums[val1] + nums[val2] == target:
                ans_list.append(val1)
                ans_list.append(val2)
                return ans_list
input_list =[3, 3]
print("Enter target:")
target_num = int(input())
output_list = twoSum(input_list, target_num)
print(output_list)