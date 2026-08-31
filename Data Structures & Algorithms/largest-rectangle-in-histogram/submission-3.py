class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxH = 0
        # iterate to get monotoic increasing stack + compute area
        for i, h in enumerate(heights):
            start = i # how far left it csn stretch
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxH = max(maxH, (height * (i - index)))
                start = index
            stack.append((start, h))


        # loop through bars still in stack to compute area
        for i, h in stack:
            maxH = max(maxH, h * (len(heights) - i))
        return maxH