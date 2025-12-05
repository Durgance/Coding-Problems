# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None :
            return None
        slow , fast = head , head
        cycle_len = 0
        flag = False
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow = slow.next

            if slow == fast:
                # found cycle
                flag = True
                curr = slow 
                while True:
                    curr = curr.next
                    cycle_len += 1
                    if curr == slow:
                        break
                        # found length reached back to start
                break
                # found cycle length
        if flag == False:
            return None

        pointer_1 = head
        pointer_2 = head
        for i in range(cycle_len):
            pointer_2 = pointer_2.next
        # n = 0
        while True:
            if pointer_1 == pointer_2:
                return pointer_1
            # n+=1
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next

            
                    