class Solution(object):
    def solveNQueens(self, n):
        def isSafe(board,row,col,n):
            for i in range(n):    
                if board[i][col]=='Q':
                    return False
            i=row
            j=col
            while(i>=0 and j>=0):
                if board[i][j]=='Q':
                    return False
                i=i-1
                j=j-1
            i=row
            j=col
            while(i>=0 and j<n):
                if board[i][j]=='Q':
                    return False
                i=i-1
                j=j+1
            return True

        def nQueens(board,row,n):
            if row==n:
                ans.append([''.join(k) for k in board])
                return
    
            for j in range(n):
                if isSafe(board,row,j,n):
                    board[row][j]='Q'
                    nQueens(board,row+1,n)
                    board[row][j]='.'

        ans=[]
        board=[["." for _ in range(n)] for _ in range(n)]
        board=nQueens(board,0,n)
        return ans