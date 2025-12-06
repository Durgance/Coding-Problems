# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev , curr = dummy, dummy.next
        while curr!=None:
            if curr.val != val:
                curr = curr.next 
                prev = prev.next
            else:
                prev.next = curr.next
                curr = prev.next
        return dummy.next