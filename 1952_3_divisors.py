class Solution:
    def isThree(self, n: int) -> bool:
        countFactors = 0
        if n <= 1: return False
        for i in range(1, (n//2) + 1):
            if n % i == 0:
                countFactors+=1
        countFactors +=1
        return True if countFactors == 3 else False
    
test = Solution()
print(test.isThree(12))