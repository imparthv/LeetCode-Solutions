# 136. Single Number
def singleNumber(nums):
    '''
    for item in nums:
        if nums.count(item) == 1:
            return item
    '''
    '''
    return [item for item in nums if nums.count(item) == 1][0]
    '''
    temp_nums = nums.copy()
    nums = list(set(nums))
    for item in nums:
        count = temp_nums.count(item)
        if count == 1:
            return item
            break
    

input_list = [4, 1, 2, 1, 2]
output = singleNumber(input_list)
print(output)