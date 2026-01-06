class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        pointer_1 = 0
        pointer_2 = len(numbers) - 1
        while pointer_1 < pointer_2:
            value = numbers[pointer_1] + numbers[pointer_2]
            if value == target:
                return [pointer_1+1, pointer_2+1]
            elif value > target:
                pointer_2 -= 1
            else:
                pointer_1 +=1
        return [-1, -1]
    
test_case = Solution()
print(test_case.twoSum([2,3,4], 7))