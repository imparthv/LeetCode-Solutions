# 2465. Number of Distinct Averages
def distinctAverages(nums):
    distinct_avg_list = []
    sorted_nums = sorted(nums)
    while len(sorted_nums) != 0:
        distinct_avg_list.append((sorted_nums[0] + sorted_nums[-1])/2)
        sorted_nums.pop(0)
        sorted_nums.pop()
    return len(set(distinct_avg_list))

print(distinctAverages([1,100]))