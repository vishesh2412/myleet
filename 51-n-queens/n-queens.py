class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(board,row):
            if row==n:
                result.append([''.join(_) for _ in board])
                return
            
            for i in range(n):
                if i in col or row-i in d1 or row+i in d2:
                    continue
                
                col.add(i)
                d1.add(row-i)
                d2.add(row+i)
                board[row][i]='Q'

                backtrack(board,row+1)

                col.remove(i)
                d1.remove(row-i)
                d2.remove(row+i)
                board[row][i]='.'

        result=[]
        board=[['.']*n for _ in range(n)]
        d1=set()
        d2=set()
        col=set()

        backtrack(board,0)
        return result