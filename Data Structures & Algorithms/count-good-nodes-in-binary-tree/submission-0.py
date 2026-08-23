# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, MaxVal):
            if not node:
                return 0
            res = 1 if node.val >= MaxVal else 0
            MaxVal = max(MaxVal, node.val)
            res += dfs(node.left, MaxVal)
            res += dfs(node.right, MaxVal)
            return res
        return dfs(root, root.val)