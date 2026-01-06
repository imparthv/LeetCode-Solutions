# 167. Two Sum II - Input Array is Sorted
def twoSum(numbers, target):
    ans_list = []
    for index_val in range(0,  len(numbers)):
        target_val = target - numbers[index_val]
        if target_val in numbers[index_val+1:]:
            ans_list.append(index_val + 1)
            ans_list.append(numbers.index(target_val, index_val+1) + 1)
            break
    return ans_list

print(twoSum([3,4,5,6], 10))