class Solution:
    def removeDuplicates(self, nums) -> int:
        checkList = nums[:]
        for i in checkList:
            if checkList.count(i) > 1 and nums.count(i) > 1:
                nums.remove(i)
       
        return len(nums)
    
test = Solution()
print(test.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


        