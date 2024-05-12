class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # import numpy as np
        if m*n != len(original):
            return []
        temp = []
        counter_n = 0
        counter_m = 0
        
        t = []
        for i in range(len(original)):
            
            t.append(original[i])
            counter_n +=1
            if counter_n>=n:
                counter_n=0
                temp.append(t)
                t=[]
            # j += 1
        return temp
        # return np.reshape(np.array(original),(m,n))
        