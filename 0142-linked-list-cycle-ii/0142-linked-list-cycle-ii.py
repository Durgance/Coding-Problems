# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return 
        d = {}
        temp = head
        while True:
            if not d.get(temp):
                d[temp] = 1
                if temp == None :
                    return
                if temp.next == None:
                    return
                temp = temp.next
            else:
                # print(d)
                return temp
