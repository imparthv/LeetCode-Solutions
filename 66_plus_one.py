# 66. Plus One
class Solution:
    def plusOne(self, digits):
        carry = 1
        i = len(digits) - 1
        while( i >= 0 and carry):
            digits[i] += carry
            if digits[i] >= 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0 

            i-=1
        if carry:
            digits.insert(0, carry)
        return digits
                 

testCase1 = Solution()

print(testCase1.plusOne([9, 9]))

        