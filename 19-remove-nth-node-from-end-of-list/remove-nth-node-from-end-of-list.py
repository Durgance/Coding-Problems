# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        # if head == None or head.next == None:
        #     return 

        slow , fast = dummy, dummy
        for i in range(n):
            fast = fast.next
        
        # if fast == None:
        #     return head.next
        
        
        while fast.next != None :
            slow = slow.next
            fast = fast.next
            
            # for i in range(n):
            #     fast = fast.next.next 
            #     continue
            # fast = fast.next.next
            # slow = slow.next
        # next_ele = fast.next
        # slow.next = next_ele
        # t1 = slow.next.next
        slow.next = slow.next.next



        # print(slow)
        # print(fast)
        return dummy.next