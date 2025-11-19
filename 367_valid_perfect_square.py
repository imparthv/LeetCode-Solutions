import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt =  (num ** 0.5)
        return True if int(sqrt) == sqrt else False
    

test = Solution()
print(test.isPerfectSquare(15))