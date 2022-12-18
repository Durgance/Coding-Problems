#User function Template for python3

class Solution:
    def solve(self,n,k,stalls):
        
        def cowPass(dist):
            coOrd = stalls[0]
            count = 1
            for i in range(1,n):
                if stalls[i]-coOrd >= dist:
                    count += 1
                    coOrd = stalls[i]
                if count == k:
                    return True
            return False
            
        stalls.sort()
        low = 1
        high = stalls[n-1]-stalls[0]
        while low <= high:
            mid = (low+high)>>1
            if cowPass(mid):
                res = mid
                low = mid+1
            else:
                high = mid-1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends