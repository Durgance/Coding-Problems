# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev = None
        curr = head
        while curr!=None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        head = self.reverse(head)
        s = 0
        n=0
        while head!= None:
            s+=head.val*2**n
            n+=1
            head = head.next

        return s