class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numSet = set(nums)
        max_count = 0
        for num in numSet:
            if num - 1 not in numSet:
                current_num = num
                count = 1
                while current_num + 1 in numSet:
                    current_num += 1
                    count += 1
                max_count = max(max_count, count)

        return max_count