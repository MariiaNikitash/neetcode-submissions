class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = nums[0]
        for num in nums[1:]:
            if num < smallest:
                smallest = num
        return smallest