# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        first, sec = head , head.next
        while sec != None:
            if first.val == sec.val:
                first.next = sec.next
                sec = first.next
                # print(head)
            # first = first.next
            # sec = sec.next
            else: 
                first = first.next
                sec = sec.next
        return head
