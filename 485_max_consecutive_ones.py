# 485. Max Consecutive Ones
def findMaxConsecutiveOnes(nums):
    nums.append(0)
    count_one_list = []
    temp_count = 0
    for item in nums:
        if item == 1:
            temp_count += 1
        else: 
            count_one_list.append(temp_count)
            temp_count = 0
    return max(count_one_list)

print(findMaxConsecutiveOnes([1,0,1,1,0,1]))