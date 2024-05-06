class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd tortoise and horse 
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # checking for the entrance to cycle
        
        p1 = nums[0]
        p2 = slow
        while p1!=p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1