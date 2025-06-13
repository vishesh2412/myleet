class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m=len(board),len(board[0])

        def backtrack(i,j,counter):
            if counter==len(word):
                return True
            if i<0 or i>=n or j<0 or j>=m:
                return False
            if board[i][j]!=word[counter]:
                return False

            temp=board[i][j]
            board[i][j]='#'

            trial=backtrack(i+1,j,counter+1) or backtrack(i,j+1,counter+1) or backtrack(i-1,j,counter+1) or backtrack(i,j-1,counter+1)

            board[i][j]=temp
            return trial
        
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    if backtrack(i,j,0):
                        return True
        return False    