# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#had this q in bloomberg 
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # pre order tr using dfs 
        res = []
        def dfs(node):
            if not node:
                res.append("null")
                return
            #DONT FORGET TO turn to str bruh
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        str_nodes = data.split(",")
        idx = 0

        # pre order dfs use idx to track, create nodes if not "null"
        def dfs():
            nonlocal idx
            if str_nodes[idx] == "null":
                idx += 1
                return None
            node = TreeNode(int(str_nodes[idx]))
            idx +=1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

# Time for both is N and space N 

