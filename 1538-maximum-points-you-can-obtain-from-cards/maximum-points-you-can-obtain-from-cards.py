class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        # https://chatgpt.com/share/693b3b60-e7a0-800f-ace7-ac926e4f4d04 understanding Window function
        # this problem intution https://chatgpt.com/share/693b3b60-e7a0-800f-ace7-ac926e4f4d04
        
        start = 0
        win_sum = 0
        # min_sum = 0
        min_sum = float('inf')
        n = len(cardPoints)
        
        freq_map = {}
        for end in range(n):
            right_card = cardPoints[end]
            win_sum += right_card

            # if end - start +1>= n - k :
            if end - start +1==n-k:
                min_sum = min(min_sum,win_sum)
        
                left_card = cardPoints[start]
                win_sum -= left_card
                start+=1
                    # print()
                    # print(win_sum)

        
            # if end-start + 1 ==k:
        return sum(cardPoints) - (min_sum if min_sum != float('inf') else 0)