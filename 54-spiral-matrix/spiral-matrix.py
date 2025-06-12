class Solution(object):
    def spiralOrder(self, matrix):
        m=len(matrix[0])
        n=len(matrix)
        visited=[[0]*m for _ in range(n)]
        completed=[[1]*m for _ in range(n)]
        i,j=0,0
        result=[]
        while(visited!=completed):
            while(i<m and visited[j][i]!=1):
                result.append(matrix[j][i])
                visited[j][i]=1
                i+=1
            i-=1
            j+=1
            while(j<n and visited[j][i]!=1):
                result.append(matrix[j][i])
                visited[j][i]=1
                j+=1
            i-=1
            j-=1
            while(i>=0 and visited[j][i]!=1):
                result.append(matrix[j][i])
                visited[j][i]=1
                i-=1
            i+=1
            j-=1
            while(j>=0 and visited[j][i]!=1):
                result.append(matrix[j][i])
                visited[j][i]=1
                j-=1
            i+=1
            j+=1        
        return result