class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        if not height:
            return 0

        n = len(height)-1
        l,r = 0, len(height)-1
        res = 0
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r-=1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res
        



