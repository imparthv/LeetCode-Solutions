class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_dict = {}
        for num in nums:
            if num not in freq_dict: freq_dict.update({num: nums.count(num)})
        freq_list = sorted(freq_dict.items(), key = lambda item: item[1], reverse=True)
        result_list = [num[0] for num in freq_list]
        return result_list[:k]
        
    
test_case = Solution()
print(test_case.topKFrequent([1], 2))