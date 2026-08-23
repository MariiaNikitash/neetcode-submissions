class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in dic:
                return [dic[comp], i]
            dic[n] = i