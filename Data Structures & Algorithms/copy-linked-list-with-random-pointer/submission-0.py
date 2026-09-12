"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # map original nodes to copied nodes
        cur = head
        mapp = {None:None}
        while cur:
            copy = Node(cur.val)
            mapp[cur] = copy
            cur = cur.next
        curr = head
        # 2nd pass to link copied nodes
        while curr:
            copy = mapp[curr]
            copy.next = mapp[curr.next]
            copy.random = mapp[curr.random]
            curr = curr.next
        return mapp[head]