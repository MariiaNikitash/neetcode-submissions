class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [] 
        n = len(nums)
    
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue # skip dublicate

            if nums[i] > 0: # if first val > 0 everything else will be larger and not gonna == 0
                break 
            l,r = i+1, n-1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum == 0:
                    res.append([nums[i],  nums[l], nums[r]])
                    l +=1
                    r -=1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1
                    while l < r and nums[r] == nums[r+1]:
                        r -=1
                elif curSum > 0:
                    r -=1
                else:
                    l +=1
        return res