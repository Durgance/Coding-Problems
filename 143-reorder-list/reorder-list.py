# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self,head):
        curr = head
        prev = None
        while curr != None:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        return prev

    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow , fast = head, head
        prev = None
        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # prev.next = None
        rev_head = self.reverse(slow.next)
        slow.next = None
        curr = head
        # rev_head = m
        # print(head)
        # print(rev_head)
        
        while rev_head and curr:
            # print(head)
            # print("--------------")
            t1 = curr.next
            t2 = rev_head.next

            curr.next = rev_head
            rev_head.next = t1

            curr = t1 
            rev_head = t2
            # print(head)
            # print("--------------")
            # print(head)
            # curr = curr.next
            # rev_head = rev_head.next
            # curr.next.next = t1
            # print(head)
            # print("--------------")
            # print("loop")
            # if rev_head.next!= None:
            #     break
            # if rev_head.val == curr.val:
            #     break

            # next_head = next_head.next
            # print(curr)
            

        