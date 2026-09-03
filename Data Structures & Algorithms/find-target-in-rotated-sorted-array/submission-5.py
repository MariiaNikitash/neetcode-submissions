class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        # find smallest val
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        smallest = l
        # use bin search on correct part to find target
        #right side
        if nums[smallest] <= target <= nums[-1]:
            l,r = smallest, len(nums)-1
        else:
            l,r = 0, smallest-1

        while l<=r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

