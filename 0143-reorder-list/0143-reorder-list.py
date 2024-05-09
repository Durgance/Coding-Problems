# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            return head
        l = []
        temp = head
        while temp:
            l.append(temp.val)
            temp = temp.next
        
        temp = head
        start = 0
        end = len(l)-1
        while start<=end:
            temp.val = l[start]
            temp = temp.next
            start+=1
            if temp == None:
                break
            temp.val = l[end]
            temp = temp.next
            end -= 1
            if temp == None:
                break
        return head
        