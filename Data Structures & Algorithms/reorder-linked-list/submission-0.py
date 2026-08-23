# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the middle, then starting tht mode reverse list then to new list add one from first list one from reversed
        # [0, 1, 2, 3s,   4, 5, 6f]. 
       
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        slow.next = None
        # reverse second half
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        first = head   
        second = prev 
        while second:
            f_next, s_next = first.next, second.next
            first.next = second
            second.next = f_next
            first, second =  f_next, s_next

