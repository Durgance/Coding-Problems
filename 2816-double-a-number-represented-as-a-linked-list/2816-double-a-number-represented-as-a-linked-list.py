# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr , prev = head , None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        node = prev
        val = 0
        while True:
            val +=  node.val*2
            node.val = val%10
            val = val//10
            if node.next == None and val!=0:
                node.next = ListNode(val)
                break
            if node.next == None:
                break
            node = node.next
        
        curr , prev = prev , None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
