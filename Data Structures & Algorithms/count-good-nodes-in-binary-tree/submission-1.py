# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(node, maxV):
            if not node:
                return 0
            res = 1 if node.val >= maxV else 0
            maxV = max(maxV, node.val)
            res += helper(node.left, maxV)
            res += helper(node.right, maxV)
            return res
        
        return helper(root, root.val)
        
                
            
            
