# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101,head)
        first , sec = dummy , dummy.next
        # c = 1
        prev = None
        while sec!=None:
            if first.val != sec.val:
                if first.next!=sec:
                    prev.next = sec
                    first = sec
                else:
                    prev = first
                    first = first.next
                # first = first.next
                sec = sec.next
            else:
                sec = sec.next
                    
                    # prev.next = None
                    # return prev.next
                    
                # c+=1
        if first.next!= sec:
            prev.next = sec
        # if prev.next.next != sec:
        #     return 
        return dummy.next
