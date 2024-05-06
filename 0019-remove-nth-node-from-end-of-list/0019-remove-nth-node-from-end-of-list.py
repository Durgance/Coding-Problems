# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n ==1:
            return 
        len_list = 0
        temp = head
        while temp:
            len_list+=1
            temp = temp.next
        rem_node = len_list - n
        print(rem_node)
        temp = head
        while temp:
            if rem_node == 0:
                temp.val = temp.next.val
                temp.next = temp.next.next
                break
            if rem_node == 1:
                if temp.next.next == None:
                    temp.next = None
                    break
                temp = temp.next
                temp.val = temp.next.val
                temp.next = temp.next.next
                break
            temp = temp.next
            rem_node-=1
        return head
