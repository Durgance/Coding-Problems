class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seek = []
        for i, row in enumerate(board):
            for j,element in enumerate(row):
                if element!='.':
                    seek.extend([(i,element),(element,j),(i//3,j//3,element)])
        # print(seek)
        return len(set(seek))==len(seek)
