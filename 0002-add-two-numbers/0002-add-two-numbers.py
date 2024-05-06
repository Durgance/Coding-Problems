# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        i=0
        # multi = pow(10,i)
        ans1 = 0
        ans2 = 0
        count1 = 0
        while temp1:
            ans1 += temp1.val*pow(10,i) 
            i+=1
            temp1=temp1.next
            count1+=1
        i =0
        count2= 0
        while temp2:
            ans2 += temp2.val*pow(10,i) 
            i+=1
            temp2=temp2.next
            count2+=1
        total = str(ans1+ans2)
        if count1>= count2:
            temp_count = count1
            temp = l1
            i=1
            while temp:
                temp.val = int(total[-i])
                if temp.next == None and i < len(total):
                    temp.next = ListNode(total[i])
                temp = temp.next
                i+=1

            return l1
        else:
            temp_count = count2
            temp = l2
            i=1
            while temp:
                temp.val = int(total[-i])
                if temp.next == None and i < len(total):
                    temp.next = ListNode(total[i])
                temp = temp.next
                i+=1

            return l2
        