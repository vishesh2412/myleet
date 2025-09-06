class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row==n:
                board=[]
                for q in queens:
                    board.append('.'*q+'Q'+'.'*(n-q-1))
                result.append(board)
                return
            
            for i in range(n):
                if col[i] or d1[row-i] or d2[row+i]:
                    continue
                
                queens[row]=i
                d1[row-i]=True
                d2[row+i]=True
                col[i]=True

                backtrack(row+1)

                queens[row]=-1
                d1[row-i]=False
                d2[row+i]=False
                col[i]=False

        result=[]
        queens=[-1]*n
        d1=[False]*(2*n)
        d2=[False]*(2*n)
        col=[False]*n

        backtrack(0)
        return result