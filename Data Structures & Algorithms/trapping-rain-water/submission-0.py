class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        res = 0
        n = len(height)
        maxLeft = len(height) * [0]
        maxRight = len(height) * [0]
        maxLeft[0] = height[0]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i-1], height[i])
    
        maxRight[n - 1] = height[n - 1]
        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])

        for i in range(n):
            res += min(maxRight[i], maxLeft[i]) - height[i]
        return res
        



