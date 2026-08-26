class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(': ')',
                '[': ']',
                '{': '}' }
        stack = []
        # itertw over each c
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if not stack or dic[stack[-1]] != c:
                    return False
                stack.pop()

        return len(stack) == 0
