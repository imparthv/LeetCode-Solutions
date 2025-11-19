class Solution:
    def majorityElement(self, nums) -> int:
        val = len(nums)/2
        checkSet = set(nums)
        if len(checkSet) == 1: return nums[0]
        for x in checkSet:
            if nums.count(x) > val: return x
    
test = Solution()
print(test.majorityElement([1,1,1,2,2,2, 2, 2, 2, 3]))