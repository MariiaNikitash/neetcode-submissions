# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        cur1 = head
        final = head
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next # 2nd half
        slow.next = None
        # reverse 2nd part
        prev = None
        curr = head2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        cur2 = prev 
        # combine parts 
        while cur1 and cur2:
            c1 = cur1.next
            c2 = cur2.next
            cur1.next, cur2.next = cur2, c1
            cur1, cur2 = c1, c2
    



