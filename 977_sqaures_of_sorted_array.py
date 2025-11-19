class Solution:
    def sortedSquares(self, nums):
        sortedList = sorted(list(map(lambda x: x**2, nums)))
        return sortedList


test = Solution()
print(test.sortedSquares([-4,-1,0,3,10]))
        
        