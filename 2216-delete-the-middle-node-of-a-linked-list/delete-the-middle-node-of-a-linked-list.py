# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow , fast = head , head
        if head.next is None:
            return None
        while fast is not None and fast.next is not None:
            prev_idx = slow
            fast = fast.next.next
            slow = slow.next
        
        # print(prev_idx)
        # if prev_idx.next is not None :
        prev_idx.next = slow.next
        return head
