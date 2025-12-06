# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## ASKED GPT TO ADD COMMENT FOR ME TO UNDERSTAND , DID FIRST ON MY OWN -- REMEMBER
        
        # Dummy node to handle edge cases (like duplicates at the head)
        dummy = ListNode(-101, head)

        # first = start of current value group
        # sec   = scanning pointer that moves ahead
        first, sec = dummy, dummy.next

        # prev = last confirmed UNIQUE node in the result list
        prev = None

        while sec is not None:
            # If values are different, we finished scanning a group
            if first.val != sec.val:
                
                # If first.next != sec, there were duplicates in this group
                if first.next != sec:
                    # Skip the entire duplicate group
                    prev.next = sec
                    first = sec
                else:
                    # No duplicates → first was unique
                    prev = first
                    first = first.next

                # Move sec forward to continue scanning
                sec = sec.next

            else:
                # Still inside the same duplicate group
                sec = sec.next

        # ✅ FINAL TAIL CHECK:
        # If the list ended while inside a duplicate group,
        # sec == None and first.next != sec
        if first.next != sec:
            prev.next = sec   # cut off tail duplicates safely

        return dummy.next
        