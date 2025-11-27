class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        quadruplets = []
        # quadruplets = set()
        arr.sort()
        for i in range(len(arr)-3):
            if i>0 and arr[i] == arr[i-1]: continue # skip i dedup
            for j in range(i+1,len(arr)-2):
                if j>i+1 and arr[j]==arr[j-1]: continue # skip j dedup 
                # value = target-arr[i] -arr[j]     
                if i!=j :
                    left = j + 1 
                    right = len(arr)-1
                    while left<right:
                        total = arr[left]+arr[right] +arr[i] + arr[j]
                        if total == target :
                            #  and i!=j and left!=right and i!=left and i!=right and j!=left and j!=right:
                            # quadruplets.add(tuple(sorted([arr[i],arr[j],arr[left],arr[right]])))
                            quadruplets.append([arr[i],arr[j],arr[left],arr[right]])
                            left += 1
                            right -= 1
                            while left<right and arr[left]== arr[left-1]:
                                left += 1
                            while left<right and arr[right] == arr[right+1]:
                                right -= 1
                        elif total<target:
                            left += 1
                        else:
                            right -= 1
        # quadruplets = sorted(quadruplets)
        # print(list(map(list,quadruplets))
        # return list(map(list,quadruplets))
        return quadruplets
        # return list(map(list,quadruplets))