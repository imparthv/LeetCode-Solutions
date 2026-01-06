class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        mid_index = len(nums1) // 2 
        if len(nums1) % 2 == 0:
            return (nums1[mid_index - 1] + nums1[mid_index]) / 2
        else: return nums1[mid_index ]

test_case = Solution()
print(test_case.findMedianSortedArrays([1,2,3,4,5], [6,7,8,9,10,11,12,13,14,15,16,17]))