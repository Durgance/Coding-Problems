class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temps)
        
        for i, temp in enumerate(temps):
            while stack and temp > stack[-1][0]:
                temp_t, temp_i = stack.pop()
                result[temp_i] = i - temp_i 
            stack.append([temp,i])
        return result

        
             
