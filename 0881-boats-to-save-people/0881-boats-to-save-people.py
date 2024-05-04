class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) -1
        boat_count = 0
        while left<=right:
            if people[right] == limit:
                right -= 1
                boat_count += 1
                
            if left == right:
                boat_count += 1
                break
            total_w = people[left] + people[right]
            
            if total_w <= limit:
                boat_count += 1
                left += 1
                right -= 1
            else:
                right-=1
                boat_count += 1
        return boat_count
        