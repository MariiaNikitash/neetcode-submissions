class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # account fo prefixes 
        pref = 1
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]

        # account for suffixes and update res
        suf = 1
        for i in reversed(range(len(nums))):
            res[i] *= suf
            suf *= nums[i]

        return res