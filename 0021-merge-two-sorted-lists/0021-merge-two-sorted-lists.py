# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Node(ListNode):
#     def __init__(self,val=0,next=None):
#         super().__init__(val, next)
    
#     def push(self,node,val):
#         newNode = ListNode(val)
#         node.next = newNode
        

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        ans = temp
        if list1 == None and list2 == None:
            return 
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        while True:
            # print(ans)
            if list1 == None or list2 == None:
                # print(list1)
                # print(list2)
                if list1 == None:
                    ans.next = list2
                    break
                elif list2 == None:
                    ans.next = list1
                    break
                else:
                    break 
            if list1.val > list2.val:
                ans.next = ListNode(list2.val)
                ans = ans.next
                list2 = list2.next 
                continue
                
            elif list1.val < list2.val:
                ans.next = ListNode(list1.val)
                ans = ans.next
                list1 = list1.next
                continue

            if list1.val == list2.val:
                ans.next = ListNode(list1.val)
                ans = ans.next
                ans.next = ListNode(list2.val)
                ans = ans.next
                list1 = list1.next 
                list2 = list2.next
            
        return temp.next