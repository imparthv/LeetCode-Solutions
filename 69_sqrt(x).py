# 69. Sqrt(x)

import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(x ** 0.5)
    
testCase_1 = Solution()
inputVal = int(input("Enter a value:"))
outValue = testCase_1.mySqrt(inputVal)
print(outValue)