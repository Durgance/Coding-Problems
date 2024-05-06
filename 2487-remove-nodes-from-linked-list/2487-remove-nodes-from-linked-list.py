# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse LL
        prev , curr = None , head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        temp = prev
        max_val = 0
        flag = False
        # Find the element and remove if last element needs to remove remove while reversing
        while temp:
            max_val = max(max_val,temp.val)    
            if max_val > temp.val:
                if temp.next == None:
                    flag = True
                    break
                temp.val = temp.next.val
                temp.next = temp.next.next
            else:
                temp = temp.next
        # reverse the list again
        prev , curr = None , prev
        while curr:
            if flag == True and curr.next == None:
                curr.next = None
                break
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev