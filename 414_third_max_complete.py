# 414. Third Maximum Number
def thirdMax(nums):
    nums_list = sorted(list(set(nums)))
    print(nums_list)
    if len(nums_list) >=3 : return nums_list[len(nums_list)-3]
    else: return nums_list[-1]

print(thirdMax([-1,2,3]))