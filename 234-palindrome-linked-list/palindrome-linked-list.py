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
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow , fast = head, head
        while fast != None and fast.next != None :
            slow = slow.next
            fast = fast.next.next
        
        new_head = self.reverse(slow)
        slow = head
        while new_head!=None:
            if new_head.val != slow.val:
                return False
            slow = slow.next
            new_head = new_head.next
        
        return True
